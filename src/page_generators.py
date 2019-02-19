from time import sleep
import os
import requests

page_dir = 'pages'

def get_pages():
    # ygo_db_url + page_number
    ygo_db_url = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=1&keyword=&stype=1&ctype=&starfr=&starto=&pscalefr=&pscaleto=&linkmarkerfr=&linkmarkerto=&link_m=2&atkfr=&atkto=&deffr=&defto=&othercon=2&rp=100&page='

    page_number = 1

    while True:
        try:
            html = requests.get(ygo_db_url + str(page_number)).content.decode('utf-8')
        except requests.exceptions.ConnectionError as ex:
            print(ex)
            sleep(0.2)
            continue
        if '<!--.box_list-->' in html:
            yield html
            page_number += 1
            sleep(0.1)
        else:
            return

def download_pages():
    if not os.path.exists(page_dir):
        os.makedirs(page_dir)

    for i, html in enumerate(get_pages()):
        page = i+1
        print('Downloading page', page, '...', len(html.encode('utf-8')),'bytes')
        with open(os.path.join(page_dir, str(page)+'.html'), 'w') as f:
            f.write(html)
        yield html

def get_downloaded_pages():
    for html_file in os.listdir(page_dir):
        with open(os.path.join(page_dir, html_file)) as f:
            yield f.read()

