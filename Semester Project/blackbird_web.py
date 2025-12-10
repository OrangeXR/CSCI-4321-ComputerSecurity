from flask import Flask, request, render_template
from blackbird import run_blackbird_search                                   # must be place in the root directory


#For home page 
app = Flask(__name__)
@app.route("/")
def home_page():
    return render_template("HomePage.html")

@app.route('/search', methods=['POST', 'GET'])
def search():
    username = None
    email = None
    results = []
    
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
    elif request.method == 'GET':
        username = request.args.get("username")
        email = request.args.get("email")
    if username and email:
        results = run_blackbird_search(username=username, email=email)

    return render_template("Search.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

