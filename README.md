 ### Author
 Nikola Djuric (github.com/ndjuric)


### Description
scaffolding a project, or multiple, every day does enter muscle memory but it's toil, I wrote this one for my own usage


### More details
It will manifest a pristine project directory structure.
Idea is to remove some toil if you play with Python often, and, of course, find the structure pleasing.

You'll also get a virtual environment, a Makefile, a main.py (with logging setup), and some additional scaffolding to start with.

The structure is inspired by the following:
    • https://docs.python-guide.org/writing/structure/


The hierarchy is as follows:
|.
├── Makefile         - I come from C, and I still find comfort in the embrace of a Makefile.
├── README.md        - This is for you, your future self, your colleagues, or, the world.
├── scripts          - Here, I tend to keep shell scripts or such that I invoke from the Makefile.
├── src              - Everything you write, the source code of your project, write it here.
│   └── main.py      - I usually start developing here, it is executable from the beginning; it configures logging and prints a friendly message.
├── storage          - A place for you to store whatever you need.
│   ├── data         - Data files, databases, program state, etc.
│   │   └── .gitkeep - .gitkeep - Git does not track empty folders.
│   └── logs         - Chronicling the silent narrative of your program’s evolution.
│       └── .gitkeep - .gitkeep - Adding .gitkeep ensures empty folders are preserved.
├── venv             - A virtual environment for your project, created automatically.

### Requirements

Requires Python 3.6+ and was tested on Linux and macOS.
--------------------------------
On Ubuntu/Debian (Linux):
Make sure you have Python 3 installed along with the venv module:
```bash
sudo apt-get update
sudo apt-get install python3 python3-venv
```
Even though venv is part of the standard library since Python 3.3, some distros package it separately.

--------------------------------
On macOS:
Python 3 comes pre-installed. To create a virtual environment:
```bash
python3 -m venv venv
```
Or install Python 3 via Homebrew:
```bash
brew install python3
```
Ensure that the folder that contains the 'python' binary is in your PATH.

### Running

To run as a standalone script:
```bash
chmod +x scaffold_python.py
./scaffold_python.py
```

To run as a module:
```bash
python -m scaffold_python
```

Or import the class into a different file and invoke scaffolding from there, as shown in the main function of the file.

Let order emerge from entropy!