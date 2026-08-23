# Python CLI Project Template

A Python command-line interface project template.

## Guide

### Create .env file.
```
MAX_RETRIES=3
RETRY_INTERVAL_SECONDS=0
RETRY_RAISE_EXCEPTION=True
```

### Create virtual environment.
```bash
python -m venv .venv
```

### Activate virtual environment.
```bash
.venv\Scripts\Activate.ps1
```

### Update pip.
```bash
python -m pip install -U pip
```

### Install packages.
```bash
pip install -r requirements.txt
```

### Create executable file.
```bash
python -m nuitka main.py --onefile --windows-console-mode=force --remove-output --assume-yes-for-downloads --output-filename=python-cli-project-template.exe --output-dir="C:\Users\{User Profile}\Downloads"
pyinstaller main.py --onefile --console --clean --name "python-cli-project-template" --distpath "C:\Users\{User Profile}\Downloads"
```