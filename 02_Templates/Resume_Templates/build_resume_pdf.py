"""Generate PDF resume for AI Content Evaluator application."""
from fpdf import FPDF

class ResumePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)

    def _clean(self, text):
        """Replace unicode chars that core fonts can't handle."""
        return text.replace("\u2014", "-").replace("\u2013", "-").replace("\u2022", "-").replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')

    def section_header(self, text):
        self.set_font("Helvetica", "B", 11)
        self.cell(0, 7, self._clean(text), new_x="LMARGIN", new_y="NEXT")
        # Draw line under header
        self.set_draw_color(60, 60, 60)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 5, self._clean(text), new_x="LMARGIN", new_y="NEXT")

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.cell(5, 5, "-", new_x="END")
        self.multi_cell(0, 5, self._clean(text), new_x="LMARGIN", new_y="NEXT")

    def job_title(self, title, company):
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 6, self._clean(f"{title} - {company}"), new_x="LMARGIN", new_y="NEXT")

    def job_meta(self, text):
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, self._clean(text), new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def project_title(self, name, subtitle=""):
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 6, self._clean(name), new_x="LMARGIN", new_y="NEXT")
        if subtitle:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(80, 80, 80)
            self.cell(0, 5, self._clean(subtitle), new_x="LMARGIN", new_y="NEXT")
            self.set_text_color(0, 0, 0)
        self.ln(1)


def build():
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_margins(18, 15, 18)

    # ── Name ──
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 10, "ISAIAH WASHINGTON", align="C", new_x="LMARGIN", new_y="NEXT")

    # ── Contact line ──
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 5, pdf._clean("Cincinnati, OH  |  Remote  |  513.544.9022  |  isaiahwashington48@gmail.com"), align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 5, pdf._clean("linkedin.com/in/isaiah-washington48  |  github.com/Izayauh/whisper"), align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(4)

    # ── Summary ──
    pdf.section_header("PROFESSIONAL SUMMARY")
    pdf.body_text(
        "Detail-oriented technical professional with 4+ years of remote work experience "
        "and hands-on knowledge of AI systems including large language models, speech-to-text "
        "inference, and multi-agent architectures. Built AI-powered applications using Google "
        "Gemini API and OpenAI Whisper, giving me practical understanding of how AI generates "
        "content, where it fails, and what quality output looks like. Strong written "
        "communicator with 1,500+ hours of remote customer-facing support experience."
    )
    pdf.ln(3)

    # ── Skills ──
    pdf.section_header("RELEVANT SKILLS")

    skills = [
        ("AI & Machine Learning:", "Google Gemini API (function calling, real-time audio), OpenAI Whisper (local inference), NVIDIA CUDA, prompt engineering, multi-agent systems, AI output evaluation"),
        ("Written Communication:", "Technical documentation, customer-facing correspondence, structured troubleshooting write-ups, ticket management"),
        ("Tools & Platforms:", "Python, Git, GitHub, Windows/WSL, Google Workspace, spreadsheet-based data systems"),
        ("Work Style:", "100% remote for 4+ years, self-directed, deadline-driven, consistent availability"),
    ]
    for label, detail in skills:
        pdf.set_font("Helvetica", "B", 9.5)
        pdf.cell(44, 5, label, new_x="END")
        pdf.set_font("Helvetica", "", 9.5)
        pdf.multi_cell(0, 5, detail, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)
    pdf.ln(2)

    # ── Projects ──
    pdf.section_header("AI PROJECT EXPERIENCE")

    pdf.project_title("Impulse — Privacy-First Dictation App", "github.com/Izayauh/whisper")
    for b in [
        "Built a GPU-accelerated speech-to-text application using Python and OpenAI Whisper, published as a public beta on GitHub (57 commits, 2 releases)",
        "Evaluated and compared AI model outputs across multiple Whisper model sizes, selecting optimal models based on accuracy, speed, and context length",
        "Handled full product lifecycle from ML inference tuning through UI design, documentation, and beta distribution",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.project_title("Live Pilot — Voice-Controlled AI Assistant", "(Functional Prototype)")
    for b in [
        "Built a voice-controlled AI assistant using Python, Google Gemini API, and OSC protocol with a 6-agent architecture and 62 tool functions",
        "Designed a deterministic execution pipeline to control AI output quality, replacing unpredictable iterative LLM loops with structured PLAN/EXECUTE/VERIFY/REPORT stages",
        "Evaluated and refined AI-generated responses across dozens of use cases to ensure accuracy and reliability",
    ]:
        pdf.bullet(b)
    pdf.ln(3)

    # ── Experience ──
    pdf.section_header("PROFESSIONAL EXPERIENCE")

    pdf.job_title("Network Support Technician", "Nexus WiFi")
    pdf.job_meta("Oct 2021 – Present  |  West Chester, OH (100% Remote)")
    for b in [
        "Provide remote technical support across 150+ managed properties, triaging issues with downed infrastructure, connectivity outages, and device failures",
        "Deliver 1,500+ hours of 100% remote customer-facing support with consistent written follow-up and ticket documentation",
        "Follow structured diagnostic workflows requiring careful attention to detail: clarify scope, verify symptoms, walk through troubleshooting, reference past tickets, and escalate when needed",
        "Manage active tickets using an in-house platform, including outbound follow-up and status updates",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.job_title("Administrative Assistant", "Midway Auto Group")
    pdf.job_meta("Jan 2019 – Dec 2023  |  Middletown, OH")
    for b in [
        "Built and maintained a spreadsheet-based inventory tracking system covering cost, deliveries, and usage across full vehicle stock",
        "Managed data input with attention to accuracy and consistency",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.job_title("Key Accounts Team Assistant", "Cincinnati Insurance Company")
    pdf.job_meta("Feb 2023 – Aug 2023  |  Fairfield, OH")
    pdf.bullet("Managed data input for key insured account policies, coordinating with underwriters and assistants to ensure accuracy")
    pdf.ln(3)

    # ── Education ──
    pdf.section_header("EDUCATION")

    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, pdf._clean("Miami University - Cincinnati, OH"), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 5, pdf._clean("Business Management Technology coursework - 67 credit hours toward Associate of Applied Business"), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "I", 9.5)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 5, "Attended through Spring 2024", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)

    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, pdf._clean("Google IT Support Certification - Coursera, November 2022"), new_x="LMARGIN", new_y="NEXT")

    # ── Output ──
    out_path = r"C:\Users\isaia\Documents\Job_Project\02_Templates\Resume_Templates\Isaiah_Washington_Resume_AI_Content_Evaluator.pdf"
    pdf.output(out_path)
    print(f"PDF saved to: {out_path}")


if __name__ == "__main__":
    build()
