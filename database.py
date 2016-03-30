from lxml import html
import requests

# There are 4 index pages containing the idioms

pg_num = ['', '2','3','4']
collection = []

for i in pg_num:
    page = requests.get('http://idiomsite.com/index' + i + '.htm')
    tree = html.fromstring(page.content)
    words = tree.xpath('//span[@class="style1"]/text()')
    collection.append(words)

# I need to flatten the list because there are nested lists

flattened = []

for sub_list in collection:
    for idiom in sub_list:
        idiom = idiom.strip(': ').capitalize()
        flattened.append(idiom)

idioms = flattened

idioms_file = open('idioms.txt', 'w+')

for idiom in idioms:
    idioms_file.write(idiom + '\n')

idioms_file.close()
