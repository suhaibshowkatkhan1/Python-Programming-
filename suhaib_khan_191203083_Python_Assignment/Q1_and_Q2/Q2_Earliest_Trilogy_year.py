from typing import List, Optional


def trilogy_year(titles: List[str], years: List[int]) -> Optional[int]:
    books = {}
    for title, year in zip(titles, years):
        if year in books:
            books[year].append(title)
        else:
            books[year] = [title]

    for year in sorted(books.keys()):
        if year + 1 in books and year + 2 in books:
            return year
    return None


titles = ['The Hunger Games', 'Catching Fire', 'Mockingjay', 'The Lord of the Rings', 'The Two Towers', 'The Return of the King', 'Divergent', 'Insurgent', 'Allegiant']
years = [2008, 2009, 2010, 1954, 1955, 1956, 2011, 2012, 2013]

trilogy_year(titles, years)
