# Python Project Template

A template for building command-line interface (CLI) projects and Python packages.

## Commands

### Create a .env file
```
MAX_RETRIES=3
RETRY_INTERVAL_SECONDS=0
RETRY_RAISE_EXCEPTION=True
```

### Create a virtual environment
```bash
python -m venv .venv
```

### Activate the virtual environment
```bash
.venv\Scripts\Activate.ps1
```

### Verify that the virtual environment is activated
```bash
Get-Command python
```

### Upgrade pip
```bash
python -m pip install --upgrade pip
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Update packages using pip-review
```bash
pip install --upgrade pip-review

pip-review
pip-review --auto
pip-review --interactive
```

### Ruff
```bash
pip install --upgrade ruff

ruff check .
ruff check . --fix

ruff format --check .
ruff format .
```

### Build a package using build
```bash
pip install --upgrade build

python -m build
```

### Upload the package to TestPyPI or PyPI using twine
```bash
pip install --upgrade twine

python -m twine check dist/*
python -m twine upload --repository testpypi dist/*
python -m twine upload dist/*
```

### Install the package uploaded to TestPyPI or PyPI
```bash
pip cache purge

pip install my_package --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/
pip install my_package --index-url https://pypi.org/simple/
```

### Create an executable using Nuitka
```bash
pip install --upgrade nuitka

python -m nuitka main.py --onefile --windows-console-mode=force --remove-output --assume-yes-for-downloads --output-filename=python-cli-project-template.exe --output-dir="C:\Users\{User Profile}\Downloads"
```

### Create an executable using PyInstaller
```bash
pip install --upgrade pyinstaller

pyinstaller main.py --onefile --console --clean --name "python-cli-project-template" --distpath "C:\Users\{User Profile}\Downloads"
```