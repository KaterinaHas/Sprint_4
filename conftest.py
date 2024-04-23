import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def book():
    book = BooksCollector()
    return book
