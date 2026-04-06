---
name: rendercv
description: Format an AI-generated resume from YAML into a beautiful PDF using LaTeX under the hood via the RenderCV tool.
---
# RenderCV Resume Formatting Process

RenderCV takes a specifically formatted YAML file representing your resume and compiles it into a high-quality LaTeX PDF.

## Instructions
1. Instead of outputting Markdown to be parsed by `fpdf2` or `python-docx`, construct a YAML file that adheres to the RenderCV schema.
2. The YAML file should include sections such as `cv`, `name`, `sections`, `education`, `experience`, etc.
3. Save the YAML file as `Resume_[Company]_[Role].yaml` in the respective application folder.
4. Render the resume by running `rendercv render Resume_[Company]_[Role].yaml`.
5. The output will be a highly professional, beautifully typeset PDF (many classic templates available, e.g., the 'sb2nov' template which matches the JakeGut/resume style).
