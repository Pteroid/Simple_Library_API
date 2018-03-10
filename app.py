import falcon
import json
import utils
from wsgiref import simple_server
import logging

logger = logging.getLogger(__name__)


class BooksResource:
    def on_get(self, req, resp):
        resp.body = json.dumps(utils.get_books())

    def on_post(self, req, resp):
        if req.content_length:
            data = json.load(req.stream)
            book = utils.put_book(**data)
            resp.body = json.dumps(book)
            resp.status = falcon.HTTP_201

    def on_delete(self, req, resp):
        utils.initialize()
        resp.status = falcon.HTTP_204


class BookResource:
    def on_get(self, req, resp, book_id):
        resp.body = json.dumps(utils.get_a_book(book_id))

    def on_delete(self, req, resp, book_id):
        utils.delete_a_book(book_id)
        resp.status = falcon.HTTP_204


class ReturningResource:
    def on_put(self, req, resp, book_id):
        if req.content_length:
            data = json.load(req.stream)
            utils.return_a_book(book_id, **data)
        else:
            utils.return_a_book(book_id)
        resp.status = falcon.HTTP_204

    def on_delete(self, req, resp, book_id):
        utils.return_a_book(book_id, cancel=True)
        resp.status = falcon.HTTP_204


app = falcon.API()

app.add_route('/books', BooksResource())
app.add_route('/books/{book_id:int}', BookResource())
app.add_route('/books/{book_id:int}/returning', ReturningResource())

if __name__ == '__main__':
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)
    httpd = simple_server.make_server('localhost', 8000, app)
    httpd.serve_forever()
