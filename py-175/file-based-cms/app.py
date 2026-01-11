from flask import flash, Flask, redirect, render_template, send_from_directory, request, session, url_for
import os
from markdown import markdown
from functools import wraps
from yaml import safe_load
import bcrypt

app = Flask(__name__)
app.secret_key='secret1'

def load_user_credentials():
    filename = 'users.yml'
    root = os.path.abspath(os.path.dirname(__file__))
    if app.config['TESTING']:
        credentials_path = os.path.join(root, 'tests', filename)
    else:
        credentials_path = os.path.join(root, 'cms', filename)

    with open(credentials_path, 'r') as file:
        return safe_load(file)
    
def is_valid_credential(username, password):
    credentials = load_user_credentials()

    if username in credentials:
        hashed_password = credentials[username].encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    
    return False

def get_data_path():
    root = os.path.abspath(os.path.dirname(__file__))
    if app.config['TESTING']:
        return os.path.join(root, 'tests', 'data')
    else:
        return os.path.join(root, 'cms', 'data')
    
def is_existing_file(file_name):
    data_dir = get_data_path()
    files_list = os.listdir(data_dir)
    return file_name in files_list

def is_md_file(file_name):
    ext = file_name.split(".")[-1]
    return ext == 'md'

def get_file_path(*args):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, *args)
    return file_path

def reset_credentials():
    session['is_signed_in'] = False
    if 'username' in session:
        del session['username']

def is_user_signed_in():
    return session.get('is_signed_in') and 'username' in session

def sign_in_decorator(func):
    """Check if user is signed in"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_user_signed_in():
            return func(*args, **kwargs)
        flash("You must be signed in to do that.", "warning")
        return redirect(url_for('sign_in'))
    return wrapper


@app.route('/')
def index():
    """Display files in the filesystem"""
    # Original version- too simplistic
    # return render_template('index.html', files=os.listdir('cms/data'))

    data_dir = get_data_path()
    return render_template('index.html', files=os.listdir(data_dir))
    

@app.route('/<file_name>')
def view_contents(file_name):
    # Handle files not in the CMS
    if not is_existing_file(file_name):
        flash(f"{file_name} does not exist.", "warning")
        return redirect(url_for('index'))
    
    # Handle Markdown files
    # send_from_directory skips straight to building the Response, which means we can't pass it into markdown
    # So we'll get the content manually
    if is_md_file(file_name):
        file_path = get_file_path(file_name)
        with open(file_path, 'r') as f:
            contents = f.read()
        return render_template('view_markdown.html', content=markdown(contents))

    # Original version
    # file_path = os.path.join(data_dir, file_name)
    # with open(file_path, 'r') as f:
    #     contents = f.read()
    # return render_template('file_contents.html', contents=contents) # <-- Got rid of template, don't need it for now

    return send_from_directory(get_data_path(), file_name)

@app.route("/<file_name>/edit")
@sign_in_decorator
def edit_contents(file_name):
    # Handle files not in the CMS
    if not is_existing_file(file_name):
        flash(f"{file_name} does not exist.", "warning")
        return redirect(url_for('index'))
    
    # Get file contents
    file_path = get_file_path(file_name)
    with open(file_path, 'r') as f:
        contents = f.read()

    return render_template('edit.html', file_name=file_name, contents=contents)

@app.route("/<file_name>", methods=['POST'])
@sign_in_decorator
def save_contents(file_name):
    new_contents = request.form['contents'].strip()

    # Handle files not in the CMS
    if not is_existing_file(file_name):
        flash(f"{file_name} does not exist.", "warning")
        return redirect(url_for('index'))
    
    # Write new file contents
    file_path = get_file_path(file_name)
    with open(file_path, 'w') as f:
        f.write(new_contents)
    
    flash(f"{file_name} has been edited.", "success")
    return redirect(url_for('index'))

@app.route("/new", methods=['GET', 'POST'])
@sign_in_decorator
def create_document():
    if request.method == 'POST':
        # Validate name of document
        title = request.form['new-title'].strip()

        if not title:
            flash("A name is required.", "warning")
            return render_template('new.html'), 422
        
        # Handle case where name matches an existing name
        if is_existing_file(title):
            flash(f"{title} already exists.", "warning")
            return render_template('new.html', title=title), 422
        
        # Create file
        file = open(get_file_path(title), 'w')
        file.close()

        flash(f"{title} has been created.", "success")
        return redirect(url_for('index'))

    return render_template('new.html')

@app.route("/<file_name>/delete", methods=['POST'])
@sign_in_decorator
def delete_document(file_name):
    # Handle files not in the CMS
    if not is_existing_file(file_name):
        flash(f"{file_name} does not exist.", "warning")
        return redirect(url_for('index'))
    
    file_path = get_file_path(file_name)
    os.remove(file_path)

    flash(f"{file_name} has been deleted.", "success")
    return redirect(url_for('index'))

@app.route("/users/signin")
def sign_in():
    return render_template('sign_in.html')

@app.route("/users/validate", methods=['POST'])
def validate_login():
    username = request.form['username']
    password = request.form['password']

    if is_valid_credential(username, password):
        session['is_signed_in'] = True
        session['username'] = username
        flash("Welcome!", "success")
        return redirect(url_for('index'))
    
    flash('Invalid credentials', "warning")
    return render_template('sign_in.html', username=username), 422

@app.route("/users/signout", methods=['POST'])
def sign_out():
    reset_credentials()
    flash("You have been signed out.", "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5003)