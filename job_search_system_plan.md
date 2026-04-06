# Job Search System Plan

## Objective

Build a repeatable AI-assisted job search system that helps me move into a better tech role with less manual friction, better organization, and stronger consistency.

The system should reduce wasted time on repetitive application work so I can focus on:
- targeting the right jobs
- improving interview readiness
- strengthening my professional positioning
- staying consistent every week

This is not meant to be a fully autonomous black box. It should be a structured human-in-the-loop workflow that makes the process faster, cleaner, and more reliable.

## Primary Goal

Secure a better-paying tech job in the near term, ideally in the range of **$50,000–$70,000+**, with preference toward roles that match my real-world strengths and can act as a bridge into stronger future opportunities.

## Target Role Types

Prioritize roles that fit my current profile and can realistically convert with focused preparation:

1. **Solutions Engineer**
2. **Technical Support Engineer**
3. **Implementation Specialist**
4. **Customer Success Engineer**
5. **Junior Systems / Network / IT roles with growth potential**
6. **Technical Account / technical client-facing support roles**
7. **Entry-level or early-career software-adjacent technical roles**

The system should bias toward roles that value:
- troubleshooting
- technical communication
- customer-facing clarity
- systems thinking
- hands-on problem solving
- networking / infrastructure familiarity
- ability to learn quickly

## Geographic Focus

Primary focus:
- **Austin, Texas**

Secondary options:
- remote roles
- hybrid roles
- other cities only if opportunity quality is clearly strong

## Existing Assets

Current materials already available:
- a **projects folder**
- current **resume**
- **Google Docs** with relevant job-search material
- **Google Sheets** containing references

The system should treat these as the initial source of truth and organize around them instead of rebuilding everything from scratch.

## What the System Needs to Do

### 1. Centralize job search assets

Create a clean structure so all materials are easy to find, update, and reuse.

This includes:
- master resume
- tailored resume versions
- references sheet
- recruiter outreach templates
- cover letter / intro templates
- job tracker
- interview prep notes
- target company list
- accomplishments / project bullets bank

### 2. Create a usable source-of-truth workspace

The system should establish one main operating layer where all job-search activity is tracked.

This workspace should include:
- roles applied to
- company names
- job links
- date found
- date applied
- status
- referral / recruiter contact
- interview stage
- follow-up status
- notes
- tailored materials used

The system should make it obvious what needs action next.

### 3. Turn the resume into a modular asset

The resume should be broken into reusable sections so AI can tailor it intelligently without inventing fake experience.

This means building:
- master experience inventory
- bullet bank by skill
- role-specific summary variants
- skill clusters
- project descriptions
- customer-facing examples
- troubleshooting examples
- networking / infrastructure examples
- technical communication examples

The AI should only remix and prioritize truthful material.

### 4. Build reference management

The references need to be converted into a clean, usable database.

For each reference, the system should ideally track:
- full name
- role / relationship
- company
- email
- phone
- strength of relationship
- whether they agreed to be a reference
- what kind of roles they are best suited to support
- notes on context

The system should also generate:
- a reference outreach template
- a confirmation message template
- a “thank you” follow-up template

### 5. Build outreach support

The system should help create and manage:
- recruiter outreach messages
- LinkedIn-style short intros
- cold outreach templates
- referral requests
- follow-up messages

Templates should be customizable by:
- role type
- company
- recruiter name
- mutual context
- location
- why I’m a fit

### 6. Build application support

For each target job, the system should be able to:
- summarize the job posting
- extract core requirements
- compare requirements against my current background
- identify gaps
- suggest best-fitting resume version
- draft a tailored summary or cover note
- generate screening-question draft answers
- save everything into the tracker

The system should not spray generic applications blindly. It should help prioritize quality over random volume.

### 7. Build interview preparation workflow

The system should support prep for:
- recruiter screens
- technical support interviews
- behavioral interviews
- customer-facing scenario interviews
- solutions engineer style interviews
- troubleshooting / diagnostic questioning
- resume walkthroughs

It should generate:
- probable interview questions
- draft answer frameworks
- STAR story bank
- weak-point preparation
- company-specific prep notes
- role-specific prep notes

### 8. Create a weekly operating rhythm

The system should support consistency, not hype.

Suggested weekly structure:
- identify target roles
- tailor applications
- send outreach
- follow up on old applications
- prepare for interviews
- update resume / bullet bank based on feedback
- review pipeline health

The system should make it easy to see:
- how many strong applications were sent
- how many follow-ups are due
- whether the pipeline is drying up
- what needs improvement

## Recommended Folder / File Structure

```text
JobSearch/
  00_Source_Materials/
    Resume_Current/
    Google_Doc_Exports/
    References/
    Certifications_Projects/
  
  01_Master_Profile/
    Master_Resume.docx
    Experience_Inventory.md
    Skills_Bank.md
    Project_Bank.md
    STAR_Stories.md
    Professional_Summary_Variants.md

  02_Templates/
    Resume_Templates/
    Cover_Letter_Templates/
    Recruiter_Outreach/
    Referral_Requests/
    Thank_You_Notes/
    Screening_Answers/

  03_Targeting/
    Target_Roles.md
    Target_Companies.md
    Austin_Companies.md
    Remote_Companies.md

  04_Applications/
    Company_Name/
      Job_Description.txt
      Tailored_Resume.docx
      Tailored_Summary.md
      Cover_Letter.md
      Notes.md

  05_Interview_Prep/
    Common_Questions.md
    Behavioral_Stories.md
    Technical_Scenarios.md
    Company_Specific/

  06_Tracking/
    Job_Tracker.xlsx or .csv
    Follow_Up_Tracker.xlsx or .csv
    References_Database.xlsx or .csv

  07_Automation/
    prompts/
    scripts/
    workflow_notes.md
```

