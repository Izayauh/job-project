"""
Resume Markdown-to-PDF converter using fpdf2.
Reads the plain-text resume block from a tailored .md file and outputs a clean,
recruiter-safe single-page PDF.

Usage:
    python resume_to_pdf.py <input.md> [output.pdf]

If output.pdf is not specified, saves alongside the input file.
"""

import sys
import re
from pathlib import Path
from fpdf import FPDF


def sanitize_text(text: str) -> str:
    """Replace Unicode characters that standard fonts can't handle."""
    replacements = {
        '\u2014': '-',   # em-dash
        '\u2013': '-',   # en-dash
        '\u2018': "'",   # left single quote
        '\u2019': "'",   # right single quote
        '\u201c': '"',   # left double quote
        '\u201d': '"',   # right double quote
        '\u2026': '...', # ellipsis
        '\u2022': '*',   # bullet (we handle our own bullets)
        '\u2500': '-',   # box-drawing horizontal
        '\u2501': '-',   # box-drawing horizontal heavy
        '\u2502': '|',   # box-drawing vertical
        '\u25cf': '*',   # black circle
    }
    for char, repl in replacements.items():
        text = text.replace(char, repl)
    # Replace any remaining box-drawing chars (U+2500 to U+257F)
    text = re.sub(r'[\u2500-\u257F]', '-', text)
    return text


class ResumePDF(FPDF):
    def __init__(self):
        super().__init__(format="letter")
        self.set_auto_page_break(auto=False)
        # Margins: tight but readable
        self.set_margins(left=12, top=10, right=12)

    def add_resume_page(self, lines: list[str], font_size: float = 8.6):
        self.add_page()
        self.set_font("Helvetica", size=font_size)
        line_height = font_size * 0.45  # tighter line spacing
        # Sanitize all lines upfront
        lines = [sanitize_text(line) for line in lines]

        y = self.t_margin
        page_bottom = self.h - 10  # bottom margin

        for line in lines:
            if y + line_height > page_bottom:
                return False  # didn't fit

            # Detect section headers (ALL CAPS lines)
            is_header = bool(re.match(r'^[A-Z][A-Z &/]+$', line.strip()))
            # Detect separator lines
            is_separator = line.strip().startswith('─') or line.strip().startswith('---')
            # Detect name line (first non-empty line, usually all caps name)
            is_name = (y == self.t_margin and line.strip() and
                       re.match(r'^[A-Z][A-Z ]+$', line.strip()))

            if is_separator:
                # Draw a thin line instead of the text
                y += line_height * 0.3
                self.set_draw_color(180, 180, 180)
                self.line(self.l_margin, y, self.w - self.r_margin, y)
                y += line_height * 0.7
                continue

            if is_name:
                self.set_font("Helvetica", "B", size=font_size + 6)
                self.set_xy(self.l_margin, y)
                self.cell(w=0, h=line_height + 2, text=line.strip(), align="C")
                self.set_font("Helvetica", size=font_size)
                y += line_height + 3
                continue

            if is_header:
                y += line_height * 0.4  # space before header
                self.set_font("Helvetica", "B", size=font_size + 1)
                self.set_xy(self.l_margin, y)
                self.cell(w=0, h=line_height + 1, text=line.strip())
                self.set_font("Helvetica", size=font_size)
                y += line_height + 2
                continue

            # Contact line (right after name, contains | separators and @)
            if y < self.t_margin + 15 and '|' in line and not line.strip().startswith('•'):
                self.set_font("Helvetica", size=font_size - 0.5)
                self.set_xy(self.l_margin, y)
                self.cell(w=0, h=line_height, text=line.strip(), align="C")
                self.set_font("Helvetica", size=font_size)
                y += line_height + 0.5
                continue

            # Bullet points
            if line.strip().startswith('•'):
                self.set_xy(self.l_margin + 4, y)
                # Handle wrapped bullet text
                text = line.strip()
                self.multi_cell(
                    w=self.w - self.l_margin - self.r_margin - 4,
                    h=line_height,
                    text=text,
                )
                y = self.get_y() + 0.3
                continue

            # Continuation of bullet (indented, no bullet marker)
            if line.startswith('    ') and line.strip() and not is_header:
                # Check if this is a skills sub-line (contains colons for alignment)
                self.set_xy(self.l_margin + 4, y)
                self.multi_cell(
                    w=self.w - self.l_margin - self.r_margin - 4,
                    h=line_height,
                    text=line.strip(),
                )
                y = self.get_y() + 0.3
                continue

            # Sub-header lines (job titles, project names, etc.)
            # These often contain em-dash and dates
            if '—' in line or ('–' in line and any(str(yr) in line for yr in range(2019, 2027))):
                self.set_font("Helvetica", "B", size=font_size)
                self.set_xy(self.l_margin, y)
                self.cell(w=0, h=line_height, text=line.strip())
                self.set_font("Helvetica", size=font_size)
                y += line_height + 0.3
                continue

            # URL lines (project links)
            if line.strip().startswith(('github.com', 'http', 'linkedin', 'impulse-')):
                self.set_font("Helvetica", size=font_size - 0.8)
                self.set_text_color(80, 80, 80)
                self.set_xy(self.l_margin + 4, y)
                self.cell(w=0, h=line_height, text=line.strip())
                self.set_text_color(0, 0, 0)
                self.set_font("Helvetica", size=font_size)
                y += line_height + 0.3
                continue

            # Empty lines — add small spacing
            if not line.strip():
                y += line_height * 0.4
                continue

            # Default: regular text
            self.set_xy(self.l_margin, y)
            self.multi_cell(
                w=self.w - self.l_margin - self.r_margin,
                h=line_height,
                text=line.strip() if line.strip() else "",
            )
            y = self.get_y() + 0.2

        return True  # everything fit


def extract_resume_text(md_path: str) -> list[str]:
    """Extract the plain-text resume block from between ``` fences."""
    content = Path(md_path).read_text(encoding="utf-8")

    # Find content between ``` markers
    match = re.search(r'```\n(.*?)```', content, re.DOTALL)
    if not match:
        print("Error: Could not find a ``` code block in the file.")
        sys.exit(1)

    return match.group(1).split('\n')


def main():
    if len(sys.argv) < 2:
        print("Usage: python resume_to_pdf.py <input.md> [output.pdf]")
        sys.exit(1)

    input_path = sys.argv[1]
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        output_path = str(Path(input_path).with_suffix('.pdf'))

    lines = extract_resume_text(input_path)

    # Try to fit on one page, reducing font size if needed
    for font_size in [8.6, 8.2, 7.8, 7.5, 7.2, 7.0]:
        pdf = ResumePDF()
        if pdf.add_resume_page(lines, font_size=font_size):
            pdf.output(output_path)
            print(f"PDF saved: {output_path} (font size: {font_size})")
            return
        print(f"  Font size {font_size} didn't fit on one page, trying smaller...")

    # Last resort — just output it even if it overflows
    pdf = ResumePDF()
    pdf.add_resume_page(lines, font_size=7.0)
    pdf.output(output_path)
    print(f"PDF saved: {output_path} (WARNING: may exceed one page)")


if __name__ == "__main__":
    main()
