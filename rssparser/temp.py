# #u = 'api/v1/feeds' / str(12) / 'authors/'
# import httpx


# print(httpx.get('http://127.0.0.1:5000' / 'api'))
# #
# # print(httpx.get(str(u)))
# # print(str(u))

# import os
# from yarl import URL
# #print(type(os.environ['API_URL']))
# from rssparser.config import load_from_env
# apiconfig = load_from_env()
# print(apiconfig.api_url)
#.api_url.path)
#  url = URL(os.environ['API_URL'])
# print(url / 'articles')
# print(type(url))
from datetime import datetime
import arrow
date =  arrow.now().for_json()
# print(arrow.get(date).datetime)
import json
# print(json.dumps(date))

import httpx

# data = {'title': 'Начальник радиотехни... во\xa0взятке', 'url': 'https://meduza.io/ne...vo-vzyatke', 'published': '2022-01-14T09:38:04+00:00', 'feed_id': 2, 'author_id': None, 'description': None}

# r = httpx.post("http://127.0.0.1:5000/api/v1/articles/", json=data)#.json()
# # print(r)
# d = datetime.now()
# print(arrow(d))

s = 'Fri, 14 Jan 2022 09:38:04 GMT'
print(arrow.get(s))

