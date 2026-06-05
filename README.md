# 🕵🏽 Code Archaeologist:

![Last Commit](https://img.shields.io/github/last-commit/reory/code-archaeologist?cacheSeconds=60)
![Repo Size](https://img.shields.io/github/repo-size/reory/code-archaeologist?cacheSeconds=60)
![License](https://img.shields.io/badge/License-MIT-green)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- Philosophy: Human-Controlled, Pattern-Driven Code Auditing.

---

## 🏫 What is this Project?
The Legacy Code Archaeologist is a precision static analysis tool built for developers who maintain a "Local Source of Truth." 
In an era of increasing AI automation, this project is designed for the "Small Dev" who wants to keep their work human-controlled while managing the complexity of modern Python ecosystems.

It treats a codebase like an archaeological site. Instead of mass-deleting code, it identifies "artifacts" (orphaned functions, unused helpers, and legacy fossils) and provides a Confidence Report. 
This allows the developer to act as the lead investigator—using the tool to find the "buried" code, but making the final executive decision on what to prune.

---

# 🧠 How it Works:
The scanner doesn't rely on a giant list of every library in existence. 
Instead, it uses three universal patterns:

### The Decorator Rule (Framework Awareness)
- Modern frameworks (`Flask`, `Django`, `FastAPI`) use decorators (e.g., @app.route) to register functions. 
The Archaeologist recognizes that any decorated function is an "Entry Point" and protects it from being flagged as an orphan.

### Interface Inference
The tool analyzes naming conventions to guess intent:
- Capitalized Names: Likely React-style components or Class definitions.
- Dunder Methods: Internal Python hooks (e.g., __init__).
These patterns signal that the code is part of a larger interface and should be treated with care.

### The Confidence Score
Every discovery is assigned a "Dead Confidence" percentage:
- 100%: Standard function, no local calls, no decorators. (High likelihood of being a relic).
- 40%: Internal or capitalized function. (Possible framework hook).
- 0%: Actively used or decorated. (Protected heritage).

---

# 📂 Project Structure
```python
uk-population-tracker/
├── scanner.py                 # The core Archaeologist engine
├── archaeology_report.json    # The generated "Dig Ledger" (JSON output)
├── .gitignore                 # Configured to ignore the report and pycache
└── [Your Project Files]       # The "Dig Site" being scanned
```

---

## 🚀 Usage Guide **The Briefcase workflow**

# 📖 Please Read **Important**
Code Archaeologist is designed as a self-contained, portable audit kit. It does not require installation or complex path configurations.

### Prerequisites
Python 3.13.7 (Tested environment)
A project directory with .py files.

### Deployment
To audit a "dig site," simply copy scanner.py into the root directory of the project you wish to scan.

**Note**: For the most accurate results, place it at the same level as your app/, src/, or processing/ folders.

### Execution
Open your terminal in that folder and run the script using the Python interpreter:

```Bash
python scanner.py
```
### Why this Method?
- Path Precision: 
By sitting in the root, the scanner’s internal "radar" (using os.walk) automatically maps the entire project structure without manual configuration.

- Zero-Footprint: 
There is no need to pip install or manage virtual environments. As long as Python is on the machine, the scanner is ready to work.

- Isolated Results: 
The generated archaeology_report.json stays within the project folder, keeping your audit data exactly where the code lives.

---

## 🔎 Reviewing the Finds
- The tool will output a table to your terminal and generate a archaeology_report.json. This **JSON** is designed to be "human-readable" but also "machine-ingestible," making it perfect for feeding into an AI Prompt PR Dev tool to generate cleanup Pull Requests.

---

## 🔐 Security & Privacy
- Zero-Cloud Dependency: All scanning happens locally on your hardware.
- Read-Only Analysis: The scanner uses Python's ast module to read code structure without executing it, ensuring no side effects occur during the "dig."

---

## 🛣️ Roadmap Features

- [ ] Carbon Dating – Integrate with local .git logs to increase "Dead Confidence" for functions that haven't been modified in months.

- [ ] X-Ray Vision – Map internal "trade routes" between files to visualize local dependencies and cross-module usage.

- [ ] Test Awareness – Cross-reference app/ code with tests/ to identify helpers that only exist to support deleted or legacy test cases.

- [ ] The Vault – Support a local archaeo.json configuration file for custom whitelists and project-specific "Protected Patterns."

- [ ] Pre-Commit Sentry – Implementation as a Git pre-commit hook to catch and report new "orphans" before they are committed to history.

---

* **Built by Roy Peters** 😊
- Keeping code human-controlled, one artifact at a time.
- Thanks for stopping by.
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Roy%20Peters-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roy-p-74980b382/)