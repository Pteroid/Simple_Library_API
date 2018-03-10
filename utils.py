from tinydb import TinyDB, Query
from tinydb.operations import increment, delete
from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)

db = TinyDB("db.json")
books = db.table("books")
seq = db.table("sequences")

Book = Query()

EXPRESSION = '%Y-%m-%d'


def next_id(name='books'):
    doc_ids = seq.update(increment('current_number'), next_id.Sequence.name == name)
    return seq.get(doc_id=doc_ids[0])['current_number']


next_id.Sequence = Query()


def initialize():
    books.purge()
    seq.purge()

    books.insert({'borrower': '田中 太郎',
                  'borrowed_date': '2017-01-12',
                  'id': 1,
                  'returned_date': '2017-01-24',
                  'title': '松浦さよ姫伝説の基礎的研究 近・現代編'})
    seq.insert({'name': 'books', 'current_number': 1})


def get_books():
    return books.all()


def get_a_book(book_id):
    return books.search(Book.id == book_id)[0]


def delete_a_book(book_id):
    books.remove(Book.id == book_id)


def put_book(title, borrower, borrowed_date=None):
    if not borrowed_date:
        borrowed_date = datetime.now().strftime(EXPRESSION)

    book = {
        'borrower': borrower,
        'borrowed_date': borrowed_date,
        'id': next_id(),
        'title': title
    }

    books.insert(book)

    return book


def return_a_book(book_id, returned_date=None, cancel=False):
    if cancel:
        books.update(delete('returned_date'), Book.id == book_id)

    if not returned_date:
        returned_date = datetime.now().strftime(EXPRESSION)

    books.update({'returned_date': returned_date}, Book.id == book_id)
