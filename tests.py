from main import BooksCollector
import _pytest
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
    def test_add_new_book_length_more_40(self):
        collector = BooksCollector()
        collector.add_new_book('хххххххххххххххххххххххххххххххххххххххx')
        assert "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" not in collector.books_genre

    def test_add_new_book_length_is_0(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert "" not in collector.books_genre

    def test_add_new_book_add_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.books_genre

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ангелы и демоны')
        collector.set_book_genre('Ангелы и демоны', 'Ужасы')
        assert collector.get_book_genre('Ангелы и демоны') == 'Ужасы'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Ангелы и демоны')
        collector.set_book_genre('Ангелы и демоны', 'Роман')
        assert collector.get_book_genre('Ангелы и демоны') == ''

    def test_set_and_get_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ангелы и демоны')
        collector.set_book_genre('Ангелы и демоны', 'Ужасы')
        assert collector.get_book_genre('Ангелы и демоны') == 'Ужасы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ангелы и демоны')
        collector.set_book_genre('Ангелы и демоны', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Ангелы и демоны']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ангелы и демоны')
        assert collector.get_books_genre() == {'Ангелы и демоны': ''}

    def test_get_books_for_children_list_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Домовенок')
        collector.set_book_genre('Домовенок', 'Детективы')
        assert 'Домовенок' not in collector.get_books_for_children()

    def test_get_books_for_children_list_is_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Ангелы и демоны')
        collector.set_book_genre('Ангелы и демоны', 'Мультфильмы')
        assert 'Ангелы и демоны' in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ангелы и демоны')
        collector.add_book_in_favorites('Ангелы и демоны')
        assert 'Ангелы и демоны' in collector.get_list_of_favorites_books()

    def test_add_duplicate_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ангелы и демоны')
        collector.add_book_in_favorites('Ангелы и демоны')
        collector.add_book_in_favorites('Ангелы и демоны')
        assert collector.get_list_of_favorites_books().count('Ангелы и демоны') == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ангелы и демоны')
        collector.add_book_in_favorites('Ангелы и демоны')
        collector.delete_book_from_favorites('Ангелы и демоны')
        assert 'Ангелы и демоны' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('books, genre', [('Домовенок', 'Детективы'),
                                              ('Ангелы и демоны', 'Ужасы')])
    def test_get_list_of_favorites_books_have_books(self, books, genre):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.set_book_genre(books, genre)
        collector.add_book_in_favorites(books)
        assert books in collector.get_list_of_favorites_books()

