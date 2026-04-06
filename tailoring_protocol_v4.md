# Tailoring Protocol v4

This protocol dictates the strict operational sequence for evaluating and tailoring a master resume to a specific job description. This workflow bridges internal truth constraints with standard structural priorities.

## Step 1: Classify the Job
Assess the target job description and categorize it strictly into one of three lanes:
- **TSE (Technical Support Engineer):** Focuses on tickets, hardware, troubleshooting, SLA management, and infrastructure triage.
- **SE / Implementation Bridge:** Demands software configuration, API literacy, systems integration, customer communication, and script execution.
- **Reject / Weak Fit:** A role requiring heavy established B2B sales cycles, CCNA-level routing engineering, strict immediate on-site presence out of state, or >5 years of formal Software Engineering.

## Step 2: Extract Requirements
Deconstruct the JD into distinct analytical categories:
- **Hard Requirements:** Specific languages, frameworks, or certifications.
- **Soft Requirements:** Communication, teamwork, problem-solving.
- **Exact Tools / Tech:** e.g., Azure AD, AWS, Connectwise, Jira, Python.
- **Customer-Facing Expectations:** Internal IT support vs. External client communication.
- **Constraints:** Degree dependencies, firm location limits, exact years-of-experience floors.

## Step 3: Map Each Requirement to Evidence
Compare the extracted requirements directly against the candidate's verified profile constraints.
- **Direct Match:** Fits an approved claim perfectly (e.g., Python -> Live Pilot).
- **Partial Match:** Conceptually related but not identical (e.g., "Network Troubleshooting" -> Access point triage).
- **Unsupported:** Completely absent from the candidate profile. 
  - *Hard Rule:* If unsupported, do not add it to the resume. Log it exclusively in the "Risk Notes" or "Interview Watchouts" section.

## Step 4: Choose the Correct Master Resume
Based on the classification in Step 1, duplicate the relevant master foundation to use as your base text.
- For TSE: Target `resume_rebuild_v4.md` (TSE lane).
- For SE / Implementation Bridge: Target `resume_rebuild_v4.md` (SE lane).

## Step 5: Tailor Exclusively Within Allowed Areas
Do not generate a completely new document. Only manipulate these specific structural levers:
- **Summary:** Tweak the final or core sentences to specify the most relevant experience for the target role.
- **Skills Ordering:** Position the most relevant possessed skills or keywords earlier in their respective lists.
- **Bullet Ordering:** Retain the most impactful scope bullet at the top. For subsequent bullets, integrate specific job description requirements into the context of the work performed.
- **Project Emphasis:** Emphasize the specific tool logic in Live Pilot or Impulse that most closely mirrors the JD stack.
- **Exact Keyword Substitutions:** You may swap generalized words for the exact keywords required by the JD, provided they remain entirely truthful and contextually accurate.

## Step 6: Run Final Output Checks
Before confirming any output, clear these quality-control checks:
- [ ] **Header Check:** Ensure standard headers are used (Summary, Skills, Experience, Projects, Education) in established order.
- [ ] **Unsupported Tool Check:** Confirm no software or platforms were added without source backing.
- [ ] **Degree Check:** Confirm it explicitly reads "coursework" and "credit hours" without stating graduation.
- [ ] **Title Check:** Verify current formal title reads "Network Support Technician". 
- [ ] **Workflow Truth Check:** Did numerical metrics substitute real workflow descriptions inappropriately?
- [ ] **Context Integration Check:** Do tools appear organically in action statements, rather than randomly thrown into a bullet?
- [ ] **Directness Check:** Are bullets direct and free of abstract praise?

## Step 7: Produce Output
Generate exactly the following response package for user review:
1. **Tailored Resume:** The plain-text document.
2. **Short Change Log:** A brief summary defining exactly what was moved or adjusted.
3. **Risk Notes:** Highlighting explicitly unmapped requirements the candidate cannot satisfy.
4. **Interview Watchouts:** Strategic notes on how to defend the partial matches and missing enterprise experience.
