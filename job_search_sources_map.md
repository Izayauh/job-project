# Job Search Source Map

This file is the source map for the job-search project. Its purpose is to show an AI system where the main job-search assets live, what each asset is used for, and how the system should treat them.

## Project Purpose

Use these linked documents as the primary source materials for the job-search system.

The AI should:
- read from these files first before creating new materials
- treat them as current working sources unless replaced by newer versions
- update derived materials based on these sources
- avoid inventing information not supported by these sources

---

## Primary Source Files

### 1. Job Search / “Getting a Job” Sheet
**Type:** Google Sheets  
**Purpose:** Main spreadsheet for job-search planning, tracking, references, or related structured information.  
**Link:** https://docs.google.com/spreadsheets/d/1DaOyWsBWNrkdC7DTQXemYx-A0TPGORgFlbQO-CRdvWw/edit?usp=drive_web&ouid=105893028104110312312

**How AI should use it:**
- inspect sheet tabs and identify what each tab contains
- extract structured data such as references, trackers, contacts, or application notes
- use it as a source of truth for table-based job-search information
- update downstream outputs based on its contents

**Likely update use cases:**
- references database updates
- application tracker updates
- outreach tracking
- follow-up tracking

---

### 2. Resume
**Type:** Google Doc  
**Purpose:** Current working resume.  
**Link:** https://docs.google.com/document/d/1jTr_fULk6Y3w0FRn8J-Ncii-xx2DN5l99X2eJj19leE/edit?usp=drive_link

**How AI should use it:**
- treat this as the current base resume
- extract work history, skills, projects, and existing phrasing
- build modular bullet banks from truthful content only
- create tailored resume variants from this source without fabricating details

**Likely update use cases:**
- master resume refinement
- tailored resume generation
- summary/profile extraction
- bullet bank creation
- interview prep story extraction

---

### 3. College Transcript
**Type:** Google Drive link  
**Purpose:** Education verification / academic history source.  
**Link provided:** https://drive.google.com/drive/home?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto

**Important note:**
This link appears to point to Google Drive home, not to a specific transcript file. An AI system may not be able to locate the transcript reliably from this link alone.

**How AI should use it:**
- do not assume this link directly opens the transcript
- use it only as a placeholder until a direct file link is provided
- once a direct transcript file is available, extract school name, dates, degree/coursework if relevant, and academic details that belong in job materials

**Likely update use cases once the direct file is available:**
- education section verification
- background fact-checking
- application form completion

---

## Recommended Handling Rules

The AI system should follow these rules when working with these files:

1. Use the resume as the main source of candidate background.
2. Use the Google Sheet as the main structured operations layer.
3. Do not invent details not supported by the source documents.
4. Treat the transcript link as incomplete until a direct transcript file is supplied.
5. Any new outputs should be stored as derived artifacts, not as replacements for the originals unless explicitly approved.

---

## Suggested Derived Files the AI Can Create

Based on the sources above, the AI can create and maintain:
- `Master_Candidate_Profile.md`
- `Resume_Bullet_Bank.md`
- `References_Database.csv`
- `Job_Tracker.csv`
- `Outreach_Templates.md`
- `Interview_Prep_Bank.md`
- `Application_Packets/` folder by company

---

## Source Priority

When there is a conflict or ambiguity, use this priority order:

1. Current Resume Google Doc
2. Job Search Google Sheet
3. Direct transcript file (once supplied)
4. Older derived files

---

## Needed Improvement

To make this system fully reliable, replace the current transcript link with a **direct file link** to the transcript document or PDF.

