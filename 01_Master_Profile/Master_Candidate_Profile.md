# Master Candidate Profile

Generated: 2026-03-11 | Updated: 2026-03-11 (Phase 2.1 — user-verified clarifications applied)
Source: Resume PDFs, LinkedIn Profile, Transcript, Project READMEs, direct user input
Status: VERIFIED — education, work history, and projects grounded in user-confirmed facts

---

## Contact

| Field | Value |
|-------|-------|
| Name | Isaiah Washington |
| Phone | 513.544.9022 |
| Email | isaiahwashington48@gmail.com |
| LinkedIn | www.linkedin.com/in/isaiah-washington48 |
| Current Location | Hamilton / Cincinnati, OH area |
| Target Location | **Austin, TX** (priority market, relocation contingent on right opportunity, ~2 month start window), Remote |

---

## Target Role

| Field | Value |
|-------|-------|
| Primary targets | Solutions Engineer, Technical Support Engineer, Implementation Specialist |
| Secondary targets | Customer Success Engineer, Junior Systems/Network/IT roles, Technical Account Manager |
| Salary target | $50,000–$70,000+ |
| Work arrangement | Remote preferred, hybrid acceptable |
| Geographic focus | Austin, TX (primary); remote (secondary) |

---

## Professional Summary (Current)

Solutions-focused technical professional with experience in network support, remote troubleshooting, and infrastructure operations. Proven ability to resolve customer-impacting issues, collaborate across teams, and improve technical workflows in fast-paced environments. Built AI-enabled tools, including a voice-controlled DAW assistant (Live Pilot) and a local speech-to-text pipeline (WhisperLocal). Seeking a remote/hybrid Solutions Engineering, Implementation, or Technical Support Engineer role.

---

## Work History

### 1. Nexus WiFi — Network Support Technician
**Oct 2021 – Present** | West Chester, OH (100% Remote)

**Role framing:** Foundational-to-intermediate technical support. Customer-facing troubleshooting, infrastructure/device issue triage, support workflow execution, escalation awareness, operational reliability. Do not inflate into senior networking or systems engineering.

**User-verified scope:**
- Provide remote technical support across 150+ managed properties
- 1,500+ hours of 100% remote customer-facing support
- Common issue categories: downed devices/infrastructure (APs, switches, gateways, modems), internet/connection outages, specific device connection issues, general support questions
- Diagnostic flow: clarify issue → confirm scope (single device vs. whole location) → check for downed devices or service issues → walk through troubleshooting steps → check ticketing system for similar past issues → escalate when outside scope
- Technical exposure includes camera setup/implementation, troubleshooting dead or failing equipment, coordinating hardware replacement (switches, APs), basic DHCP server verification
- Ticketing: in-house internal platform operated through company website
- Volume: ~2-5 resolved tickets per night shift, ~5-10 per morning shift plus outbound calling and ticket updates (rough estimates, do not overstate)

**What NOT to claim:**
- Do not write protocol-level troubleshooting stories (DNS, VPN deep-dives, etc.) — not enough specific recall
- Do not frame as advanced network engineering
- Do not imply SLA metrics or formal monitoring tools unless confirmed later

### 2. The Cincinnati Insurance Company — Key Accounts Team Assistant
**Feb 2023 – Aug 2023** | Fairfield, OH

**Verified facts:**
- Managed data input on key insured account policies per company guidelines
- Communicated with underwriters and underwriter assistants for accurate policy data input

**Audit notes:**
- REMOVED: "Implemented company policies, technical procedures, and standards for data security" — duplicate filler bullet (same as Nexus WiFi and Midway Auto)
- WEAK: Remaining bullets describe duties, not impact. No volume metrics, no accuracy improvements, no process contributions.
- SHORT TENURE: 6 months. Keep on resume but don't lead with it.

### 3. Midway Auto Group — Administrative Assistant
**Jan 2019 – Dec 2023** | Middletown, OH

**User-verified facts:**
- Built and maintained a spreadsheet-based inventory tracking system covering cost, deliveries, and usage across the dealership's full vehicle stock
- Improved visibility and organization across dealership operations during a period of business growth
- Assisted walk-in clients, scheduled appointments, answered phone lines

**Framing rule:** Do not imply that the inventory system directly caused a 200% sales increase. The business grew during this period; the system supported operational visibility. Keep attribution honest.

