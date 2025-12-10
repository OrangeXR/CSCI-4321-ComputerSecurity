from flask import Flask, request, render_template
from blackbird import run_blackbird_search   # must be in root directory

app = Flask(__name__)

# Home page
@app.route("/")
def home_page():
    return render_template("HomePage.html")

@app.route('/search', methods=['POST', 'GET'])
def search():
    # Get inputs depending on method
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
    else:
        username = request.args.get("username")
        email = request.args.get("email")

    # Split comma-separated values into lists
    usernames = [u.strip() for u in username.split(",")] if username else []
    emails = [e.strip() for e in email.split(",")] if email else []

    results = []

    # Search by usernames
    for u in usernames:
        results.extend(run_blackbird_search(username=u, email=None))

    # Search by emails
    for e in emails:
        results.extend(run_blackbird_search(username=None, email=e))

    # Deduplicate results by URL (optional)
    unique = {acct['url']: acct for acct in results}
    results = list(unique.values())

    return render_template("Search.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)