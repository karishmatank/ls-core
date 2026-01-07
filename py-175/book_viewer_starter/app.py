from flask import Flask, render_template, g, redirect, request
from markupsafe import Markup

app = Flask(__name__)

@app.before_request
def load_contents():
    """Loads table of contents data before each request"""
    with open("book_viewer/data/toc.txt", "r") as file:
        g.contents = file.readlines()

def split_paragraphs(text):
    paragraphs = text.split("\n\n")
    return paragraphs

@app.template_filter('in_paragraphs')
def in_paragraphs(text):
    # By default, Jinja escapes output such that malicious HTML can't run, to avoid XSS attacks
    # Jinja's recommendation is to use Markup from markupsafe, which is a dependency of Flask so no need to install separately
    # but we can also include '| safe' in the tag instead within the template, i.e. {{ ch_contents | in_paragraphs | safe }}
    paragraphs = split_paragraphs(text)
    paragraphs = [f"<p id='p{idx}'>" + paragraph + "</p>" for idx, paragraph in enumerate(paragraphs, start=1)]
    return Markup("".join(paragraphs))

@app.route("/")
def index():
    # with open("templates/index.html", "r") as file:
    #     return file.read()

    return render_template('home.html', contents=g.contents)

@app.route("/chapters/<int:ch_num>")
def chapter_contents(ch_num):
    if (1 <= int(ch_num) <= len(g.contents)):
        chapter_name = g.contents[int(ch_num) - 1]
        chapter_title = f"Chapter {ch_num}: {chapter_name}"

        with open(f"book_viewer/data/chp{ch_num}.txt", 'r') as file:
            ch_contents = file.read()
        
        return render_template('chapter.html', ch_title=chapter_title, ch_contents=ch_contents, contents=g.contents)
    else:
        return redirect("/")

@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors gracefully by redirecting the user"""
    return redirect('/')

@app.template_filter('highlight_query')
def highlight_query(text, query):
    # Split apart text by the query string. This will create a list of substrings
    # EDIT: Could have just used the replace method for strings...
    substrings = text.split(query)
    return Markup(f"<strong>{query}</strong>".join(substrings))

@app.route("/search")
def search():
    query = request.args.get('query', '')
    if query:
        # Look for which chapters the query text is in
        chapters = []
        for ch_num, chapter in enumerate(g.contents, start=1):
            # Get text
            with open(f"book_viewer/data/chp{ch_num}.txt", 'r') as file:
                ch_contents = file.read()

            paragraph_matches = [{'p_num': idx, 'p_text': paragraph}
                                 for idx, paragraph in enumerate(split_paragraphs(ch_contents), start=1)
                                 if query.lower() in paragraph.lower()]

            if paragraph_matches:
                chapters.append({
                    'ch_num': ch_num,
                    'ch_name': chapter,
                    'p_matches': paragraph_matches
                })
        
        return render_template('search.html', query=query, contents=g.contents, results=chapters)

    return render_template('search.html', query=query, contents=g.contents)

if __name__ == "__main__":
    app.run(debug=True, port=5003)