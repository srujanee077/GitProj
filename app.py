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
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

# @app.route('/mylibrary/books', methods=['GET'])
# def home():
#     return jsonify("Hello from Books")

# @app.route('/books', methods=['GET'])
# def api_all():
#     return jsonify(books)

