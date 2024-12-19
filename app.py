from flask import Flask, request, jsonify
from models import db, Book, Member
from auth import token_required
from utils import paginate_query

app = Flask(__name__)
app.config.from_object('instance.config.Config')
db.init_app(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Library Management System API!"})


@app.route('/books', methods=['GET', 'POST'])
@token_required
def handle_books(current_user):
    if request.method == 'GET':
        search = request.args.get('search')
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)

        query = Book.query
        if search:
            query = query.filter((Book.title.ilike(f"%{search}%")) | (Book.author.ilike(f"%{search}%")))

        books = paginate_query(query, page, per_page)
        return jsonify([book.to_dict() for book in books])
    elif request.method == 'POST':
        data = request.json
        new_book = Book(title=data['title'], author=data['author'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@token_required
def handle_book(current_user, id):
    book = Book.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(book.to_dict())
    elif request.method == 'PUT':
        data = request.json
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        db.session.commit()
        return jsonify(book.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        return '', 204

@app.route('/members', methods=['GET', 'POST'])
@token_required
def handle_members(current_user):
    if request.method == 'GET':
        members = Member.query.all()
        return jsonify([member.to_dict() for member in members])
    elif request.method == 'POST':
        data = request.json
        new_member = Member(name=data['name'], email=data['email'])
        db.session.add(new_member)
        db.session.commit()
        return jsonify(new_member.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
