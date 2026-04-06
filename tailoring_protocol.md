# Tailoring Protocol

This protocol defines the exact, unalterable human-in-the-loop workflow for tailoring resumes to new job descriptions. It ensures alignment and high conversion without drifting into fluff or overclaiming.

## Step 1: Classify the Job
Before writing anything, classify the job description into one of three buckets:
1. **TSE (Technical Support Engineer):** Focuses heavily on tickets, troubleshooting, SLA management, and device/infrastructure triage.
2. **SE/Implementation Bridge:** Requires customer communication but explicitly demands software configuration, API literacy, systems integration, and script execution.
3. **Reject / Weak Fit:** A role requiring heavy established B2B sales cycles, CCNA-level routing engineering, or strict immediate on-site presence in a non-target city. *Action: Drop the job. Move on.*

## Step 2: Extract Requirements
Deconstruct the JD into:
* **Hard Requirements:** Years of experience, degree mandates, specific languages/frameworks.
* **Soft Requirements:** Communication, "cross-functional collaboration".
* **Emphasis:** Support vs. Implementation vs. Engineering.
* **Customer Facing:** Is the end-user internal IT or external clients?
* **Tool Keywords:** Connectwise, Jira, Zendesk, Salesforce, AWS, Python, APIs.

## Step 3: Compare Against the Claims Firewall
Match the extracted requirements directly against the `resume_claims_firewall.md`.
* **Direct Match:** The requirement maps perfectly to an approved claim. (e.g., Python -> Live Pilot; Triage -> Nexus WiFi).
* **Partial Match:** The requirement is related. (e.g., "Network Troubleshooting" -> "Access point, switch, gateway triage").
* **Unsupported:** The requirement is absent from the candidate profile (e.g., Kubernetes, Azure Active Directory). *Rule: Do not add it to the resume.*

## Step 4: Choose the Correct Master Resume
Based on Step 1, select the foundational document:
* For TSE: Start with the TSE Master Resume. (Experience leads).
* For SE/Implementation: Start with the SE Master Resume. (Projects lead).

## Step 5: Allowable Tailoring Areas
Do not generate a completely new document. Only touch these specific levers:
1. **Summary:** Minor tweaks to the final sentence to reflect the exact job title being prioritized.
2. **Skills Ordering:** Shift the most relevant tool keywords to the front of the list, provided they are already possessed.
3. **Bullet Ordering:** If the job emphasizes hardware triage, slide the hardware bullet to the top of the Nexus WiFi section.
4. **Project Emphasis:** For audio-tech or AI companies, emphasize Live Pilot. For application packaging or UI companies, emphasize Impulse.
5. **Limited Keyword Substitutions:** If the job asks for "Issue Resolution" instead of "Issue Triage", swap the term. *Do not swap "React" for "Angular" if Angular is unknown.*

## Step 6: Anti-Overclaim Checks
Execute this checklist before final validation:
* [ ] **Degree Inflation:** Does it still strictly say "completed 67 credit hours"?
* [ ] **Title Inflation:** Does the experience still say "Network Support Technician"?
* [ ] **Unsupported Metrics:** Are all percentages/numbers only the ones explicitly verified (1,500 hours, 150+ properties, 30+ to 1)?
* [ ] **Enterprise-Experience Inflation:** Have the projects remained separated from the true corporate experience?
* [ ] **Summary Fluff:** Are there any empty adjectives? (e.g., "Passionate", "Results-oriented", "Synergistic").
* [ ] **Keyword Stuffing:** Are there listed technical skills with zero context points in the bullets?

## Step 7: Produce Final Output
For the user review step, produce exactly:
1. **Tailored Resume:** The plain text output.
2. **Short Change Log:** E.g., "Moved Live Pilot bullet to top; changed 'customer-facing' to 'client-facing'."
3. **Risk Notes:** E.g., "JD asked for SaaS B2B experience. This is missing and cannot be faked. Expect friction."
4. **Interview Watchouts:** E.g., "They use Zendesk. You use an in-house tool. Be prepared to explain how your workflow maps to Zendesk."

### Hard Rules:
* If a job can only be won by pretending Isaiah has done work he has not done, reject the role.
* Do not invent metrics.
* Do not use job descriptions from the open web unless they are supplied or saved in the repo.
* If no real JD is provided, tailor only at the lane level.
