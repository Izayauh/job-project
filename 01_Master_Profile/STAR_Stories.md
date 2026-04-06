# STAR Stories Bank

Updated: 2026-03-11 (Phase 2.1 — user-verified clarifications applied)
Status: Stories #2-4 grounded in confirmed facts. Stories #1, #5-7 still need user input.

---

## How to Use

Each story follows the STAR format:
- **Situation:** Context and background
- **Task:** What you needed to accomplish
- **Action:** What you specifically did
- **Result:** The outcome, ideally with a metric

---

## Story 1: Remote Infrastructure Triage (Nexus WiFi)

**Tags:** troubleshooting, customer-facing, remote support, equipment triage
**Best for:** Tech Support Eng, Solutions Eng interviews

- **Situation:** A customer contacts support reporting that their internet is down at a managed property.
- **Task:** Determine whether the issue is isolated to one device or affects the entire location, identify the root cause, and resolve or escalate appropriately.
- **Action:** Clarify the issue with the customer. Confirm scope (single device vs. whole location). Check for downed infrastructure — access points, switches, gateways, modems. Walk through basic troubleshooting steps. Reference the internal ticketing system for similar past issues. If the issue is outside scope (e.g., failed hardware needing field replacement), escalate with full context.
- **Result:** [NEEDS INPUT — can you recall a specific example? Even a general one: "Identified a failed switch affecting an entire property, escalated with documentation, hardware was replaced within X days"?]

**Note:** This story framework is ready. One real example would complete it.

---

## Story 2: Building the Inventory System (Midway Auto Group)

**Tags:** system building, process improvement, operations
**Best for:** Implementation Specialist, Solutions Eng interviews

- **Situation:** Midway Auto Group needed a way to track motor vehicle inventory — what was in stock, what it cost, delivery status, and usage — but didn't have a structured system in place.
- **Task:** Create and maintain a tracking system that gave the team visibility into the full inventory.
- **Action:** Built a spreadsheet-based inventory tracking system covering cost, deliveries, and usage across the dealership's full vehicle stock. Maintained and updated it over a 4+ year period.
- **Result:** The system improved visibility and organization across dealership operations during a period of significant business growth.

**Interview framing:** Don't claim the system caused sales growth. Frame it as: "I identified an operational gap, built a practical solution with the tools available, and maintained it reliably for years. It gave the team better visibility during a period when the business was scaling."

---

## Story 3: Building Live Pilot (Functional Prototype)

**Tags:** AI, automation, system design, initiative, problem-solving
**Best for:** Solutions Eng, Implementation Eng interviews

- **Situation:** Music production workflows in Ableton Live required repetitive manual steps — loading plugins, configuring device chains, adjusting parameters — that broke creative flow.
- **Task:** Build a tool that could control the DAW through voice commands, reducing manual interaction during sessions.
- **Action:** Designed and built Live Pilot using Python, Google Gemini 2.5 Flash (with function calling and real-time audio streaming), and OSC protocol. Architected a 6-agent system with 62 tool functions. When the initial iterative LLM approach was too slow and expensive (30+ API calls per plugin chain), redesigned the architecture into a deterministic pipeline (PLAN → EXECUTE → VERIFY → REPORT) that reduced it to exactly 1 call. Added crash recovery, idempotent operations, a plugin knowledge base, and fallback resolution.
- **Result:** The system could execute chain-of-thought-driven commands and load plugin chains from a single voice instruction. API calls per operation dropped from 30+ to 1. The system handles crashes and unknown devices gracefully. Not fully complete across its full intended scope — it relied partly on preloaded information — but demonstrated real system design and architecture.

**Interview framing:** Be honest that it's a functional prototype, not a finished product. The impressive parts are the architecture decisions: the pipeline redesign, the agent system, the crash recovery. Lead with the problem-solving narrative: "I built something, it was too slow, so I redesigned it."

**Talking points:**
- "I identified a real bottleneck, built a working solution, then redesigned the architecture when the first approach didn't scale."
- "Going from O(n) LLM calls to O(1) required rethinking the entire execution model."
- "It's a functional prototype — not fully production-complete — but the architecture and the pipeline design are the real technical substance."