### 4. Texas Roadhouse — Server
**Oct 2019 – Mar 2020** | Hamilton, OH

- Ensured optimal guest experience through order management and table service
- Greeted and served beverages within 5 minutes per company standards
- Completed 6+ hour Ohio Alcohol Seller Server training

---

## Education

### Miami University — Hamilton/Oxford, OH
**Approved wording for all applications:**
> Miami University — Business Management Technology coursework
> Completed 67 credit hours toward Associate of Applied Business
> Attended through Spring 2024

- **College:** College of Liberal Arts & Applied Science
- **Transfer credits:** 28 hours from Cincinnati State Technical CC

**Relevant coursework (strong grades only — use selectively):**
- Database Design & Development (B-)
- HTML/CSS/JavaScript (Transfer)
- Statistics (B-)
- Workplace Writing (B)
- Mgt-Small Business Operations (A)
- Introduction to Management I (A)
- Computers and Business (A)
- Introduction to Marketing (B+)
- Introduction to Business Law (A)

**Full transcript details (internal reference only — do not include on resume):**
- Overall GPA: 2.67
- Courses with W or below C: Intro to Computer Concepts & Programming (W), Introduction to HCI (F), Tech/Ethics & Global Society (D+), Principles of Public Speaking (W)

### Google IT Support Certification — Coursera
- **Completed:** November 2022

### Hamilton High School
- **Graduated:** June 2015

---

## Education — Resolved
Previous resume versions used various incorrect degree names (Bachelor of Science in IT, BS in Business, Bachelor of Business Commerce, etc.). All have been replaced with the transcript-verified wording above. Do not use bachelor's degree language. Do not imply degree completion.

---

## Certifications

| Certification | Issuer | Date |
|---------------|--------|------|
| Google IT Support | Coursera | Nov 2022 |

---

## Projects

### Live Pilot — Voice-Controlled AI DAW Assistant (Functional Prototype)
**Repo:** github.com/Izayauh/LivePilot (public) - Local dev at C:\Users\isaia\Projects\music\live-pilot
**Stack:** Python, Google Gemini 2.5 Flash, OSC protocol, multi-agent architecture
**Status:** Functional prototype. Capable of executing chain-of-thought-driven commands and loading plugin chains. Not fully complete across the full intended scope. Relied partly on preloaded information and generalized plugin-setting behavior.

- Built a voice-controlled assistant for Ableton Live 11 using real-time audio streaming and AI function calling
- Designed a 6-agent architecture with 62 registered tool functions for DAW control
- Implemented a deterministic pipeline (PLAN → EXECUTE → VERIFY → REPORT) replacing iterative LLM loops, reducing API calls from 30+ per chain to exactly 1
- Built an OSC bridge for real-time communication between AI agents and Ableton Live
- Includes crash recovery, process lifecycle management, plugin chain builder with fallback resolution, and idempotent operations
- Has test suite, config management, desktop text chat UI, and WSL cross-environment support
- **Demonstrates:** system design, API integration, automation engineering, pipeline architecture
- **Portfolio rule:** Link publicly to the GitHub repository. Describe on resume as a project, not a product. Frame as functional prototype.

### Impulse (WhisperLocal) — Privacy-First Dictation App
**Repo:** github.com/Izayauh/whisper (public, 57 commits, 2 releases, clean README)
**Website:** impulse-eight-lake.vercel.app — VERIFIED PRESENTABLE
**App stack:** Python, OpenAI Whisper, NVIDIA CUDA, Windows system integration
**Website stack:** React 19, TypeScript, Tailwind CSS, Vite, Vercel (serverless functions, KV store), Resend (email), Motion (animations)
**Status:** Fully built application. Beta release (1.0.0-beta.1). Has edge-case instability and has not been actively maintained recently. Public repo is clean and professional. Website is polished and professional.

