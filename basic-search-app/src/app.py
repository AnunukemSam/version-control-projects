from flask import Flask, request, render_template

app = Flask(__name__)

# Predefined list of items to search
ITEMS = ["apple", "banana", "cherry", "date", "grape", "kiwi"]

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# Search route
@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")  # Get the search input from the form
    results = [item for item in ITEMS if query.lower() in item.lower()]  # Case-insensitive search
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

