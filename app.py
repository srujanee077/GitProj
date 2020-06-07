import flask
from flask import request, jsonify, url_for,redirect
from werkzeug.exceptions import abort

app = flask.Flask(__name__)
books = [
    {'id': "0",
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': "1",
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': "2",
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/books/all',methods=['GET'])
def getallBooks():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
   book = request.get_json()
   books.append(book)
   return {'id': len(books)}, 200


@app.route('/books/<bookID>',methods=['GET'])
def getBook(bookID):
    bookByID = [ book for book in books if (book['id'] == bookID) ]
    return jsonify({'book':bookByID})

@app.route('/books/<int:bookID>',methods=['PUT'])
def updateBook(bookID):
    book = request.get_json()
    books[bookID] = book
    return jsonify(books[bookID]),200

@app.route('/books/<int:bookID>',methods=['DELETE'])
def deleteBook(bookID):
    books.pop(bookID)
    return 'None', 200

#run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)