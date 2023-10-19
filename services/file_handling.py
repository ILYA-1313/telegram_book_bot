#модуль для подготовки книги, чтобы боту было удобно
#c ней работать.


import os
import sys



BOOK_PATH ="book/Bredberi_Marsianskie-hroniki.txt" #"D:\\Илья\\Портфолео\\Python\\Учебные проекты\\stepik\\Телеграм-боты на Python и AIOgram\\9.5.book_bot\\book\\book.txt" #путь к файлу книги
PAGE_SIZE=1050 #максимальное количество букв для одной страницы(для каждого телефона своя)



book: dict[int, str] = {}


#Функция, возвращающая строку с текстом страницы и её размер
def _get_part_text(text: str, start: int, PAGE_SIZE: int) -> tuple[str, int]:
    end = min(start + PAGE_SIZE, len(text))
    for finally_len in range(end, start, -1):
        if text[end - 1] in ",.!:;?" and text[end - 2] in ",.!:;?":
            if text[finally_len - 1] in (" " or "\n") and text[finally_len - 2] in ",.!:;?" and text[
                finally_len - 3] not in ",.!:;?":
                break
        elif text[finally_len - 1] in ",.!:;?" and text[finally_len - 2] not in ",.!:;?" and (text == " " or "\n"):
            break
        else:
            finally_len = end

    page = text[start:finally_len].rstrip()
    return page, len(page)
    #pass


#Функция, формирующая словарь книги
def prepare_book(path: str) -> None:#path - путь к файлу книги. Функция принимает аргумент - путь к файлу
    with open(path, 'rt', encoding="utf-8") as file:
        text = file.read()
        start, page_number = 0, 1
        while start < len(text):
            page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
            start += page_size
            book[page_number] = page_text.strip()
            page_number += 1

    # book_open = open(path, "rt", encoding='utf-8')  # открываем текстовый файл книги
    # book_read = book_open.read()  # читаем файл
    # _get_part_text(book_read, 0, PAGE_SIZE)  # преобразуем текст в словарь. ключ - номер странцы, значение - текст страницы
    # book_open.close()  # закрываем текстовый файл книги
    # # pass


#Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))

