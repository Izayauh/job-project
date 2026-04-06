"""Generate ATS-optimized PDF resume for Plaid TSE v2."""
from fpdf import FPDF
import os


class ResumePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)

    def _c(self, text):
        return text.replace("\u2014", "-").replace("\u2013", "-").replace("\u2022", "-").replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')

    def section_header(self, text):
        self.set_font("Helvetica", "B", 11)
        self.cell(0, 7, self._c(text), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(60, 60, 60)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 5, self._c(text), new_x="LMARGIN", new_y="NEXT")

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.cell(5, 5, "-", new_x="END")
        self.multi_cell(0, 5, self._c(text), new_x="LMARGIN", new_y="NEXT")

    def job_title(self, title, company):
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 6, self._c(f"{title} - {company}"), new_x="LMARGIN", new_y="NEXT")

    def job_meta(self, text):
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, self._c(text), new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def project_title(self, name, subtitle=""):
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 6, self._c(name), new_x="LMARGIN", new_y="NEXT")
        if subtitle:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(80, 80, 80)
            self.cell(0, 5, self._c(subtitle), new_x="LMARGIN", new_y="NEXT")
            self.set_text_color(0, 0, 0)
        self.ln(1)

    def skill_row(self, label, detail):
        self.set_font("Helvetica", "B", 9.5)
        self.cell(40, 5, self._c(label), new_x="END")
        self.set_font("Helvetica", "", 9.5)
        self.multi_cell(0, 5, self._c(detail), new_x="LMARGIN", new_y="NEXT")
        self.ln(1)


