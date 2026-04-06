---
name: resume-matcher
description: Score and match a resume against a target job description using the AI-powered Resume-Matcher tool.
---
# Resume-Matcher Protocol

This tool replaces legacy hardcoded keyword-matching scripts. It provides AI-powered, contextual score analysis between a master/tailored resume and a targeted Job Description.

## Instructions
1. Ensure the Local Resume Matcher Docker container or backend is running.
2. Feed the job description text (`JD_[Company]_[Role].txt`) and the current drafted resume into the Resume-Matcher system.
3. Review the AI-generated keyword match scores and suggested improvements.
4. Modify the resume data appropriately based on its feedback regarding layout, missing concepts, and metrics.
5. Provide the user with the revised Resume-Matcher findings.
