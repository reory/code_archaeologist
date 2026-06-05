import ast
import os
import json
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("Archaeologist")


class ArchaeologistScanner:
    def __init__(self):
        self.definitions = {}  # {name: node}
        self.calls = set()  # Track unique function calls via AST analysis
        self.file_map = {}  # {name: filepath}

    def scan_file(self, filepath):
        """Scan a file and return parsed results"""

        with open(filepath, "r", encoding="utf-8") as f:
            try:
                # Convert source code into tree for structural inspection
                tree = ast.parse(f.read())
                for node in ast.walk(tree):
                    # Capture function definitions
                    if isinstance(
                        node, (ast.FunctionDef, ast.AsyncFunctionDef)
                    ):
                        # Create a unique key using the file path and function name
                        unique_id = f"{filepath}:{node.name}"
                        self.definitions[unique_id] = node
                        self.file_map[unique_id] = filepath

                    # Capture function calls (local and method chaining)
                    if isinstance(node, ast.Call):
                        # Standard calls: func()
                        if isinstance(node.func, ast.Name):
                            self.calls.add(node.func.id)
                        # Chained calls: obj.method()
                        elif isinstance(node.func, ast.Attribute):
                            self.calls.add(node.func.attr)
                # Detailed trace
                logger.debug(f"Successfully excavated {filepath}")
            except Exception as e:
                logger.error(f"Excavation failed {filepath}: {e}")

    def calculate_confidence(self, name, node):
        """
        Assigns a confidence score (0-100) that the code is 'Dead'.
        Lower score = More likely its actually in use (protected)
        """

        score = 100

        # The Decorator Rule (Framework entry points)
        # Covers Flask, Django, FastAPI, Celery, etc.
        if node.decorator_list:
            return 0  # 0% chance its dead; decorators mean it's an entry point

        # Interface Inference (React-like or standard Dunders)
        # Component-style names (Capitalised) or Python internals
        if name.startswith("__") or name[0].isupper():
            score -= 60

        # Private Indicators
        # Leading underscores often mean its only for local use
        if name.startswith("_") and not name.startswith("__"):
            score += 10

        # Usage Check
        if name in self.calls:
            return 0  # Definitely in use

        # Return the final result between 0 and 100 for consistent scoring
        return min(max(score, 0), 100)

    def run(self, directory):
        """Run the Tool."""

        # Log the start of the process
        logger.info(f"Surverying Site: {os.path.abspath(directory)}")

        # looks through the directory tree to locate all source files
        for root, _, filenames in os.walk(directory):
            if any(
                x in root for x in ["venv", ".git", "__pycache__", "tests"]
            ):
                continue
            for filename in filenames:
                if filename.endswith(".py"):
                    self.scan_file(os.path.join(root, filename))

        # Initialise an empty list to store the findings for the final summary
        report = []

        # Use unique_id (path:name) to iterate through definitions
        for unique_id, node in self.definitions.items():

            # Extract the actual function name for the confidence rules
            name = node.name

            # Assign a probability score based on naming patterns and
            # framework usage
            dead_confidence = self.calculate_confidence(name, node)

            # Catalogue suspected dead code with
            # its source location and probability score
            if dead_confidence > 0:
                report.append(
                    {
                        "function": name,
                        "file": self.file_map[unique_id],
                        "dead_confidence": f"{dead_confidence}%",
                    }
                )

        # Sort by most likely to be 'dead'
        return sorted(
            report,
            key=lambda x: int(x["dead_confidence"].strip("%")),
            reverse=True,
        )

    def save_report(self, report, filename="archaeology_report.json"):
        """Write analysis report to a JSON file"""

        with open(filename, "w", encoding="utf-8") as f:
            # Save to a JSON
            json.dump(report, f, indent=4)
        # Confirm the report has been stored.
        logger.info(f"\n ✅Site Report saved to: {os.path.abspath(filename)}")


if __name__ == "__main__":
    scanner = ArchaeologistScanner()

    # Start the Action of scanner.py
    logger.info("🕵🏽 Starting site excavation..")

    # Execute the scan from the current root to map the entire project geography
    results = scanner.run(".")

    # Format and display the findings in a structured table
    print(f"🕵🏽SITE REPORT: {len(results)} potential artifacts found. \n")
    print(f"{'CONFIDENCE':<12} | {'FUNCTION':<25} | {'LOCATION'}")
    print("-" * 85)

    # Display each discovered artifact to the console for real-time review
    for r in results:
        # Truncate for a clean UI
        location = (
            (r["file"][:50] + "..") if len(r["file"]) > 50 else r["file"]
        )
        print(f"{r['dead_confidence']:<12} | {r['function']:<25} | {location}")

    print("_" * 85)  # Closing line for the table

    # Log the end of the transition
    logger.info("Excavation complete. Archiving results..")

    # Save the report to a JSON file.
    scanner.save_report(results)
