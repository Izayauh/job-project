"""
Match Report System — ATS Keyword Scoring Tool
================================================
Scores a resume against a job description by extracting and matching
hard skills, soft skills, job title, negative words, and word count.

Usage:
    python match_report.py <resume_file> <jd_file> [--output report.txt]

    resume_file: path to resume (.pdf, .docx, .md, or .txt)
    jd_file:     path to job description (.txt or .md)

Example:
    python match_report.py ../04_Applications/Plaid/Resume_Plaid_TSE_v4.pdf jd_plaid.txt
"""

import re
import sys
import os
import json
import argparse
from collections import Counter

# ── Negative Words List ────────────────────────────────────────
# Words/phrases that ATS tone checkers commonly flag
NEGATIVE_WORDS = [
    "failure", "failures", "failed", "fail",
    "problem", "problems", "problematic",
    "wrong", "error", "errors",
    "weakness", "weaknesses", "weak",
    "poor", "poorly",
    "lack", "lacking",
    "unable", "cannot",
    "difficult", "difficulty",
    "struggle", "struggled", "struggling",
    "crisis", "crises",
    "conflict", "conflicts",
    "complaint", "complaints",
    "mistake", "mistakes",
    "unfortunately",
    "downturn", "downed",
    "fired", "terminated", "laid off",
    "hate", "hated",
    "quit", "quitting",
    "without supervision",
    "without direct supervision",
    "not responsible",
    "no experience",
]

# ── Common Soft Skills to Check ────────────────────────────────
COMMON_SOFT_SKILLS = [
    "collaborative", "collaboration", "collaborate",
    "customer-centric", "customer centric",
    "customer-facing", "customer facing",
    "customer needs",
    "empathetic", "empathy",
    "time management",
    "work independently", "independently",
    "self-starter", "self starter",
    "written and verbal communication",
    "strong communication",
    "problem-solving", "problem solving",
    "critical thinking",
    "attention to detail",
    "team player", "teamwork",
    "leadership", "lead",
    "adaptable", "adaptability",
    "creative", "creativity",
    "brainstorming",
    "cross-functionally", "cross-functional", "cross functionally",
    "proactive", "proactively",
    "organized", "organization",
    "multitasking", "multi-tasking",
    "interpersonal",
    "analytical",
    "reliable", "reliability",
    "motivated", "self-motivated",
    "detail-oriented", "detail oriented",
]


def extract_text_from_pdf(path):
    """Extract text from PDF using fpdf2's parsing or fallback."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except ImportError:
        pass

    # Fallback: try pdfminer
    try:
        from pdfminer.high_level import extract_text as pdfminer_extract
        return pdfminer_extract(path)
    except ImportError:
        pass

    # Last resort: read as bytes and decode what we can
    print("WARNING: No PDF library available (install pypdf or pdfminer.six)")
    print("         Falling back to raw text extraction — results may be poor")
    with open(path, "rb") as f:
        raw = f.read()
    # Extract printable ASCII runs
    text = re.sub(rb'[^\x20-\x7e\n\r]', b' ', raw).decode('ascii', errors='ignore')
    return text


def extract_text_from_docx(path):
    """Extract text from DOCX."""
    from docx import Document
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)


def read_file(path):
    """Read any supported file format and return plain text."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(path)
    elif ext == ".docx":
        return extract_text_from_docx(path)
    else:  # .txt, .md, etc.
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


