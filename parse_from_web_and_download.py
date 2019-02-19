from src import parse_pages
from src import download_pages as generator

if __name__ == '__main__':
    parse_pages(generator())
