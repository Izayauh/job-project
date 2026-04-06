# Resume Build Process — Mandatory Workflow

Updated: 2026-03-28
Status: LOCKED — do not skip steps

---

## Hard Rules

1. **NEVER build a resume without the full job description.** Summaries, bullet points, and paraphrased JDs are not acceptable. The complete JD text must be provided and saved before any resume work begins.

2. **Every resume must be scored before delivery.** Run `match_report.py` against the resume and JD. Target: 90+ before showing to user. Iterate until score is met.

3. **Keywords must be matched verbatim.** If the JD says "coding," use "coding" — not "programming." If the JD says "customer-centric," use that exact phrase. Do not paraphrase JD keywords.

4. **The exact job title must appear in the Professional Summary.** This is a searchability requirement. If the title is "Technical Support Engineer," those exact words must be in the summary.

5. **All truthfulness rules still apply.** ATS optimization does not override Resume_Tailoring_Base.md rules. Do not claim tools, skills, or experience that aren't real. See `01_Master_Profile/Resume_Tailoring_Base.md` "Items to Avoid Claiming" section.

---

## Step-by-Step Process

### Step 1: Collect & Save JD
- Get the **complete** job description text from the user
- Save it as `JD_[Company]_[Role].txt` in the application folder
- Create the application folder: `04_Applications/[Company]/`

### Step 2: Extract Keywords
- Run keyword extraction on the JD
- Build a keyword map with three categories:
  - **Hard Skills:** technical terms, tools, languages, platforms
  - **Soft Skills:** interpersonal, work-style, communication terms
  - **Job Title:** exact title for summary inclusion
- Save the keyword map in Application_Notes.md

### Step 3: Select Base Template
- Choose from `02_Templates/Resume_Templates/`:
  - `Resume_Solutions_Engineer.md` — for SE, builder-first roles
  - `Resume_Technical_Support_Engineer.md` — for TSE, support-first roles
  - `Resume_Implementation_CustomerSuccess.md` — for impl, CS, onboarding roles
  - `Resume_AI_Content_Evaluator.md` — for AI training, annotation roles
- Or create a new variant if no template fits

### Step 4: Build Tailored Resume
- Start from the base template
- Weave in every JD keyword naturally:
  - Hard skills: in Skills section + relevant bullets
  - Soft skills: in Summary + experience bullets
  - Job title: in Summary, first sentence
- Follow the ATS optimization checklist (below)
- Target 800-1000 words

### Step 5: Score with Resume-Matcher
- Use the local **Resume-Matcher** AI tool to evaluate the drafted resume against the JD.
- Check overall score and contextual alignment (it provides deeper semantic matching than simple keyword scripts).
- Check for MISSING hard/soft skills via its keyword highlighting.
- Check for negative words and layout structure feedback.
- Iterate on the resume content until the Resume-Matcher score and AI suggestions are optimized.

### Step 6: Generate Outputs using RenderCV
- Format the tailored resume data into the `RenderCV` YAML schema.
- Save it as `Resume_[Company]_[Role].yaml` in the application's folder.
- Run `rendercv render Resume_[Company]_[Role].yaml` to generate a professional PDF.
- (This replaces legacy python-docx and fpdf2 scripts).

### Step 7: Deliver & Recommend Jobscan Verification
- Show PDF/DOCX to user
- Recommend user run through Jobscan for external verification
- Save final Jobscan score in Application_Notes.md

---

## ATS Optimization Checklist

Before finalizing any resume, verify:

- [ ] Job title appears in Professional Summary (exact match)
- [ ] All hard skills from JD appear at least once
- [ ] All soft skills from JD appear at least once
- [ ] No negative words (failures, downed, problems, without supervision, etc.)
- [ ] Word count is 800-1000
- [ ] Section headers are standard: "Professional Summary", "Experience", "Education", "Technical Skills"
- [ ] Dates are properly formatted (Mon YYYY - Mon YYYY)
- [ ] Contact info includes location, email, phone
- [ ] File format is PDF (preferred) or DOCX
- [ ] File name is clean, no special characters

## Negative Words to Avoid

Replace these with positive alternatives:
| Negative | Use Instead |
|----------|-------------|
| failures | challenges |
| downed | disrupted |
| problems | opportunities, challenges |
| urgent | high-priority |
| issues (when describing negatives) | requests, topics, challenges |
| without supervision | independently, as a self-starter |
| recurring issues | recurring patterns |
| debugging | analyzing, investigating, resolving |
| error/errors | keep only when describing specific technical debugging |
| crisis | keep only if JD uses it |

---

## File Naming Convention

```
04_Applications/
  [Company]/
    JD_[Company]_[Role].txt          — saved job description
    Resume_[Company]_[Role].md       — resume source
    Resume_[Company]_[Role].pdf      — PDF output
    Resume_[Company]_[Role].docx     — DOCX output
    CoverLetter_[Company]_[Role].md  — cover letter (if needed)
    Application_Notes.md             — fit assessment, keyword map, scores
    Match_Report_[Company].txt       — match report output
```
