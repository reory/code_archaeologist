# 🤝 Contributing to Code Archeologist

Thank you for wanting to contribute to Code Archeologist

---

# 📜 The Golden Rules
- Standard Library Only: 
No external dependencies. 
The tool must remain a single, portable .py file that runs on a vanilla Python installation.

- Human-in-the-Loop: Features should assist developer decision-making, not automate code deletion.

- Zero Footprint: Ensure the scanner remains "Read-Only" and does not modify the target codebase.

---

# ⚙️ How to Contribute
- Bug Fixes: If the AST parser misses a specific Python 3.13+ syntax, please submit a fix.

- New Patterns: Have a common framework pattern (like a specific decorator style) that the scanner misses? Add it to the inference logic.

- Roadmap Items: Refer to the README for planned features like Git "Carbon Dating" or Test-Awareness.

---

# 🚀 Submission Process
- Fork the repo.

- Create a feature branch (git checkout -b feature/AmazingFeature).

- Ensure your code passes standard pytest or Hypothesis checks if applicable.

- Open a Pull Request with a clear description of the "Archaeological" benefit.

---

Chat later 😊