def normalize(text):
    """Lowercase, normalize hyphens to spaces, and clean text for matching.

    Hyphens are replaced with spaces so that 'root-cause' matches 'root cause'
    and vice versa — Jobscan treats these as equivalent.
    """
    text = text.lower().strip()
    text = text.replace('-', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text


def count_occurrences(text, keyword, use_word_boundary=False):
    """Count case-insensitive occurrences of a keyword/phrase in text.

    Both text and keyword are hyphen-normalized (hyphens → spaces) so that
    'root-cause' matches 'root cause' and vice versa.

    Args:
        use_word_boundary: If True, require word boundaries around the keyword.
            Automatically enabled for short keywords (<=3 chars) to prevent
            false positives like 'ai' matching 'maintain' or 'go' matching 'going'.
    """
    # Normalize hyphens to spaces in both text and keyword
    norm_text = normalize(text)
    norm_keyword = keyword.lower().replace('-', ' ').strip()
    escaped = re.escape(norm_keyword)
    # Force word boundaries for short keywords to prevent false positives
    if use_word_boundary or len(norm_keyword) <= 3:
        pattern = r'\b' + escaped + r'\b'
    else:
        pattern = escaped
    return len(re.findall(pattern, norm_text))


def extract_hard_skills(jd_text):
    """Extract likely hard skills from JD text.

    Uses a combination of known tech keywords and n-gram extraction.
    Returns a list of (skill, count_in_jd) tuples.
    """
    jd_lower = normalize(jd_text)

    # Known tech/hard skill patterns to check
    # Organized by category for maintainability
    known_skills = [
        # ── Programming Languages ──
        "python", "javascript", "typescript", "java", "ruby", "go", "golang",
        "rust", "c++", "c#", "php", "swift", "kotlin",
        # ── Web / Markup ──
        "html", "css", "sql", "nosql", "graphql",
        # ── APIs ──
        "rest api", "rest apis", "openapi", "api", "apis",
        # ── Frameworks ──
        "react", "angular", "vue", "node.js", "express",
        "django", "flask", "fastapi",
        # ── Cloud / Infra ──
        "aws", "azure", "gcp", "google cloud",
        "docker", "kubernetes", "terraform",
        # ── Version Control / Collaboration ──
        "git", "github", "gitlab", "bitbucket",
        "jira", "zendesk", "salesforce", "hubspot",
        "slack", "confluence", "notion",
        # ── Operating Systems ──
        "linux", "windows", "macos",
        # ── Databases & Search ──
        "mongodb", "postgresql", "mysql", "redis", "elasticsearch",
        "kibana",
        # ── Message Queues ──
        "rabbitmq", "kafka",
        # ── DevOps / Methodologies ──
        "ci/cd", "devops", "agile", "scrum",
        # ── AI / Data ──
        "machine learning", "ai", "data science", "analytics",
        "data visualization", "data visualizations",
        # ── Support & Operations ──
        "technical support", "customer support", "application support",
        "technical projects", "remote support",
        "troubleshoot", "troubleshooting",
        "debugging", "java debugging",
        "documentation", "technical documentation",
        "knowledge base articles", "knowledge base",
        "internal tools", "support tools",
        "crm systems", "crm",
        "ticketing systems", "ticketing",
        "incident management", "ticket management",
        "on-call", "on call",
        # ── Programming Concepts ──
        "coding", "programming", "scripting",
        "python scripting",
        "tooling", "automation",
        # ── Domain / Industry ──
        "financial services", "fintech",
        "supply chain", "logistics",
        "transportation management", "tms",
        "freight",
        # ── Root Cause / Process ──
        "root cause", "root-cause", "root cause analysis",
        "integration", "integration issues",
        "process improvement", "performance improvement",
        "product enhancements",
        # ── SLA / SRE ──
        "service level agreements", "sla", "slas",
        "site reliability engineering", "site reliability",
        # ── Education Fields (Jobscan checks these) ──
        "computer science", "information technology",
        "computer information systems",
        # ── General Tech ──
        "networking", "infrastructure",
        "monitoring", "observability",
        "security", "compliance",
        "saas", "b2b", "b2c",
        "onboarding", "implementation",
        "configuration", "deployment",
        "testing", "qa", "quality assurance",
        "browser developer tools", "browser dev tools", "developer tools",
        "webhook", "webhooks", "api polling",
        "customer success", "customer experience",
    ]

    found = []
    for skill in known_skills:
        count = count_occurrences(jd_text, skill)
        if count > 0:
            found.append((skill, count))

    # Deduplicate: remove skills that are substrings or exact duplicates
    # (after hyphen normalization) of longer phrases already kept.
    # E.g., "root cause" is dropped when "root cause analysis" is present.
    # "on-call" and "on call" are treated as the same skill.
    found.sort(key=lambda x: len(x[0]), reverse=True)
    deduplicated = []
    seen_normalized = set()
    for skill, count in found:
        norm_skill = skill.lower().replace('-', ' ')
        # Skip exact duplicates after normalization
        if norm_skill in seen_normalized:
            continue
        # Skip substrings of already-kept skills
        is_substring = False
        for norm_kept in seen_normalized:
            if norm_skill in norm_kept and norm_skill != norm_kept:
                is_substring = True
                break
        if not is_substring:
            deduplicated.append((skill, count))
            seen_normalized.add(norm_skill)

    return deduplicated


def extract_soft_skills(jd_text):
    """Extract soft skills found in JD from the common list."""
    found = []
    for skill in COMMON_SOFT_SKILLS:
        count = count_occurrences(jd_text, skill)
        if count > 0:
            found.append((skill, count))
    # Deduplicate: remove substrings and hyphen-normalized duplicates
    found.sort(key=lambda x: len(x[0]), reverse=True)
    deduplicated = []
    seen_normalized = set()
    for skill, count in found:
        norm_skill = skill.lower().replace('-', ' ')
        if norm_skill in seen_normalized:
            continue
        is_substring = False
        for norm_kept in seen_normalized:
            if norm_skill in norm_kept and norm_skill != norm_kept:
                is_substring = True
                break
        if not is_substring:
            deduplicated.append((skill, count))
            seen_normalized.add(norm_skill)
    return deduplicated


def extract_job_title(jd_text):
    """Try to extract the job title from the JD.

    Looks for common patterns like 'Role: X', 'Position: X', or
    takes the first line if short enough.
    """
    lines = jd_text.strip().split("\n")

    # Check for explicit title patterns
    for line in lines[:10]:
        line = line.strip()
        for prefix in ["title:", "role:", "position:", "job title:"]:
            if line.lower().startswith(prefix):
                return line[len(prefix):].strip()

    # Check for common title patterns in first few lines
    title_patterns = [
        r"(?:technical\s+)?support\s+engineer",
        r"(?:customer\s+)?success\s+engineer",
        r"solutions?\s+engineer",
        r"implementation\s+(?:specialist|engineer|consultant)",
        r"(?:associate\s+)?professional\s+services\s+consultant",
        r"technical\s+account\s+manager",
        r"customer\s+support\s+engineer",
        r"(?:senior\s+)?software\s+engineer",
        r"(?:key\s+)?account\s+(?:support\s+)?engineer",
    ]

    for line in lines[:15]:
        for pattern in title_patterns:
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                return match.group(0).strip()

    # Fallback: first non-empty line under 60 chars
    for line in lines[:5]:
        line = line.strip()
        if 5 < len(line) < 60:
            return line

    return None


def check_negative_words(resume_text):
    """Check for negative words/phrases in resume text."""
    found = []
    resume_lower = resume_text.lower()
    for word in NEGATIVE_WORDS:
        count = count_occurrences(resume_text, word)
        if count > 0:
            found.append((word, count))
    return found


def score_resume(resume_text, jd_text):
    """Score a resume against a job description.

    Returns a dict with:
    - overall_score (0-100)
    - hard_skills: list of {skill, jd_count, resume_count, matched}
    - soft_skills: list of {skill, jd_count, resume_count, matched}
    - job_title: {title, found_in_resume}
    - negative_words: list of {word, count}
    - word_count: int
    - recommendations: list of strings
    """
    results = {
        "hard_skills": [],
        "soft_skills": [],
        "job_title": {},
        "negative_words": [],
        "word_count": 0,
        "recommendations": [],
    }

    # ── Word Count ──
    words = resume_text.split()
    results["word_count"] = len(words)

    # ── Job Title Match ──
    title = extract_job_title(jd_text)
    if title:
        found = count_occurrences(resume_text, title) > 0
        results["job_title"] = {"title": title, "found_in_resume": found}
        if not found:
            results["recommendations"].append(
                f"CRITICAL: Add exact job title '{title}' to your Professional Summary"
            )

    # ── Hard Skills ──
    jd_hard = extract_hard_skills(jd_text)
    hard_matched = 0
    hard_total = len(jd_hard)

    for skill, jd_count in jd_hard:
        resume_count = count_occurrences(resume_text, skill)
        matched = resume_count > 0
        if matched:
            hard_matched += 1
        results["hard_skills"].append({
            "skill": skill,
            "jd_count": jd_count,
            "resume_count": resume_count,
            "matched": matched,
        })
        if not matched:
            results["recommendations"].append(
                f"MISSING hard skill: '{skill}' (appears {jd_count}x in JD)"
            )

    # ── Soft Skills ──
    jd_soft = extract_soft_skills(jd_text)
    soft_matched = 0
    soft_total = len(jd_soft)

    for skill, jd_count in jd_soft:
        resume_count = count_occurrences(resume_text, skill)
        matched = resume_count > 0
        if matched:
            soft_matched += 1
        results["soft_skills"].append({
            "skill": skill,
            "jd_count": jd_count,
            "resume_count": resume_count,
            "matched": matched,
        })
        if not matched:
            results["recommendations"].append(
                f"MISSING soft skill: '{skill}' (appears {jd_count}x in JD)"
            )

    # ── Negative Words ──
    negatives = check_negative_words(resume_text)
    results["negative_words"] = [{"word": w, "count": c} for w, c in negatives]
    for word, count in negatives:
        results["recommendations"].append(
            f"NEGATIVE WORD: '{word}' found {count}x — consider rephrasing"
        )

    # ── Word Count Check ──
    if results["word_count"] < 700:
        results["recommendations"].append(
            f"Word count is {results['word_count']} — aim for 800-1000 for better ATS relevance"
        )

    # ── Calculate Score ──
    # Scoring weights — calibrated against Jobscan (March 2026):
    # Jobscan heavily penalizes missing hard skills. Each missing hard skill
    # costs roughly 2-3 points. Hard skills dominate the score (~70%).
    # Soft skills matter less (~15%). Title, word count, negatives fill the rest.
    #
    # Previous weights (55/25/10) were too generous — produced 86 when
    # Jobscan scored 64 on the same resume. The gap was caused by:
    #   1. Missing skills not being extracted (fixed above)
    #   2. False-positive matches inflating hard skill % (fixed with word boundaries)
    #   3. Soft skills weighted too high, masking hard skill gaps

    hard_pct = (hard_matched / hard_total * 100) if hard_total > 0 else 100
    soft_pct = (soft_matched / soft_total * 100) if soft_total > 0 else 100
    title_pct = 100 if results["job_title"].get("found_in_resume", True) else 0

    neg_penalty = min(len(negatives) * 3, 10)
    word_bonus = 0
    if results["word_count"] < 700:
        word_bonus = -3  # penalize very short resumes
    elif results["word_count"] <= 1000:
        word_bonus = 3
    else:
        word_bonus = 2  # slightly over is fine

    score = (
        hard_pct * 0.70 +
        soft_pct * 0.15 +
        title_pct * 0.08 +
        word_bonus -
        neg_penalty
    )
    results["overall_score"] = round(min(max(score, 0), 100))

    # Component scores for display
    results["hard_score"] = round(hard_pct)
    results["soft_score"] = round(soft_pct)
    results["hard_matched"] = hard_matched
    results["hard_total"] = hard_total
    results["soft_matched"] = soft_matched
    results["soft_total"] = soft_total

    return results


def format_report(results, resume_path, jd_path):
    """Format results into a readable text report."""
    lines = []
    lines.append("=" * 65)
    lines.append("  MATCH REPORT")
    lines.append("=" * 65)
    lines.append(f"Resume:  {os.path.basename(resume_path)}")
    lines.append(f"JD:      {os.path.basename(jd_path)}")
    lines.append("")
    lines.append(f"  OVERALL SCORE: {results['overall_score']}/100")
    lines.append("")
    lines.append(f"  Hard Skills:  {results['hard_matched']}/{results['hard_total']} matched ({results['hard_score']}%)")
    lines.append(f"  Soft Skills:  {results['soft_matched']}/{results['soft_total']} matched ({results['soft_score']}%)")
    lines.append(f"  Word Count:   {results['word_count']}")
    if results.get("job_title"):
        jt = results["job_title"]
        status = "MATCHED" if jt["found_in_resume"] else "MISSING"
        lines.append(f"  Job Title:    '{jt['title']}' — {status}")
    lines.append(f"  Neg. Words:   {len(results['negative_words'])} found")
    lines.append("")

    # Hard Skills Table
    lines.append("-" * 65)
    lines.append("  HARD SKILLS")
    lines.append("-" * 65)
    lines.append(f"  {'Skill':<30} {'Resume':>8} {'JD':>8} {'Status':>10}")
    lines.append(f"  {'-'*30} {'-'*8} {'-'*8} {'-'*10}")
    for s in sorted(results["hard_skills"], key=lambda x: x["matched"]):
        status = "OK" if s["matched"] else "MISSING"
        lines.append(f"  {s['skill']:<30} {s['resume_count']:>8} {s['jd_count']:>8} {status:>10}")

    lines.append("")

    # Soft Skills Table
    lines.append("-" * 65)
    lines.append("  SOFT SKILLS")
    lines.append("-" * 65)
    lines.append(f"  {'Skill':<30} {'Resume':>8} {'JD':>8} {'Status':>10}")
    lines.append(f"  {'-'*30} {'-'*8} {'-'*8} {'-'*10}")
    for s in sorted(results["soft_skills"], key=lambda x: x["matched"]):
        status = "OK" if s["matched"] else "MISSING"
        lines.append(f"  {s['skill']:<30} {s['resume_count']:>8} {s['jd_count']:>8} {status:>10}")

    # Negative Words
    if results["negative_words"]:
        lines.append("")
        lines.append("-" * 65)
        lines.append("  NEGATIVE WORDS FOUND")
        lines.append("-" * 65)
        for nw in results["negative_words"]:
            lines.append(f"  '{nw['word']}' — {nw['count']}x")

    # Recommendations
    if results["recommendations"]:
        lines.append("")
        lines.append("-" * 65)
        lines.append("  RECOMMENDATIONS")
        lines.append("-" * 65)
        for i, rec in enumerate(results["recommendations"], 1):
            lines.append(f"  {i}. {rec}")

    lines.append("")
    lines.append("=" * 65)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Score a resume against a job description for ATS optimization"
    )
    parser.add_argument("resume", help="Path to resume file (.pdf, .docx, .md, .txt)")
    parser.add_argument("jd", help="Path to job description file (.txt, .md)")
    parser.add_argument("--output", "-o", help="Save report to file", default=None)
    parser.add_argument("--json", action="store_true", help="Output as JSON instead of text")
    args = parser.parse_args()

    if not os.path.exists(args.resume):
        print(f"Error: Resume file not found: {args.resume}")
        sys.exit(1)
    if not os.path.exists(args.jd):
        print(f"Error: JD file not found: {args.jd}")
        sys.exit(1)

    resume_text = read_file(args.resume)
    jd_text = read_file(args.jd)

    results = score_resume(resume_text, jd_text)

    if args.json:
        output = json.dumps(results, indent=2)
    else:
        output = format_report(results, args.resume, args.jd)

    print(output)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"\nReport saved to: {args.output}")


if __name__ == "__main__":
    main()
