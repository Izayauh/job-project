# Phase 4: Live Target List & Application-Ready Materials

**Status:** LOCKED (2026-03-12)
**Goal:** Calibration batch — learn which role types and company profiles respond best. Not volume.

---

## Step 1: You Source 8 Raw Roles (You, ~1-2 hours)

### Search Platforms (in order)
1. **LinkedIn Jobs** — filter by role title + Austin, TX + Remote + $50K-$90K
2. **Built In Austin** — strong for tech companies that value product fluency
3. **Wellfound (AngelList)** — startups where builder mindset is a selling point
4. **Otta** — curated tech roles, good for SE/CSE
5. **Indeed** — broader net, useful for Implementation/CS roles

### Search Queries

| Priority | Query | Location Filter | Target Count |
|----------|-------|----------------|--------------|
| 1 | "Solutions Engineer" | Austin, TX + Remote | 4 roles |
| 2 | "Implementation Engineer" OR "Implementation Specialist" OR "Customer Success Engineer" | Austin, TX + Remote | 2 roles |
| 3 | "Technical Support Engineer" (filter for ones mentioning troubleshooting, technical breadth, customer communication) | Austin, TX + Remote | 2 roles |

### For Each Role, Capture
- Company name
- Exact job title
- Location (on-site / hybrid / remote)
- Job posting URL
- Salary if listed
- 2-3 lines from the job description that stood out (requirements, responsibilities, tools mentioned)

### Quick Disqualify Filters (skip immediately)
- Requires 5+ years in a named enterprise platform (Salesforce, ServiceNow, etc.)
- Requires deep pre-sales / quota-carrying experience
- Requires specific certifications you don't have (AWS SA, CCNA, etc.)
- Enterprise-only focus (Fortune 500 sales cycles, $500K+ deals)
- Requires a completed degree (not "or equivalent experience")
- Company is rigidly pedigree-filtering (top-tier degree requirements, big-name employer expectations)

---

## Step 2: I Analyze and Score the List (Me, after you provide raw data)

Once you paste or provide the raw list, I produce for each role:

### Scoring Criteria

**Fit score (1-10)** based on:
- Skill overlap with verified Skills_Bank
- Whether "nice to haves" align with your projects
- Role seniority match (avoiding roles that clearly want 7+ years)
- Geographic / compensation alignment
- Whether your projects are meaningful differentiators for this company's product

### Targeting Bias (applied to scoring)

**Boost factors:**
- Companies under 500 employees
- Startups or growth-stage companies
- Roles where "builder mindset," "technical curiosity," or "product fluency" appear in description
- Roles where your projects directly relate to their product domain
- Companies where technical communication matters more than tool checklists

**Penalty factors:**
- Rigid enterprise roles with heavy credential / platform requirements
- Roles with pedigree filtering (specific degree, specific employer background)
- Companies over 1,000 employees with formal hiring processes that hard-filter on credentials
- Roles requiring enterprise sales motion experience
- Roles requiring specific platforms you cannot truthfully claim

### Output Per Role
- Fit score (1-10)
- Which resume version to use (SE / TSE / Impl-CS)
- Why it fits — specific mapping to your verified experience
- Risk factors — where a recruiter might hesitate
- Verdict: **Apply Now** / **Apply Later** (after prep) / **Skip**

### Ranking
All 8 roles ranked from strongest to weakest fit.

---

## Step 3: I Select and Prepare the Top 3-5 (Me)

From the ranked list, recommend the best **3 to 5** roles to apply to immediately. Do not force 5 if only 3 are genuinely strong.

### A. Resume Tailoring (per selected role)
- Select the correct base template (SE / TSE / Impl-CS)
- Write a tailored summary line that mirrors the company's language
- Identify 3-5 company-specific emphasis points (reorder bullets, swap Tier 2 bullets in/out)
- Flag any bullet swaps or reordering suggestions
- All changes stay within approved bullets from `Resume_Tailoring_Base.md`

### B. Cover Letter Decision (per selected role)
Recommend cover letter **only** when:
- The application portal has a cover letter upload field
- The company is < 200 employees (more likely a human reads it)
- You have a clear "why this company" angle beyond "I need a job"
- The role description mentions values/culture that genuinely align

If yes, draft using approved claims only.

### C. Application Package Output (per selected role)
Each selected role gets a folder under `04_Applications/[Company_Name]/`:
- `Resume_[Company]_[Role].md` — tailored version
- `Cover_Letter_[Company].md` — if applicable
- `Application_Notes.md` — fit score, emphasis points, risk factors, follow-up notes
- Update `06_Tracking/Job_Tracker.csv` with new entries

---

## Step 4: Pre-Application Checklist (Joint)

Before submitting each application:

- [ ] Export each final reviewed resume to a clean recruiter-safe PDF format before submission
- [ ] Portfolio links tested (Impulse GitHub + website both load)
- [ ] Impulse website footer resolved (see Blocker #1 below)
- [ ] Summary line feels natural for this specific role
- [ ] No claims outside the approved bullets list
- [ ] Job Tracker updated with date, source, status
- [ ] If cover letter included — proofread, company name correct, no template placeholders

---

## Step 5: Post-Batch Follow-Up & Calibration (Joint)

After the calibration batch is submitted:

- Set follow-up dates (7-10 days post-application) in the tracker
- Prepare follow-up outreach using `Outreach_Templates.md` template #4
- **Calibration review after 2 weeks:**
  - Which role types got responses?
  - Which company profiles engaged?
  - Were there patterns in rejections (experience gap, missing tool, seniority)?
  - Adjust targeting bias, resume emphasis, and batch size for the next round
- Queue remaining roles from the 8 for next batch if appropriate
- Note upskilling targets if consistent gaps appear

---

## Dependencies / Blockers

| # | Blocker | Status | Impact | Resolution |
|---|---------|--------|--------|------------|
| 1 | **Impulse website footer says "Impulse AI Inc."** | MUST FIX BEFORE ANY APPLICATION | Recruiter visiting the site sees a fake company name — credibility risk | Confirm whether Impulse AI Inc. is a real incorporated entity. If not, change footer to something neutral (e.g., "Impulse" or "Isaiah Washington") |
| 2 | Cover letter template not built | Not started | Needed if any top role warrants one | Build during Step 3 if needed |
| 3 | STAR Stories #1, #5, #6, #7 are skeletons | Needs your input | Not blocking applications, blocks interview prep | Fill in before any interviews land |
| 4 | Resume PDF export workflow | Untested | Must verify .md to clean PDF pipeline | Test before first submission |

---

## Execution Timeline

| Day | Action | Owner |
|-----|--------|-------|
| Day 1 | **Fix Impulse footer if not a real entity** | You |
| Day 1 | Source 8 raw roles using search queries above | You |
| Day 1 | Paste raw list into conversation | You |
| Day 1-2 | Score, rank, select top 3-5, generate tailored materials | Me |
| Day 2 | Review tailored materials, flag anything off | You |
| Day 2 | Test PDF export pipeline | You |
| Day 2-3 | Export final PDFs, submit calibration batch | You |
| Day 3 | Update Job_Tracker, set follow-up reminders | Joint |
| Day 10-14 | Send follow-up messages for unanswered applications | You |
| Day 14+ | Calibration review — analyze response patterns, adjust for next batch | Joint |

---

## Constraints (carried from system rules)

- Use only truthful claims
- Do not auto-apply
- Do not generate fake tool experience
- Optimize for credibility and interview potential, not volume
- Highlight where projects meaningfully strengthen fit
- All resume modifications must pass against `Resume_Tailoring_Base.md` "Items to Avoid Claiming"
