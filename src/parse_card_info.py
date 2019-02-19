from bs4 import BeautifulSoup, element as box_list_element
from .page_generators import get_pages, download_pages, page_dir
import json


class Card():
    def __init__(self, card: box_list_element):
        self.name = card.find(class_='box_card_name').get_text().strip()
        self.text = card.find(class_='box_card_text').get_text().strip()

        self.pendulum_text = card.find(class_='box_card_pen_effect')
        if self.pendulum_text:
            self.pendulum_text = self.pendulum_text.get_text().strip()
        else:
            self.pendulum_text = ''

        self.ygo_db_url = 'https://www.db.yugioh-card.com'+card.find(class_='link_value').get('value')

    def get_word_count(self):
        return len(self.text.split()) + len(self.pendulum_text.split())

    def __iter__(self):
       yield 'url', self.ygo_db_url
       yield 'name', self.name
       yield 'text', self.text
       yield 'pendulum_text', self.pendulum_text
       yield 'word_count', self.get_word_count()


def parse_pages(generator):
    out_file = 'output.json'
    list_json = []
    for p in generator:
        soup = BeautifulSoup(p, 'html.parser')

        for card in soup.find(class_='box_list').find_all('li'):
            c = Card(card)
            list_json.append(dict(c))
            print('"'+c.name+'" card text parsed')

    print('Saving card text word count info to', out_file)
    with open(out_file, 'w') as f:
        json.dump(list_json, f)

