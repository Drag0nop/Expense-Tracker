# Flask Expense Tracker

This project is a Flask-based **Expense Tracker** application that helps users manage their personal finances. Users can log in, add, delete, and view their expenses. It includes secure login and logout functionality for user authentication.

---

## Features

- **Add Expense:** Input expense details such as amount, category, and description.
- **Delete Expense:** Remove expenses easily from the list.
- **View Expenses:** See all expenses in a clean, organized layout.
- **User Authentication:** Secure login and logout functionality.

---

## Prerequisites

To run this project, you'll need:
- Python 3.x
- Flask and its dependencies (install via `requirements.txt`)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   
2. Navigate to the project directory:
   '''bash
  cd expense-tracker
3. (Optional) Create a virtual environment:
   '''bash
  python -m venv venv

4. Activate the virtual environment:
    On Windows:
    '''bash
        venv\Scripts\activate
    On macOS/Linux:
    '''bash
       source venv/bin/activate

5. Install the dependencies:
   '''bash
    pip install -r requirements.txt

## Usage

Start the Flask application:
'''bash
python app.py

Open your browser and navigate to:
'''arduino
http://127.0.0.1:5000

Use the application to:

Log in with your credentials.
Add expenses with details such as amount and description.
View and delete expenses as needed.
Log out securely when finished.

## Project structure

Expense_Tracker/
├── static/                  # Static files for styling, images, and interactivity
│   ├── login.css            # Styles for login page
│   ├── home.css             # Styles for home page
│   ├── add.css              # Styles for add expense page
│   ├── delete.css           # Styles for delete expense page
│   ├── expense.css          # Styles for viewing expenses
│   ├── expense.webp         # Image asset
│   ├── image_hd.webp        # Image asset
│   └── script.js            # JavaScript file for client-side interactivity
├── templates/               # HTML templates for rendering pages
│   ├── login.html           # Login page
│   ├── home.html            # Home/dashboard page
│   ├── add.html             # Add expense page
│   ├── delete.html          # Delete expense page
│   └── expense.html         # View expenses page
├── expense_tracker.py       # Main Flask application file
└── README.md                # Project documentation
