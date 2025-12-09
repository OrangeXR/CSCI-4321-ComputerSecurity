from flask import Flask, request, render_template
from blackbird import run_blackbird_search                                   # must be place in the root directory


#For home page 
app = Flask(__name__)
@app.route("/")
def home_page():
    return render_template("HomePage.html")

#@app.route('/')
#def home():
 #   return """
  ## <form action="/search" method="get">
    #    <label>Username: <input type="text" name="username"></label><br>
     #   <label>Email: <input type="text" name="email"></label><br>
      #  <input type="submit" value="Search">
    #</form>
    #"""

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


    # Render results as a list
    #html = """
   # <h2>Search Results</h2>
    #<ul>
   # {% for account in results %}
   #     <li>{{ account['name'] }} - <a href="{{ account['url'] }}">{{ account['url'] }}</a> ({{ account['status'] }})</li>
   # {% endfor %}
   # </ul>
   # <a href="/">Back</a>
   # """
    return render_template("Search.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
