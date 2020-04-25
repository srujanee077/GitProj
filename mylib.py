import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    ]

@app.route('/mylibrary/books', methods=['GET'])
def home():
    return jsonify("Hello from Books")

# @app.route('/books', methods=['GET'])
# def api_all():
#     return jsonify(books)

app.run()