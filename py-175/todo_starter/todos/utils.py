def error_invalid_length(title):
    if len(title) < 1 or len(title) > 100:
        return 'The title must be between 1 and 100 characters.'
    return None

def error_for_list_title(title, lists):
    # Check for duplicate names
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."

    # Limit title based on length
    return error_invalid_length(title)

def find_list_by_id(list_id, lists):
    try:
        return next(lst for lst in lists if lst['id'] == list_id)
    except StopIteration:
        # No list exists with the ID passed in
        return None
    
def find_todo_by_id(todo_id, lst):
    try:
        return next(todo for todo in lst['todos'] if todo['id'] == todo_id)
    except StopIteration:
        return None
    
def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0

def is_todo_completed(todo):
    return todo['completed']
    
def mark_all_todos_complete(lst):
    for todo in lst['todos']:
        todo['completed'] = True
    
def mark_todo_complete(todo, completed):
    # Marks a to do as complete or not based on value of `completed` argument
    todo['completed'] = completed

def remove_todo(lst, todo):
    lst['todos'].remove(todo)

def remove_list(lst, lists):
    lists.remove(lst)

def sort_items(lists, sort_func):
    return sorted(lists, key=lambda lst: (sort_func(lst), lst['title'].lower()))

def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed'])

def update_list_title(title, lst):
    lst['title'] = title