#!/usr/bin/env python
"""
Author: Nikola Djuric (github.com/ndjuric)
A smol scaffolding tool.
The structure is inspired by the following:
    • https://docs.python-guide.org/writing/structure/
With some personal additions.
"""

import logging
import os
import stat
import venv
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

class ProjectScaffolder:
    def __init__(self, project_name: str):
        self.project_name = project_name.strip()
        self.root = Path(self.project_name)

    def create_dir(self, dir_path: Path) -> bool:
        if dir_path.exists():
            logger.info(f"Directory already exists: {dir_path}")
            return True
        dir_path.mkdir(parents=True)
        logger.info(f"Created directory: {dir_path}")
        return True

    def create_file(self, file_path: Path, content: str = "") -> bool:
        if file_path.exists():
            logger.info(f"File already exists: {file_path}")
            return True
        file_path.write_text(content)
        logger.info(f"Created file: {file_path}")
        return True

    def make_executable(self, file_path: Path) -> bool:
        try:
            current_mode = file_path.stat().st_mode
            file_path.chmod(current_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
            logger.info(f"Set executable permissions for: {file_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to set executable permission for {file_path}: {e}")
            return False

    def create_virtualenv(self) -> bool:
        venv_dir = self.root / "venv"
        if venv_dir.exists():
            logger.info(f"Virtual environment already exists: {venv_dir}")
            return True
        try:
            builder = venv.EnvBuilder(with_pip=True)
            builder.create(venv_dir)
            logger.info(f"Created virtual environment at: {venv_dir}")
            return True
        except Exception as e:
            logger.error(f"Failed to create virtual environment: {e}")
            return False

    def setup_file_logging(self, logs_dir: Path) -> bool:
        log_file = logs_dir / "scaffold.log"
        try:
            file_handler = logging.FileHandler(log_file, mode="a")
            file_handler.setLevel(logging.INFO)
            formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.info(f"File logging activated: {log_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to set up file logging at {log_file}: {e}")
            return False

    def scaffold(self) -> bool:
        if not self.create_dir(self.root):
            return False

        storage = self.root / "storage"
        if not self.create_dir(storage):
            return False
        data_dir = storage / "data"
        if not self.create_dir(data_dir):
            return False
        logs_dir = storage / "logs"
        if not self.create_dir(logs_dir):
            return False
        if not self.create_file(data_dir / ".gitkeep"):
            return False
        if not self.create_file(logs_dir / ".gitkeep"):
            return False

        if not self.setup_file_logging(logs_dir):
            return False

        if not self.create_virtualenv():
            return False
        if not self.create_file(self.root / "README.md", f"# {self.project_name}\n"):
            return False
        if not self.create_file(self.root / "Makefile", "# Makefile\n"):
            return False
        if not self.create_dir(self.root / "scripts"):
            return False

        src_dir = self.root / "src"
        if not self.create_dir(src_dir):
            return False
        main_py_path = src_dir / "main.py"
        main_py_content = (
            "#!/usr/bin/env python\n"
            '"""\n'
            "This is the entry point of your project.\n"
            "It is pre-configured with logging (both to console and file, if desired).\n"
            '"""\n\n'
            "import logging\n"
            "import os\n"
            "from pathlib import Path\n\n"
            "# Configure logging\n"
            "logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')\n"
            "logger = logging.getLogger(__name__)\n\n"
            "def main():\n"
            "    logger.info('Hello, world! This is main.py in your project.')\n"
            "    print('Hello, world!')\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        )
        if not self.create_file(main_py_path, main_py_content):
            return False
        if not self.make_executable(main_py_path):
            return False

        return True

def main():
    project_name = input("Enter the project name: ").strip()
    if not project_name:
        logger.error("Project name cannot be empty.")
        exit(1)

    scaffolder = ProjectScaffolder(project_name)
    if not scaffolder.scaffold():
        logger.error("Scaffolding failed.")
        exit(1)

    logger.info("Scaffolding completed successfully.")
    exit(0)

if __name__ == "__main__":
    main()
