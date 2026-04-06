"""Generate PDF resumes for Plaid, Turvo, and Total Expert applications."""
from fpdf import FPDF
import os

BASE = r"C:\Users\isaia\Documents\Job_Project\04_Applications"


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
        self.cell(44, 5, self._c(label), new_x="END")
        self.set_font("Helvetica", "", 9.5)
        self.multi_cell(0, 5, self._c(detail), new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def header_block(self, name, contact1, contact2):
        self.set_font("Helvetica", "B", 18)
        self.cell(0, 10, self._c(name), align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(80, 80, 80)
        self.cell(0, 5, self._c(contact1), align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, self._c(contact2), align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(4)

    def edu_entry(self, school, detail, attended, coursework=None):
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 6, self._c(school), new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 10)
        self.cell(0, 5, self._c(detail), new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "I", 9.5)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, self._c(attended), new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        if coursework:
            self.set_font("Helvetica", "", 9.5)
            self.cell(0, 5, self._c(f"Relevant coursework: {coursework}"), new_x="LMARGIN", new_y="NEXT")
        self.ln(3)


def build_plaid():
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_margins(18, 15, 18)

    pdf.header_block(
        "ISAIAH WASHINGTON",
        "Cincinnati, OH (Eastern Time)  |  Remote  |  513.544.9022  |  isaiahwashington48@gmail.com",
        "linkedin.com/in/isaiah-washington48  |  github.com/Izayauh/whisper"
    )

    pdf.section_header("PROFESSIONAL SUMMARY")
    pdf.body_text(
        "Technical support professional with 4+ years of remote experience triaging infrastructure and "
        "connectivity issues across 150+ managed properties. 1,500+ hours of direct customer-facing support "
        "through structured diagnostic workflows. Builds Python-based tools independently, including a shipped "
        "dictation app with GPU acceleration and a voice-controlled AI assistant integrating REST APIs and "
        "multi-agent architecture. Google IT Support certified. Seeking a Technical Support Engineer role "
        "grounded in API troubleshooting, customer communication, and technical investigation."
    )
    pdf.ln(3)

    pdf.section_header("TECHNICAL SKILLS")
    pdf.skill_row("Languages & Web:", "Python, JavaScript, HTML/CSS, SQL (coursework), React, TypeScript, Tailwind CSS")
    pdf.skill_row("APIs & Integration:", "REST APIs, Google Gemini API (function calling), OSC protocol, API debugging and testing")
    pdf.skill_row("Support & Operations:", "Remote troubleshooting, device and infrastructure triage, ticket management, structured diagnostic workflows, escalation handling")
    pdf.skill_row("Tools & Platforms:", "Git, GitHub, Windows/WSL, Vercel, in-house ticketing platforms, Google Workspace")
    pdf.skill_row("Certification:", "Google IT Support - Coursera, 2022")
    pdf.ln(2)

    pdf.section_header("EXPERIENCE")
    pdf.job_title("Network Support Technician", "Nexus WiFi")
    pdf.job_meta("Oct 2021 - Present  |  West Chester, OH (100% Remote)")
    for b in [
        "Provide remote technical support across 150+ managed properties, triaging issues with downed infrastructure, connectivity outages, and device failures",
        "Deliver 1,500+ hours of 100% remote customer-facing support, guiding users through troubleshooting and resolution",
        "Diagnose and triage issues with access points, switches, gateways, and modems, coordinating hardware replacement when needed",
        "Follow structured diagnostic workflow: clarify scope, check for downed devices, walk through troubleshooting, reference past tickets, and escalate when outside scope",
        "Manage active tickets using an in-house platform, including outbound follow-up calls and status updates",
        "Resolve an estimated 5-10 tickets per morning shift and 2-5 per night shift through remote troubleshooting and coordination",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.job_title("Key Accounts Team Assistant", "The Cincinnati Insurance Company")
    pdf.job_meta("Feb 2023 - Aug 2023  |  Fairfield, OH")
    pdf.bullet("Managed data input for key insured account policies, coordinating with underwriters and assistants to ensure accuracy")
    pdf.ln(2)

    pdf.job_title("Administrative Assistant", "Midway Auto Group")
    pdf.job_meta("Jan 2019 - Dec 2023  |  Middletown, OH")
    pdf.bullet("Built and maintained a spreadsheet-based inventory tracking system covering cost, deliveries, and usage across the dealership's full vehicle stock")
    pdf.bullet("Assisted walk-in clients, scheduled appointments, and answered phone lines in a client-facing administrative role")
    pdf.ln(3)

    pdf.section_header("PROJECTS")
    pdf.project_title("Impulse - Privacy-First Dictation App", "github.com/Izayauh/whisper  |  impulse-eight-lake.vercel.app")
    for b in [
        "Built and shipped a GPU-accelerated speech-to-text dictation app for Windows using Python and OpenAI Whisper, published as a public beta on GitHub (57 commits, 2 releases)",
        "Built a product landing page using React, TypeScript, Tailwind CSS, and Vercel with working beta signup flow and interactive demo",
        "Handled full product lifecycle: local ML inference, GPU optimization, UI design, installer packaging, documentation, and beta distribution",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.project_title("Live Pilot - Voice-Controlled AI DAW Assistant", "(Functional Prototype)")
    for b in [
        "Built a voice-controlled AI assistant for Ableton Live using Python, Google Gemini API, and OSC protocol with a 6-agent architecture and 62 tool functions",
        "Integrated REST API endpoints for real-time audio processing and function calling, with structured request/response handling",
        "Designed a deterministic pipeline replacing iterative LLM loops, reducing API calls per operation from 30+ to 1",
    ]:
        pdf.bullet(b)
    pdf.ln(3)

    pdf.section_header("EDUCATION")
    pdf.edu_entry("Miami University - Cincinnati, OH", "Business Management Technology coursework - 67 credit hours toward Associate of Applied Business", "Attended through Spring 2024", "Database Design & Development, HTML/CSS/JavaScript")
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, pdf._c("Google IT Support Certification - Coursera, November 2022"), new_x="LMARGIN", new_y="NEXT")

    out = os.path.join(BASE, "Plaid", "Resume_Plaid_TSE.pdf")
    pdf.output(out)
    print(f"Plaid PDF: {out}")


def build_turvo():
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_margins(18, 15, 18)

    pdf.header_block(
        "ISAIAH WASHINGTON",
        "Cincinnati, OH  |  Open to Austin/Dallas, TX and Remote  |  513.544.9022  |  isaiahwashington48@gmail.com",
        "linkedin.com/in/isaiah-washington48  |  github.com/Izayauh/whisper"
    )

    pdf.section_header("PROFESSIONAL SUMMARY")
    pdf.body_text(
        "Technical support professional with 4+ years of remote experience performing root-cause analysis and "
        "troubleshooting across 150+ managed properties. 1,500+ hours of direct customer-facing support using "
        "structured diagnostic workflows, escalation handling, and detailed ticket documentation. Builds "
        "Python-based tools independently, including API integration work with REST endpoints and structured "
        "request/response debugging. Seeking a Customer Support Engineer role where troubleshooting depth, "
        "scripting ability, and clear technical communication create value."
    )
    pdf.ln(3)

    pdf.section_header("TECHNICAL SKILLS")
    pdf.skill_row("Troubleshooting:", "Root-cause analysis, structured diagnostic workflows, device and infrastructure triage, connectivity issue resolution, escalation handling")
    pdf.skill_row("Programming & APIs:", "Python scripting, REST APIs, Google Gemini API (function calling), HTML/CSS/JavaScript, SQL (coursework)")
    pdf.skill_row("Documentation:", "Ticket documentation, structured follow-up write-ups, customer-facing correspondence, process documentation")
    pdf.skill_row("Tools & Platforms:", "Git, GitHub, Windows/WSL, browser developer tools, in-house ticketing platforms, Google Workspace")
    pdf.skill_row("Certification:", "Google IT Support - Coursera, 2022")
    pdf.ln(2)

    pdf.section_header("EXPERIENCE")
    pdf.job_title("Network Support Technician", "Nexus WiFi")
    pdf.job_meta("Oct 2021 - Present  |  West Chester, OH (100% Remote)")
    for b in [
        "Provide remote technical support across 150+ managed properties, triaging issues with downed infrastructure, connectivity outages, and device failures",
        "Deliver 1,500+ hours of 100% remote customer-facing support, guiding users through troubleshooting and resolution",
        "Perform root-cause analysis on connectivity failures by clarifying scope, checking for downed devices, walking through structured diagnostics, referencing past tickets, and escalating when outside scope",
        "Diagnose and triage issues with access points, switches, gateways, and modems, coordinating hardware replacement when needed",
        "Manage active tickets using an in-house platform with detailed documentation, outbound follow-up calls, and status updates",
        "Resolve an estimated 5-10 tickets per morning shift and 2-5 per night shift through remote troubleshooting and coordination",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.job_title("Key Accounts Team Assistant", "The Cincinnati Insurance Company")
    pdf.job_meta("Feb 2023 - Aug 2023  |  Fairfield, OH")
    pdf.bullet("Managed data input for key insured account policies, coordinating with underwriters and assistants to ensure accuracy")
    pdf.ln(2)

    pdf.job_title("Administrative Assistant", "Midway Auto Group")
    pdf.job_meta("Jan 2019 - Dec 2023  |  Middletown, OH")
    pdf.bullet("Built and maintained a spreadsheet-based inventory tracking system covering cost, deliveries, and usage across the dealership's full vehicle stock")
    pdf.bullet("Improved visibility and organization across dealership operations during a period of significant business growth")
    pdf.ln(3)

    pdf.section_header("PROJECTS")
    pdf.project_title("Impulse - Privacy-First Dictation App", "github.com/Izayauh/whisper  |  impulse-eight-lake.vercel.app")
    for b in [
        "Built and shipped a GPU-accelerated speech-to-text dictation app for Windows using Python and OpenAI Whisper, published as a public beta on GitHub (57 commits, 2 releases)",
        "Handled full product lifecycle: local ML inference, GPU optimization, UI design, installer packaging, documentation, and beta distribution",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.project_title("Live Pilot - Voice-Controlled AI DAW Assistant", "(Functional Prototype)")
    for b in [
        "Built a voice-controlled AI assistant for Ableton Live using Python, Google Gemini API, and OSC protocol with a 6-agent architecture and 62 tool functions",
        "Integrated REST API endpoints with structured request/response handling, debugging API call failures and optimizing request flow",
        "Designed a deterministic pipeline replacing iterative LLM loops, reducing API calls per operation from 30+ to 1",
    ]:
        pdf.bullet(b)
    pdf.ln(3)

    pdf.section_header("EDUCATION")
    pdf.edu_entry("Miami University - Cincinnati, OH", "Business Management Technology coursework - 67 credit hours toward Associate of Applied Business", "Attended through Spring 2024")
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, pdf._c("Google IT Support Certification - Coursera, November 2022"), new_x="LMARGIN", new_y="NEXT")

    out = os.path.join(BASE, "Turvo", "Resume_Turvo_CSE.pdf")
    pdf.output(out)
    print(f"Turvo PDF: {out}")


def build_total_expert():
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_margins(18, 15, 18)

    pdf.header_block(
        "ISAIAH WASHINGTON",
        "Cincinnati, OH  |  Remote  |  513.544.9022  |  isaiahwashington48@gmail.com",
        "linkedin.com/in/isaiah-washington48  |  github.com/Izayauh/whisper"
    )

    pdf.section_header("PROFESSIONAL SUMMARY")
    pdf.body_text(
        "Technical professional with 4+ years of remote customer-facing support and a track record of building "
        "operational systems from scratch. Built and maintained tracking systems, managed onboarding-adjacent "
        "configuration work, and delivered 1,500+ hours of direct customer communication. Independently shipped "
        "a software product through full lifecycle from requirements through documentation and distribution. "
        "Seeking an implementation-focused role where customer communication, technical configuration, and "
        "structured delivery drive results."
    )
    pdf.ln(3)

    pdf.section_header("TECHNICAL SKILLS")
    pdf.skill_row("Implementation & Delivery:", "System configuration, onboarding support, QA testing, process documentation, full product lifecycle delivery")
    pdf.skill_row("Customer-Facing:", "Remote troubleshooting (1,500+ hours), customer guidance, cross-functional coordination, ticket workflow management, status reporting")
    pdf.skill_row("Languages & Tools:", "Python, HTML/CSS/JavaScript, SQL (coursework), React, TypeScript, Git, GitHub, Vercel")
    pdf.skill_row("Platforms:", "Windows/WSL, Google Workspace, in-house ticketing platforms, spreadsheet-based tracking systems")
    pdf.ln(2)

    pdf.section_header("EXPERIENCE")
    pdf.job_title("Network Support Technician", "Nexus WiFi")
    pdf.job_meta("Oct 2021 - Present  |  West Chester, OH (100% Remote)")
    for b in [
        "Provide remote technical support across 150+ managed properties, triaging issues with downed infrastructure, connectivity outages, and device failures",
        "Deliver 1,500+ hours of 100% remote customer-facing support, guiding users through troubleshooting and resolution",
        "Follow structured diagnostic workflow: clarify scope, check for downed devices, walk through troubleshooting, reference past tickets, and escalate when outside scope",
        "Perform camera setup and implementation work alongside core network support responsibilities",
        "Manage active tickets using an in-house platform, including outbound follow-up calls and status updates",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.job_title("Administrative Assistant", "Midway Auto Group")
    pdf.job_meta("Jan 2019 - Dec 2023  |  Middletown, OH")
    pdf.bullet("Built and maintained a spreadsheet-based inventory tracking system covering cost, deliveries, and usage across the dealership's full vehicle stock")
    pdf.bullet("Improved visibility and organization across dealership operations during a period of significant business growth")
    pdf.ln(2)

    pdf.job_title("Key Accounts Team Assistant", "The Cincinnati Insurance Company")
    pdf.job_meta("Feb 2023 - Aug 2023  |  Fairfield, OH")
    pdf.bullet("Managed data input for key insured account policies, coordinating with underwriters and assistants to ensure accuracy")
    pdf.ln(3)

    pdf.section_header("PROJECTS")
    pdf.project_title("Impulse - Privacy-First Dictation App", "github.com/Izayauh/whisper  |  impulse-eight-lake.vercel.app")
    for b in [
        "Built and shipped a GPU-accelerated speech-to-text dictation app for Windows using Python and OpenAI Whisper, published as a public beta on GitHub (57 commits, 2 releases)",
        "Developed system-wide hotkey integration, floating UI, statistics dashboard, and Windows installer with setup wizard",
        "Built a product landing page using React, TypeScript, Tailwind CSS, and Vercel with working beta signup flow and interactive demo",
        "Handled full product lifecycle: local ML inference, GPU optimization, UI design, installer packaging, license system, documentation, and beta distribution",
    ]:
        pdf.bullet(b)
    pdf.ln(2)

    pdf.project_title("Live Pilot - Voice-Controlled AI DAW Assistant", "(Functional Prototype)")
    for b in [
        "Built a voice-controlled AI assistant for Ableton Live using Python, Google Gemini API, and OSC protocol with a 6-agent architecture and 62 tool functions",
        "Designed a deterministic pipeline replacing iterative LLM loops, reducing API calls per operation from 30+ to 1",
    ]:
        pdf.bullet(b)
    pdf.ln(3)

    pdf.section_header("EDUCATION")
    pdf.edu_entry("Miami University - Cincinnati, OH", "Business Management Technology coursework - 67 credit hours toward Associate of Applied Business", "Attended through Spring 2024", "Database Design & Development, Business Management, Small Business Operations")
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, pdf._c("Google IT Support Certification - Coursera, November 2022"), new_x="LMARGIN", new_y="NEXT")

    out = os.path.join(BASE, "Total_Expert_PS", "Resume_TotalExpert_PS.pdf")
    pdf.output(out)
    print(f"Total Expert PDF: {out}")


if __name__ == "__main__":
    build_plaid()
    build_turvo()
    build_total_expert()
    print("\nAll PDFs generated.")
