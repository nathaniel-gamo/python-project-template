# Python CLI Project Template

A Python command-line interface project template.

## Guide

### Create .env file.
```
LOG_FILE_PATH=app.log
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
pyinstaller main.py --onefile --console --clean --name "main" --distpath "C:\Users\{User Profile}\Downloads"
```