from src import parse_pages
from src import get_downloaded_pages as generator

if __name__ == '__main__':
    try:
        parse_pages(generator())
    except FileNotFoundError:
        print('There are no downloaded pages.')
