import os
import glob

workspace_dir = r"C:\Users\isaia\Projects\tools\job-project"
extensions = ["*.md", "*.yaml", "*.txt", "*.py"]

# 1. Mass replace Live Pilot -> Live Pilot
for ext in extensions:
    for filepath in glob.glob(os.path.join(workspace_dir, "**", ext), recursive=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if "Live Pilot" in content:
                new_content = content.replace("Live Pilot", "Live Pilot")
                
                # Special cases for Master_Candidate_Profile.md and similar profiles
                if "Master_Candidate_Profile.md" in filepath or "Experience_Inventory.md" in filepath:
                    # Replace the specific old repo notes
                    new_content = new_content.replace(
                        "**Repo:** Local only (C:\\Users\\isaia\\Documents\\Live Pilot\\) — not public",
                        "**Repo:** github.com/Izayauh/LivePilot (public) - Local dev at C:\\Users\\isaia\\Projects\\music\\live-pilot"
                    )
                    new_content = new_content.replace(
                        "- **Portfolio rule:** Do not link publicly. No public repo.",
                        "- **Portfolio rule:** Link publicly to the GitHub repository."
                    )
                    
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {filepath}")
        except Exception as e:
            pass

print("Mass replacement completed successfully.")
