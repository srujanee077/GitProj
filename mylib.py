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
[{
         'name':'Harry Potter',
        'author':'J.K.Rowling',
        'publisher':'Bloomsbury',
        'price':600,
        'published':2000,
        'ISBN Code':446310785,
              },
      {
         'name':'To Kill a Mockingbird',
        'author':'Harper Lee Read',
        'publisher':'J. B. Lippincott & Co.',
        'price':500,
        'published':1960,
        'ISBN Code':446310786},

     {
        'name':'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'publisher': 'J. B. Lippincott & Co.',
        'price': 500,
        'published': 1992,
        'ISBN Code':446310788},
    {
        'name':'Ancillary Justice',
        'author': 'Ann Leckie',
        'publisher': 'Dzanc Books (Detroit, MI)',
        'price': 800,
        'published': 2014,
        'ISBN Code':446310710
    },
  {
    'name':'The Yiddish Policemen Union1',
    'author': 'Michael Chabon',
    'publisher': 'Rare Bird Books (Los Angeles, CA)',
    'price': 300,
    'published': 2008,
    'ISBN Code': 446310717
  }
]

@app.route('/mylibrary/books', methods=['GET'])
def home():
    return jsonify("Hello from Books")

# @app.route('/books', methods=['GET'])
# def api_all():
#     return jsonify(books)

app.run()