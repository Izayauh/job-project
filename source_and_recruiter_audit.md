# Source and Recruiter Audit

This document audits the recently created resume deliverables against both internal repository facts and external recruiter/ATS best practices.

## Major Issues Identified

### Issue 1: Dense Summaries and Outdated Objectives
- **File:** `resume_rebuild.md`
- **Exact phrase:** "Seeking a Technical Support Engineer role grounded in clear communication..."
- **Issue type:** recruiter readability problem, ATS / formatting risk
- **Internal source support:** partial (Matches the profile intent but not the tone)
- **External guidance support:** none (Modern summaries should be 2-3 punchy sentences focused strictly on value delivery, not what the candidate is "seeking.")
- **Action:** rewrite
- **Corrected wording:** Convert dense paragraphs into 2-3 short, distinct sentences focusing strictly on verifiable scope (years of experience + key technical stack + core competency). Remove the "Seeking a..." clause entirely.

### Issue 2: Boilerplate "Duties" Rather Than Acquired Scope
- **File:** `resume_rebuild.md` (TSE and SE versions)
- **Exact phrase:** "Process 2-10 tickets per shift through an internal platform while managing outbound follow-up calls and status updates."
- **Issue type:** fake precision / recruiter readability problem
- **Internal source support:** direct (Matches user estimates)
- **External guidance support:** partial (Metrics are good, but daily task estimates can look like fake metrics if they aren't tied to a larger business outcome or SLA system. Broad scope is better than granular task counts if the counts are estimates.)
- **Action:** rewrite
- **Corrected wording:** "Execute structured diagnostic workflows to manage ticket lifecycles, maintaining communication with non-technical users from initial report to resolution."

### Issue 3: Keyword Stuffing Risk in Tailoring Protocol
- **File:** `tailoring_protocol.md`
- **Exact phrase:** "Skills Ordering: Shift the most relevant tool keywords to the front of the list, provided they are already possessed."
- **Issue type:** keyword stuffing risk
- **Internal source support:** direct (Matches the intention of adapting to the JD)
- **External guidance support:** partial (ATS parsers give much higher weight to keywords placed *in context* within experience bullets than a comma-separated list.)
- **Action:** rewrite
- **Corrected rule:** "Skills Alignment: Ensure required keywords appear naturally within experience or project bullets showing exactly *how* they were used, rather than just shifting them in a skills block."

### Issue 4: Weak Tailoring Logic
- **File:** `tailoring_protocol.md`
- **Exact phrase:** "Bullet Ordering: If the job emphasizes hardware triage, slide the hardware bullet to the top of the Nexus WiFi section."
- **Issue type:** weak tailoring logic
- **Internal source support:** direct
- **External guidance support:** partial (Trivial reordering does not provide context. The top bullet must consistently be the strongest summary of scope or impact, while the subsequent bullets prove specific requirements.)
- **Action:** rewrite
- **Corrected rule:** "Bullet Alignment: Retain the most impactful scope bullet at the top. For subsequent bullets, integrate specific job description requirements into the context of the work performed, rather than just dragging and dropping lines."

### Issue 5: Unsupported Project Claims Over Experience
- **File:** `resume_rebuild.md` (SE Version)
- **Exact phrase:** Leading the resume with the "Projects" section before "Experience".
- **Issue type:** ATS / formatting risk
- **Internal source support:** direct (Intent to highlight strengths)
- **External guidance support:** partial (Standard ATS parsers and human recruiters expect "Experience" immediately following "Skills". Placing projects first can confuse parsing logic and make the gap in formal SE titles more glaring.)
- **Action:** rewrite
- **Corrected rule:** Always use standard reverse-chronological section flow: Summary > Skills > Experience > Projects > Education. For the SE resume, let the bullet quality within the Experience and Projects sections carry the narrative, instead of breaking standard layout structures.
