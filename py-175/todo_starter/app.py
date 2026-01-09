from uuid import uuid4
from functools import wraps
from flask import flash, Flask, redirect, render_template, request, session, url_for
from todos.utils import (
    error_for_list_title, 
    error_invalid_length, 
    find_list_by_id, 
    find_todo_by_id,
    is_list_completed,
    is_todo_completed,
    mark_all_todos_complete, 
    mark_todo_complete,
    remove_list,
    remove_todo,
    sort_items,
    todos_remaining,
    update_list_title
)
from werkzeug.exceptions import NotFound
import os

app = Flask(__name__)
app.secret_key = 'secret1'

def require_list(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        list_id = kwargs.get('list_id')
        selected_list = find_list_by_id(list_id, session['lists'])
        if not selected_list:
            raise NotFound(description="List not found.")
        return f(selected_list=selected_list, *args, **kwargs)
    return decorated_function

def require_todo(f):
    @wraps(f)
    @require_list
    def decorated_function(selected_list, *args, **kwargs):
        todo_id = kwargs.get('todo_id')
        selected_todo = find_todo_by_id(todo_id, selected_list)
        if not selected_todo:
            raise NotFound(description="Todo not found.")
        return f(selected_list=selected_list, selected_todo=selected_todo, *args, **kwargs)
    return decorated_function

@app.context_processor
def list_utilities_processor():
    return dict(
        is_list_completed=is_list_completed,
    )

@app.before_request
def initialize_session():
    if 'lists' not in session:
        session['lists'] = []

@app.route("/")
def index():
    return redirect(url_for('get_lists'))

@app.route("/lists/new")
def add_todo_list():
    return render_template("new_list.html")

@app.route("/lists")
def get_lists():
    # lists = [
    #     {"title": "Lunch Groceries", "todos": []},
    #     {"title": "Dinner Groceries", "todos": []},
    # ]
    lists = sort_items(session['lists'], is_list_completed)
    return render_template("lists.html", lists=lists, todos_remaining=todos_remaining)

@app.route("/lists", methods=['POST'])
def create_list():
    title = request.form["list-title"].strip()

    error = error_for_list_title(title, session['lists'])
    if error:
        flash(error, "error")
        return render_template('new_list.html', title=title)
    
    session['lists'].append({
        'id': str(uuid4()),
        'title': title, 
        'todos': [],
    })
    flash("The list has been created.", "success")
    session.modified = True
    return redirect(url_for('get_lists'))

@app.route("/lists/<list_id>")
@require_list
def show_list(selected_list, list_id):
    selected_list['todos'] = sort_items(selected_list['todos'], is_todo_completed)
    return render_template('list.html', lst=selected_list)

@app.route("/lists/<list_id>", methods=['POST'])
@require_list
def edit_list_title(selected_list, list_id):
    title = request.form['list_title'].strip()

    error = error_for_list_title(title, session['lists'])
    if error:
        flash(error, "error")
        return render_template('edit_list.html', 
                               lst=selected_list, 
                               title=title if title else selected_list['title'])
    
    # Separate out mutation logic from Flask logic
    update_list_title(title, selected_list)

    flash("List successfully updated.", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/todos", methods=['POST'])
@require_list
def create_todo(selected_list, list_id):
    title = request.form['todo'].strip()

    error = error_invalid_length(title)
    if error:
        flash(error, "error")
        return render_template('list.html', lst=selected_list)
    
    selected_list['todos'].append({
        'id': str(uuid4()),
        'completed': False,
        'title': title
    })

    flash("To do successfully created.", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/todos/<todo_id>/toggle", methods=['POST'])
@require_todo
def toggle_complete(selected_list, selected_todo, list_id, todo_id):
    completed = request.form['completed'] == 'True'

    # Separate out mutation logic from Flask logic
    mark_todo_complete(selected_todo, completed)

    flash("To do completion status changed.", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/todos/<todo_id>/delete", methods=['POST'])
@require_todo
def delete_todo(selected_list, selected_todo, list_id, todo_id):
    # Separate out mutation logic from Flask logic
    remove_todo(selected_list, selected_todo)

    flash("To do deleted.", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/complete_all", methods=['POST'])
@require_list
def complete_all_todos(selected_list, list_id):
    # Separate out mutation logic from Flask logic
    mark_all_todos_complete(selected_list)
    
    flash("All to dos marked complete.", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/edit")
@require_list
def edit_list(selected_list, list_id):
    return render_template('edit_list.html', lst=selected_list)

@app.route("/lists/<list_id>/delete", methods=['POST'])
@require_list
def delete_list(selected_list, list_id):
    # Separate out mutation logic from Flask logic
    remove_list(selected_list, session['lists'])

    flash("To do list removed.", "success")
    session.modified = True
    return redirect(url_for('get_lists'))

if __name__ == "__main__":
    if os.environ.get('FLASK_ENV') == 'production':
        app.run(debug=False)
    else:
        app.run(debug=True, port=5003)