## Core Data Structures the AI System Should Build

### A. Master Candidate Profile

A structured document containing:
- role target
- location preferences
- salary range
- technical skills
- customer-facing skills
- work history
- project history
- strongest selling points
- weaker areas to account for
- preferred industries

### B. Resume Bullet Bank

Each bullet should be tagged by:
- skill type
- role relevance
- experience source
- customer-facing / technical / project / troubleshooting
- strength score

### C. Job Tracker

Suggested columns:
- company
- title
- location
- job link
- source
- date found
- date applied
- current stage
- status
- recruiter
- contact info
- tailored resume used
- follow-up due date
- notes
- salary if listed
- role fit score
- interest score

### D. Reference Database

Suggested columns:
- name
- relationship
- company
- title
- email
- phone
- confirmed yes/no
- best role type
- notes
- last contacted
- thank-you sent yes/no

### E. Outreach Template Library

Categories:
- recruiter first message
- recruiter follow-up
- referral ask
- post-application follow-up
- thank-you after interview
- reconnect message

## Functional Requirements for the AI System

The AI system should be able to do the following:

### Intake and organization
- scan the job search folder
- identify existing resumes, docs, sheets, and links
- classify files by purpose
- suggest a cleaned structure
- flag duplicates or outdated files

### Resume support
- parse resume content
- extract skills, accomplishments, and experience
- build a modular experience bank
- generate tailored resume drafts based on real content only

### Reference support
- ingest references from Google Sheets or exported files
- normalize formatting
- identify missing contact fields
- generate outreach drafts

### Job application support
- ingest job descriptions
- score role fit
- recommend whether to apply
- tailor materials
- log the application automatically

### Interview support
- generate likely questions
- create answer drafts from real experience
- track interview stage by company

### Pipeline management
- identify stale applications needing follow-up
- identify weak conversion areas
- surface next-best actions

## Constraints

The system must obey these rules:

1. **No fabricated experience**
2. **No fake metrics unless explicitly supplied**
3. **No fake credentials**
4. **No generic fluff if it weakens credibility**
5. **Bias toward roles I can plausibly win now**
6. **Preserve a human review step before sending anything**
7. **Keep all assets editable and transparent**
8. **Do not over-automate at the expense of accuracy**

## Success Criteria

The system is working if it produces:
- one organized source-of-truth job search workspace
- one cleaned master resume base
- one structured references database
- one usable job tracker
- one outreach template set
- one repeatable application workflow
- one interview prep workflow
- a clear next-action list at all times

Real-world success indicators:
- more consistent applications
- less friction per application
- better quality tailoring
- stronger follow-up discipline
- improved interview readiness
- more responses from relevant roles

## Immediate Build Order

### Phase 1 — Organize what already exists
- inspect current projects folder
- identify resume files, docs, links, sheets
- export or mirror critical info into a local structure
- build initial folder architecture
- create a master inventory of assets

### Phase 2 — Build source-of-truth docs
- create master candidate profile
- create resume bullet bank
- create references database
- create application tracker

### Phase 3 — Build reusable templates
- recruiter outreach templates
- referral ask templates
- tailored summary templates
- thank-you templates
- screening answer templates

### Phase 4 — Build targeting and scoring
- define target role categories
- define fit scoring logic
- define application priority logic
- define when to skip weak-fit roles

### Phase 5 — Build interview prep system
- create STAR story bank
- create common technical interview question bank
- create customer-facing scenario bank
- create company prep templates

## First Deliverables the AI System Should Produce

1. **Asset Inventory**
   - list every relevant file, doc, and sheet currently in the projects folder

2. **Master Candidate Profile**
   - distilled from resume + existing documents

3. **References Database**
   - converted from Google Sheets into a clean structured table

4. **Job Tracker**
   - spreadsheet or CSV with required columns

5. **Resume Bullet Bank**
   - broken into tagged reusable bullets

6. **Template Pack**
   - outreach, referral, follow-up, and thank-you templates

## Plain-English Tasking Prompt for an AI Builder

Use this as the instruction block for the AI system:

> Build an AI-assisted job search operating system using my existing projects folder as the starting point. I already have a current resume, Google Docs, and Google Sheets containing references. First, inventory and classify all existing assets. Then create a source-of-truth workspace containing a master candidate profile, modular resume bullet bank, references database, job tracker, outreach templates, and interview prep framework. The system must only use truthful information from my real background and should optimize for tech roles such as solutions engineer, technical support engineer, implementation specialist, customer success engineer, and adjacent technical roles. Geographic focus should prioritize Austin, Texas and remote opportunities. Keep the workflow human-reviewed, structured, reusable, and easy to update.

## Technical Build Notes

If this is being turned into an actual automation system, the first implementation should probably use:
- local folder scan
- file parser for docs / sheets / resume files
- structured JSON outputs for candidate data
- spreadsheet-backed tracker
- prompt templates for tailoring and outreach
- a simple scoring layer for job fit

Do not start with complicated agents everywhere. Start with:
- clean data
- clean folders
- clean schemas
- predictable outputs

That’s what will keep it from turning into mush.

## Recommended Next Action

Start by having the AI system do only this:

**“Inventory my current job-search assets and convert them into a structured source-of-truth workspace.”**

That is step one. Not applying yet. Not mass tailoring yet. First clean the ground.
