# Write a function that takes a short line of text and prints it within a box.

def print_in_box(message):
    content_width = len(message) + 2 # 2 additional characters on either side
    
    top_bottom_border = "+" + "-" * content_width + "+"
    top_bottom_margin = "|" + " " * content_width + "|"
    message_line = "| " + message + " |"

    print(top_bottom_border)
    print(top_bottom_margin)
    print(message_line)
    print(top_bottom_margin)
    print(top_bottom_border)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')