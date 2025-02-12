1. test_add_new_book_invalid_length_more_40	Проверка невозможности добавления имени книги длиной более 40 символов
2. test_add_new_book_invalid_length_is_0	    Проверка невозможности добавления имени книги длиной 0 символов
3. test_add_new_add_same_book	              Проверка невозможности добавления уже добавленной книги 
4. test_set_book_genre	                      Проверка установки жанра для книги и правильное получение этого жанра.
5. test_set_book_genre_invalid	              Проверка, что при установке неподдерживаемого жанра для книги не изменяет её жанр.
6. test_set_and_get_genre	                  Проверка установки и получения жанра для книги.
7. test_get_books_with_ specific _genre	    Проверка, что метод возвращает книги с указанным жанром.
8. test_get_books_genre	                    Проверка правильного получения словаря всех книг с их жанрами.
9. test_get_books_for_children_list_is_empty	Проверка, что метод правильно не возвращает книги, неподходящие для детей.
10. test_get_books_for_children_list_is_not_empty	Проверяет, что метод правильно возвращает книги, подходящие для детей.
11. test_add_book_in_favorites	                Проверка возможности добавления книги в избранные.
12. test_add_duplicate_book_in_favorites	      Проверка невозможности добавления книги в избранное повторно
13. test_delete_book_from_favorites	            Проверяет возможность удаления книги из списка избранных.
14. test_get_list_of_favorites_books_have_books	Проверка вывода списка избранных книг