---

## Story 4: Building Impulse / WhisperLocal (Fully Built App)

**Tags:** product development, ML pipeline, GPU optimization, privacy, full lifecycle
**Best for:** Solutions Eng, Implementation Eng, any role valuing initiative

- **Situation:** Cloud-based speech-to-text tools send audio to external servers, raising privacy concerns. Existing local alternatives were developer-focused and hard to use for regular users.
- **Task:** Build a privacy-first dictation app that runs entirely locally, is fast enough for real-time use, and is accessible to non-technical users.
- **Action:** Built Impulse — a system-wide Windows dictation app using Python and OpenAI Whisper with NVIDIA CUDA GPU acceleration. Implemented smart model selection (auto-picks from tiny to large-v3 based on dictation length), floating UI with statistics dashboard, global hotkeys (WIN+CTRL), latch mode for hands-free use, custom dictionary system, and first-run setup wizard. Packaged into a Windows installer (~3.5 GB) with license key validation. Published a beta release on GitHub with user guide, privacy policy, changelog, and testing checklist. Went through 3 structured development phases.
- **Result:** Fully built application (1.0.0-beta.1) processing speech-to-text entirely on the user's machine. Public GitHub repo with 57 commits and 2 releases. Has edge-case instability and is not actively maintained currently, but represents a complete product development cycle.

**Interview framing:** This is the strongest "I shipped something" story. Be upfront that it's a beta with known edge cases. The point isn't that it's perfect — it's that you handled the full lifecycle: requirement → design → build → test → package → distribute → document.

**Talking points:**
- "I went from an idea to a packaged installer with a license system and public beta."
- "GPU acceleration was necessary because CPU-only Whisper is too slow for real-time dictation."
- "The product development skills — packaging, documentation, user-facing design — are as relevant as the ML pipeline."

---

## Story 5: Cross-Team Communication at Cincinnati Insurance

**Tags:** cross-functional, communication, data accuracy
**Best for:** Customer Success, Implementation interviews

- **Situation:** Key insured accounts required accurate policy data input coordinated between multiple teams.
- **Task:** Manage data input while communicating effectively with underwriters and assistants.
- **Action:** [NEEDS INPUT — how did you ensure accuracy? Any catches or process improvements?]
- **Result:** [NEEDS INPUT — what was the quality/accuracy outcome?]

---

## Story 6: Handling a Difficult Customer (Nexus WiFi)

**Tags:** customer escalation, de-escalation, problem solving
**Best for:** Any customer-facing interview

- **Situation:** [NEEDS INPUT — describe a frustrated or difficult customer scenario]
- **Task:** [What did you need to resolve?]
- **Action:** [How did you handle the communication and the technical issue?]
- **Result:** [Outcome?]

---

## Story 7: Managing Ticket Workflow (Nexus WiFi)

**Tags:** operations, prioritization, time management
**Best for:** Support Eng, IT roles

- **Situation:** Supporting 150+ properties remotely with a mix of incoming tickets, ongoing issues, and outbound follow-up calls across shifting schedules (morning and night shifts).
- **Task:** Keep ticket workflows efficient and ensure nothing falls through cracks.
- **Action:** [NEEDS INPUT — how do you prioritize between new incoming tickets and ongoing ones? Do you batch outbound calls? How do you decide what to escalate vs. keep working on?]
- **Result:** Resolve an estimated 5–10 tickets per morning shift and 2–5 per night shift, plus outbound calling and status updates.

---

## Stories Still Needed

- [ ] A specific equipment failure triage win (e.g., identified a failed AP/switch, escalated, resolved)
- [ ] A time you improved a process or workflow at Nexus or Midway
- [ ] A time you had to learn something new quickly (Google IT cert? Python? A new tool at work?)
- [ ] A time you disagreed with a teammate and how you resolved it
- [ ] A failure or mistake and what you learned

**Removed from list:** "A specific DNS/DHCP/VPN troubleshooting win" — per user input, not enough specific recall for protocol-level stories. Replaced with equipment triage framing.
