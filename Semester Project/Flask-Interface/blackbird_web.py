from flask import Flask, request, render_template_string
from blackbird import run_blackbird_search                                   # must be place in the root directory

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Blackbird Search</h1>such a hassle
    <form action="/search" method="get">
        <label>Username: <input type="text" name="username"></label><br>
        <label>Email: <input type="text" name="email"></label><br>
        <input type="submit" value="Search">
    </form>
    """

@app.route('/search')
def search():
    username = request.args.get("username")
    email = request.args.get("email")

    # Call your blackbird search function
    results = run_blackbird_search(username=username, email=email)

    # Render results as a list
    html = """
    <h2>Search Results</h2>
    <ul>
    {% for account in results %}
        <li>{{ account['name'] }} - <a href="{{ account['url'] }}">{{ account['url'] }}</a> ({{ account['status'] }})</li>
    {% endfor %}
    </ul>
    <a href="/">Back</a>
    """
    return render_template_string(html, results=results)

if __name__ == "__main__":
    blackbird_web.run(debug=True)