- Built a system-wide speech-to-text dictation application for Windows with 100% local processing
- Implemented GPU-accelerated transcription using NVIDIA CUDA and multiple Whisper model sizes (tiny through large-v3)
- Designed smart model selection that auto-picks optimal speed/quality balance based on dictation length
- Built floating bubble UI, statistics dashboard, hotkey system (WIN+CTRL), and latch mode for hands-free use
- Created Windows installer with setup wizard, first-run configuration, and license validation
- Published to GitHub as a beta product with user guide, privacy policy, changelog, and testing checklist
- Went through structured development phases (Phase 1-3 complete) with production-readiness milestones
- **Demonstrates:** product development lifecycle, GPU optimization, system-level integration, packaging/distribution, user experience design
- Website is a polished product landing page (React 19, TypeScript, Tailwind, Vercel) with working beta signup, interactive demo, feature cards, animations, and responsive design
- **Portfolio rule:** Link both the GitHub repo AND the website on resumes. Both are public and professional. The website is itself a portfolio piece demonstrating frontend development and product marketing skills. Note: app has edge-case instability — do not claim it as production-stable.
- **Open question:** Footer says "© 2026 Impulse AI Inc." — verify if this is a real entity or placeholder before recruiter conversations.

---

## Technical Skills

| Category | Skills | Evidence Level |
|----------|--------|----------------|
| Technical Support | Customer-facing troubleshooting, device/infrastructure triage (APs, switches, gateways, modems), equipment failure diagnosis, basic DHCP verification, camera setup/implementation | Verified — daily work at Nexus WiFi |
| Remote Support | Ticket-based workflow management, remote diagnostics, escalation awareness, outbound follow-up | Verified — 150+ properties, 1,500+ hours, in-house ticketing platform |
| Python | Application development, API integration, automation scripting | Verified — two substantial projects with source code |
| AI/ML Integration | Google Gemini API (function calling, real-time audio), OpenAI Whisper (local inference, multiple model sizes) | Verified — Live Pilot and Impulse |
| System Design | Multi-agent architecture, deterministic pipelines, crash recovery, idempotent operations | Verified — Live Pilot pipeline |
| Product Development | Windows installer packaging, license systems, UI design, beta release management | Verified — Impulse |
| GPU/Performance | NVIDIA CUDA acceleration, model selection optimization | Verified — Impulse GPU pipeline |
| Protocols | OSC (Open Sound Control) | Verified — Live Pilot OSC bridge |
| Frontend / Web | React, TypeScript, Tailwind CSS, Vite, Vercel deployment, serverless functions | Verified — Impulse product website |
| Tools | Git, GitHub, virtual environments, Windows/WSL cross-environment development | Verified — both projects |
| Business Software | Microsoft Office, Windows OS, Microsoft Teams, SQL (coursework) | Verified — work history |

**Skills to avoid claiming:**
- "Infrastructure monitoring and incident response" — no specific monitoring tools used
- "SLA-focused" — no SLA metrics available
- "Technical documentation" — no specific documentation artifacts confirmed
- Protocol-level network engineering (deep DNS/VPN/routing) — Nexus WiFi was support-level triage, not engineering
- "REST APIs" — no confirmed REST API work beyond project context

---

## Interpersonal / Soft Skills

- Customer-facing technical communication
- Cross-functional collaboration
- Technical documentation and workflow improvement
- Communication and interpretation
- Adaptability and problem solving
- Team coordination

---

## Strongest Selling Points

1. **4+ years of remote technical support** — real customer-facing experience triaging infrastructure and device issues across 150+ properties
2. **Built and shipped a real product** — Impulse is a fully built Windows dictation app with GPU acceleration, installer, license system, and a clean public GitHub repo (57 commits, 2 releases)
3. **Built a functional AI prototype with real architecture** — Live Pilot's 6-agent system, deterministic pipeline, and OSC integration show system design ability beyond tutorials
4. **1,500+ hours of remote customer-facing communication** — translating technical issues into clear guidance for non-technical users
5. **Self-directed builder** — Google IT cert, university coursework, and two substantial independent projects, all without formal engineering training

---

## Weaker Areas to Account For

1. **Degree not completed** — 67 credit hours toward Associate of Applied Business, withdrew Spring 2024. Frame as "coursework" not "degree."
2. **Limited formal SE/engineering title experience** — current title is Network Support Technician, not engineer. Projects help offset this but the title gap is real.
3. **Nexus WiFi is support-level, not engineering-level** — device triage, customer troubleshooting, escalation awareness. Don't overstate the technical depth.
4. **Live Pilot is a functional prototype** — it is now on a public repo but is a prototype rather than a finished commercial product
5. **Location transition** — currently in Cincinnati. Austin is contingent on the right opportunity. Can start within ~2 months. Also open to fully remote.

---

## Preferred Industries

- Technology / SaaS
- Infrastructure / Networking
- AI / Automation tooling
- Insurance / FinTech (has direct experience)
- Any company valuing technical support excellence
