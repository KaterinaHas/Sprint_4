import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book_is_true(self, book):
        book.add_new_book('Анна Каренина')
        assert len(book.get_books_genre()) == 1

    name = [
        'Анна Каренина',
        'Рассвет полночи, или Созерцание славы, торжества и мудрости порфироносных',
        ''
    ]

    @pytest.mark.parametrize('name', name)
    def test_add_new_book_not_add_book(self, book, name):
        book.add_new_book('Анна Каренина')
        book.add_new_book(name)
        assert len(book.get_books_genre()) == 1

    def test_set_book_genre_set_one_genre(self, book):
        book.add_new_book('Анна Каренина')
        book.set_book_genre('Анна Каренина', 'Фантастика')
        assert book.books_genre['Анна Каренина'] == 'Фантастика'

    def test_set_book_genre_not_genre_in_list_not_set_genre(self, book):
        book.add_new_book('Анна Каренина')
        book.set_book_genre('Анна Каренина', 'Триллер')
        assert book.books_genre['Анна Каренина'] == ''

    def test_get_book_genre_name_in_list_is_true(self, book):
        book.add_new_book('Анна Каренина')
        book.set_book_genre('Анна Каренина', 'Фантастика')
        assert book.get_book_genre('Анна Каренина') == 'Фантастика'

    def test_get_books_with_specific_genre_genre_in_list(self, book):
        book.add_new_book('Анна Каренина')
        book.set_book_genre('Анна Каренина', 'Фантастика')
        assert book.get_books_with_specific_genre('Фантастика') == ['Анна Каренина']

    def test_get_books_genre(self, book):
        book.add_new_book('Анна Каренина')
        book.set_book_genre('Анна Каренина', 'Фантастика')
        assert book.get_books_genre() == {'Анна Каренина': 'Фантастика'}

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Незнайка', 'Фантастика'],
            ['Буратино', 'Мультфильмы'],
            ['Смешарики', 'Комедии']
        ])
    def test_get_books_for_children_book_for_children_is_true(self, book, name, genre):
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_books_for_children() == [name]

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Семейка Адамс', 'Ужасы'],
            ['13-ая комната', 'Детективы']
        ])
    def test_get_books_for_children_book_not_for_children_is_true(self, book, name, genre):
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_books_for_children() == []

    def test_add_book_in_favorites_add_one_book(self, book):
        book.add_new_book('Анна Каренина')
        book.add_book_in_favorites('Анна Каренина')
        assert book.favorites == ['Анна Каренина']

    def test_delete_book_from_favorites_delete_one_book(self, book):
        book.add_new_book('Анна Каренина')
        book.add_book_in_favorites('Анна Каренина')
        book.delete_book_from_favorites('Анна Каренина')
        assert book.favorites == []

    def test_get_list_of_favorites_books_list_not_empty(self, book):
        book.add_new_book('Анна Каренина')
        book.add_book_in_favorites('Анна Каренина')
        assert book.get_list_of_favorites_books() == ['Анна Каренина']