def build():
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_margins(18, 15, 18)

    # Header
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 10, "ISAIAH WASHINGTON", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 5, pdf._c("Cincinnati, OH (Eastern Time)  |  Remote  |  513.544.9022  |  isaiahwashington48@gmail.com"), align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 5, pdf._c("linkedin.com/in/isaiah-washington48  |  github.com/Izayauh/whisper"), align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(4)

    # Summary
    pdf.section_header("PROFESSIONAL SUMMARY")
    pdf.body_text(
        "Technical Support Engineer with 4+ years of remote, customer-facing experience "
        "troubleshooting infrastructure and connectivity issues across 150+ managed properties. "
        "Experienced in using ticketing systems, internal tools, and structured diagnostic workflows "
        "to investigate root cause, resolve technical issues, and escalate effectively. Collaborative "
        "problem-solver who builds Python-based tooling independently, including coding projects that "
        "integrate REST APIs and multi-agent architectures. Customer-centric communicator with strong "
        "written and verbal communication skills who is empathetic to customer needs and genuinely "
        "passionate about delivering a world-class support experience. Eager to bring collaboration "
        "and technical depth to a financial services team helping customers resolve complex "
        "integration issues."
    )
    pdf.ln(3)

    # Skills
    pdf.section_header("TECHNICAL SKILLS")
    pdf.skill_row("Languages & Coding:", "Python, JavaScript, HTML, CSS, SQL (coursework)")
    pdf.skill_row("APIs & Integration:", "REST APIs, API debugging and testing, Google Gemini API (function calling), OSC protocol, structured request/response handling")
    pdf.skill_row("Ticketing & Tools:", "Ticketing systems (Jira, Zendesk), internal tools, browser developer tools, documentation platforms")
    pdf.skill_row("Tooling & Platforms:", "Git, GitHub, Vercel, Windows/WSL, Google Workspace")
    pdf.skill_row("Certification:", "Google IT Support - Coursera, 2022")
    pdf.ln(2)

    # Experience
    pdf.section_header("EXPERIENCE")

    pdf.job_title("Network Support Technician", "Nexus WiFi")
    pdf.job_meta("Oct 2021 - Present  |  West Chester, OH (100% Remote)")
    for b in [
        "Provide remote technical support across 150+ managed properties, troubleshooting downed infrastructure, connectivity outages, and device failures while balancing multiple priorities through effective time management",
        "Deliver 1,500+ hours of customer-facing support, taking an empathetic and customer-centric approach to understanding customer needs and guiding users through troubleshooting and resolution",
        "Investigate root cause of connectivity failures using internal tools and documentation, following structured diagnostic workflows to clarify scope, verify symptoms, and escalate through collaboration with appropriate teams when outside scope",
        "Manage 5-10 tickets per morning shift and 2-5 per night shift using ticketing systems, including detailed documentation, outbound follow-up, and status updates",
        "Diagnose and triage issues with access points, switches, gateways, and modems, coordinating hardware replacement and collaborating cross-functionally with field technicians and vendors",
        "Work independently in a fully remote environment as a self-starter, proactively managing daily ticket queues and prioritizing urgent customer issues while maintaining consistent collaboration with team members",
        "Contribute to process improvement by identifying recurring issues, documenting solutions for future reference, and refining troubleshooting workflows",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.job_title("Key Accounts Team Assistant", "The Cincinnati Insurance Company")
    pdf.job_meta("Feb 2023 - Aug 2023  |  Fairfield, OH (Financial Services)")
    for b in [
        "Managed data input for key insured account policies in a financial services environment, coordinating with underwriters and assistants to ensure accuracy and meet customer needs",
        "Gained direct exposure to financial services operations, compliance workflows, and collaborative cross-functional coordination between teams",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.job_title("Administrative Assistant", "Midway Auto Group")
    pdf.job_meta("Jan 2019 - Dec 2023  |  Middletown, OH")
    for b in [
        "Built and maintained a spreadsheet-based inventory tracking system covering cost, deliveries, and usage across the dealership's full vehicle stock",
        "Assisted walk-in clients, scheduled appointments, and answered phone lines in a customer-facing administrative role, developing strong written and verbal communication skills",
    ]:
        pdf.bullet(b)
    pdf.ln(3)

    # Technical Projects
    pdf.section_header("TECHNICAL PROJECTS")

    pdf.project_title("Impulse - Privacy-First Dictation App", "github.com/Izayauh/whisper  |  impulse-eight-lake.vercel.app")
    for b in [
        "Built and shipped a GPU-accelerated speech-to-text dictation app for Windows using Python coding and OpenAI Whisper, published as a public beta on GitHub (57 commits, 2 releases)",
        "Built a product landing page using JavaScript, HTML, CSS, React, TypeScript, and Tailwind CSS deployed on Vercel with working beta signup flow and interactive demo",
        "Handled full product lifecycle including tooling, documentation, UI design, installer packaging, and beta distribution",
        "Contributed to process improvement through brainstorming sessions on feature prioritization, user feedback integration, and iterative development",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.project_title("Live Pilot - Voice-Controlled AI DAW Assistant", "(Functional Prototype)")
    for b in [
        "Built a voice-controlled AI assistant for Ableton Live using Python coding, Google Gemini REST API, and OSC protocol with a 6-agent architecture and 62 tool functions",
        "Integrated REST API endpoints for real-time audio processing and function calling, with structured request/response handling, debugging of integration issues, and collaborative iteration on design decisions",
        "Designed internal tooling to replace iterative LLM loops with a deterministic pipeline, reducing API calls per operation from 30+ to 1",
    ]:
        pdf.bullet(b)
    pdf.ln(3)

    # Education
    pdf.section_header("EDUCATION")

    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, pdf._c("Miami University - Cincinnati, OH"), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 5, pdf._c("Business Management Technology coursework - 67 credit hours toward Associate of Applied Business"), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "I", 9.5)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 5, pdf._c("Attended through Spring 2024"), new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.cell(0, 5, pdf._c("Relevant coursework: Database Design & Development (SQL), HTML/CSS/JavaScript"), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, pdf._c("Google IT Support Certification - Coursera, November 2022"), new_x="LMARGIN", new_y="NEXT")

    out = os.path.join(os.path.dirname(__file__), "Resume_Plaid_TSE_v3.pdf")
    pdf.output(out)
    print(f"PDF saved to: {out}")


if __name__ == "__main__":
    build()
