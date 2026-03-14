# Employee Payroll System

A robust, offline desktop application to manage employee payroll, attendance, and generating salary slips using Tkinter and SQLite.

## How to setup and run on another PC

### Requirements
You only need to install **Python** and three external packages to get this system working since it relies on a local SQLite database and doesn't require setting up a MySQL server.

### 1. Install Python
Download and install Python 3.10+ from the official python website for your operating system. Make sure you check **"Add Python to PATH"** in the Windows installer.

### 2. Copy the folder
Copy the entire `Employee Payroll System` folder to your new PC (via USB drive, cloud storage, etc.). This ensures you bring the main code files (`login.py`, `EPS.py`, `create_db.py`), your active database (`esc2.db`), and all your GUI images (`Images` folder) along with it.

### 3. Open Terminal/Command Prompt
Navigate into the folder on your new PC, and open the command prompt (or PowerShell).
You can do this easily on Windows by opening the folder, clicking on the folder path address bar at the top, typing `cmd`, and hitting Enter.

### 4. Setup Virtual Environment
It's recommended to create a virtual environment to manage dependencies cleanly. Run the following command to create one:
```shell
python -m venv venv
```

Activate the virtual environment:
- **On Windows:**
```shell
venv\Scripts\activate
```
- **On macOS/Linux:**
```shell
source venv/bin/activate
```

### 5. Install Dependencies
Run the following pip command to quickly install the necessary visual tools for Python:
```shell
pip install -r requirements.txt
```
*(This installs `Pillow`, `qrcode`, and `python-resize-image`)*

### 6. Launch the Application!
Start the app by running the main entry script:
```shell
python login.py
```

### Optional: Start with a Fresh Database
If you moved the folder but do not want to keep the old Employees/Users from the previous PC, simply delete `esc2.db` from the folder, and run:
```shell
python create_db.py
```
This will generate a fresh, blank slate database for your new computer.
