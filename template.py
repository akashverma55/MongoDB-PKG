import os
from pathlib import Path
import logging

package_name = "MongoDB-Connector"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

list_of_files = [
    ".github/workflows/ci.yaml",
    ".github/workflows/python-publish.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/integration.py",
    "init_setup.sh",
    "requirements.txt", 
    "requirements_dev.txt", 
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiment.py",
    ".gitignore",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as file:
            logging.info(f"Created file: {filepath}")