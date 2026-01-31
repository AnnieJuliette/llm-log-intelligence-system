from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    search_query = ""
    search_result = ""

    if request.method == "POST":
        search_query = request.form.get("query")

        # Simulated LLM interpretation
        if "500" in search_query:
            search_result = "23 entries found (HTTP 500 errors)"
        elif "suspicious" in search_query.lower():
            search_result = "LLM detected SQL injection & brute-force attempts"
        else:
            search_result = "No critical issues detected"

    data = {
        "total_logs": "1,000,000",
        "error_4xx": "12%",
        "error_5xx": "3%",
        "search_query": search_query,
        "search_result": search_result,
    }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
