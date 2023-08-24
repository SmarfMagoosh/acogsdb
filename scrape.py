#12:20am
from bs4 import BeautifulSoup as bs
from requests import get
from json import dumps, loads
import pandas as pd

def get_mp3_url(row):
    url = row['URL']
    doc = bs(get('https://www.goodshepherdbinghamton.org/' + url).content, 'html.parser')
    links = [a.attrs['href'] for a in doc.find_all("a")]
    links = [a for a in links if a.endswith('.mp3') or a.endswith('.m4a')]
    return url if len(links) == 0 else links[0]

blogs = loads(open('cogs.json').read())
df = pd.DataFrame([[v for k, v in blog.items()] for blog in blogs],
                   columns = ['Title', 'Date', 'Text', 'URL', 'Passage', 'Speaker'])

urls = list(df['URL'])
