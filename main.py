import pathlib
from typing_extensions import Self


class Book:
    def __init__(self):
        self.frankenstein_book_fp = pathlib.Path('books/frankenstein.txt')

    def main(self) -> None:
        frankenstein = self.read_book(self.frankenstein_book_fp)

        print('Checking book:', self.frankenstein_book_fp.name)
        print('Total Words:', self.word_count(frankenstein))
        self.char_count(frankenstein)

    @staticmethod
    def read_book(fp: pathlib.Path) -> str:
        with open(fp, 'r', encoding='utf8') as f:
            return f.read()

    @staticmethod
    def word_count(book: str) -> int:
        return len(book.split())

    @staticmethod
    def char_count(book: str) -> list[dict]:
        def sort_on(dict):
            return dict['count']

        char_stats = {}
        char_meta = []
        book_lower = book.lower()

        for char in book_lower:
            if char == '\n':
                char = '\\n'

            if char in char_stats:
                char_stats[char] += 1
            else:
                char_stats[char] = 1

        for char, count in char_stats.items():
            char_meta.append({'char': char, 'count': count})

        char_meta.sort(reverse=True, key=sort_on)

        for entry in char_meta:
            print(f"The '{entry['char']}' character was found {entry['count']} times")

        return char_meta


if __name__ == '__main__':
    book = Book()
    book.main()

