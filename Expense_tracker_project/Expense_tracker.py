from flask import Flask, render_template, request, redirect, url_for, flash, session
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For session management

class ExpenseTracker:
    def __init__(self, username):
        self.username = username
        self.expenses = pd.DataFrame(columns=["Date", "Description", "Quantity", "Price per Unit", "Total Amount"])
        self.csv_file = "expenses_data.csv"
        self.load_expenses()

    def initialize_csv(self):
        # Create an empty CSV file with the necessary columns
        df = pd.DataFrame(columns=["Username", "Date", "Description", "Quantity", "Price per Unit", "Total Amount"])
        df.to_csv(self.csv_file, index=False)

    def load_expenses(self):
        if os.path.exists(self.csv_file):
            df = pd.read_csv(self.csv_file)
            user_expenses = df[df["Username"] == self.username]
            self.expenses = user_expenses.drop(columns=["Username"])
        else:
            self.initialize_csv()

    def save_expenses(self):
        if os.path.exists(self.csv_file):
            df = pd.read_csv(self.csv_file)
            # Remove current user's data
            df = df[df["Username"] != self.username]
        else:
            df = pd.DataFrame(columns=["Username", "Date", "Description", "Quantity", "Price per Unit", "Total Amount"])

        # Append current user's data
        user_data = self.expenses.copy()
        user_data["Username"] = self.username
        df = pd.concat([df, user_data], ignore_index=True)

        # Save to CSV
        df.to_csv(self.csv_file, index=False)

    def add_expense(self, date, description, quantity, price):
        total_amount = quantity * price
        new_expense = {
            "Date": date,
            "Description": description,
            "Quantity": quantity,
            "Price per Unit": price,
            "Total Amount": total_amount,
        }
        self.expenses = pd.concat([self.expenses, pd.DataFrame([new_expense])], ignore_index=True)
        self.save_expenses()

    def delete_expense(self, date):
        self.expenses = self.expenses[self.expenses["Date"] != date]
        self.save_expenses()

    def get_total_expenses(self):
        return self.expenses["Total Amount"].sum()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        if not username:
            flash("Please enter a valid username.", "error")
            return redirect(url_for("login"))
        session["username"] = username
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/home", methods=["GET"])
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    
    return render_template("home.html", username=session["username"])

@app.route("/add_expense", methods=["GET", "POST"])
def add_expense():
    if "username" not in session:
        return redirect(url_for("login"))
    
    tracker = ExpenseTracker(session["username"])

    if request.method == "POST":
        try:
            date = request.form["date"]
            description = request.form["description"]
            quantity = float(request.form["quantity"])
            price = float(request.form["price"])
            tracker.add_expense(date, description, quantity, price)
            flash("Expense added successfully!", "success")
        except ValueError:
            flash("Please enter valid numerical values for quantity and price.", "error")

    return render_template("add_expense.html", username=session["username"])

@app.route("/expenses")
def expenses():
    if "username" not in session:
        return redirect(url_for("login"))

    tracker = ExpenseTracker(session["username"])
    total = tracker.get_total_expenses()

    # Group expenses by date
    grouped_expenses = {}
    for _, row in tracker.expenses.iterrows():
        date = row["Date"]
        if date not in grouped_expenses:
            grouped_expenses[date] = []
        grouped_expenses[date].append({
            "desc": row["Description"],
            "qty": row["Quantity"],
            "price": row["Price per Unit"],
            "total": row["Total Amount"]
        })

    return render_template("expenses.html", expenses=grouped_expenses, total=total)

@app.route("/delete_expense", methods=["GET", "POST"])
def delete_expense():
    if "username" not in session:
        return redirect(url_for("login"))

    tracker = ExpenseTracker(session["username"])

    # Group expenses by date for rendering
    grouped_expenses = {}
    for _, row in tracker.expenses.iterrows():
        date = row["Date"]
        if date not in grouped_expenses:
            grouped_expenses[date] = []
        grouped_expenses[date].append({
            "desc": row["Description"],
            "qty": row["Quantity"],
            "price": row["Price per Unit"],
            "total": row["Total Amount"]
        })

    if request.method == "POST":
        date = request.form["date"]
        tracker.delete_expense(date)
        flash(f"All expenses for {date} have been deleted successfully!", "success")

    return render_template(
        "delete_expense.html", expenses=grouped_expenses, username=session["username"]
    )

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
