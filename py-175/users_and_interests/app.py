from flask import Flask, render_template, g, redirect
import yaml

app = Flask(__name__)

@app.before_request
def load_users():
    with open('users.yaml', 'r') as file:
        data = yaml.safe_load(file)
    g.users = data

@app.route("/")
def index():
    return render_template('home.html', users=g.users, stats=total_interests())

@app.route("/users")
def users():
    """Added in to avoid 404 error if a user simply visits /users"""
    return redirect("/")

@app.route("/users/<name>")
def user(name):
    if name not in g.users:
        return redirect('/')
    
    other_users = {key: value for key, value in g.users.items() if key != name}
    return render_template('user.html', 
                           name=name.title(), 
                           details=g.users[name],
                           users=other_users,
                           stats=total_interests())

@app.template_filter('format_commas')
def format_commas(lst):
    return ", ".join([str(i).title() for i in lst])

@app.template_filter('capitalize')
def capitalize(text):
    return text.title()

def total_interests():
    num_users = len(g.users)
    num_interests = len([interest for value in g.users.values() for interest in value['interests']])
    return {"num_users": num_users, "num_interests": num_interests}

if __name__ == '__main__':
    app.run(debug=True, port=5003)