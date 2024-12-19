from app import app
from models import db, Book, Member

def seed_demo_data():
    with app.app_context():
        # Drop and recreate tables
        db.drop_all()
        db.create_all()

        # Add demo books
        demo_books = [
            Book(title="1984", author="George Orwell"),
            Book(title="To Kill a Mockingbird", author="Harper Lee"),
            Book(title="Pride and Prejudice", author="Jane Austen"),
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald"),
            Book(title="Moby Dick", author="Herman Melville"),
        ]
        db.session.add_all(demo_books)

        # Add demo members
        demo_members = [
            Member(name="Alice Johnson", email="alice@example.com"),
            Member(name="Bob Smith", email="bob@example.com"),
            Member(name="Charlie Brown", email="charlie@example.com"),
        ]
        db.session.add_all(demo_members)

        db.session.commit()
        print("Demo data seeded!")

if __name__ == "__main__":
    seed_demo_data()
