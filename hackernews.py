# https://hacker-news.firebaseio.com/v0/item/15318128.json?print=pretty
# https://news.ycombinator.com/item?id=15318128

import requests
# from pprint import pprint as pp
import json
from bs4 import BeautifulSoup
import html2text

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class HackerNews(object):
    def __init__(self):
        self.host = 'https://hacker-news.firebaseio.com'
        self.session = requests.Session()
        # self.head = header
        self.head = {}

    def get_item(self,item_id):
        url = '{}/{}/{}/{}.json'.format(self.host,'v0','item',item_id)
        r = requests.request("GET",url,headers=self.head)
        if r.status_code == requests.codes.ok:
           return r.json()
        else:
            print(r.text)
    
    def clean_text(self,html_text):
        # get rid of <i> and <p> and encodings like Quigley&#x27;s
        # return BeautifulSoup(text, "lxml").prettify()
        return html2text.html2text(html_text)