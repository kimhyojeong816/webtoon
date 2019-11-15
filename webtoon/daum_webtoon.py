import requests
import time
from .models import WebToon



# print(time.time())

def artist_name(artist):
    return artist[0].get('name')+'/'+artist[1].get('name')


def daum_webtoon_week(week):
        json_object=requests.get('http://webtoon.daum.net/data/pc/webtoon/list_serialized/' + week + '?timeStamp='+str(time.time())).json()
        # print(json_object.get('result'))
        # print(json_object.get('data'))

        webtoon_list=json_object.get('data')
        for webtoon in webtoon_list:
            daum_webtoon=WebToon()
            daum_webtoon.webtoon_id='다음_'+webtoon.get('title')
            daum_webtoon.webtoon_name = webtoon.get('title')
            daum_webtoon.webtoon_author = artist_name(webtoon.get('cartoon').get('artists'))
            daum_webtoon.webtoon_img_url = webtoon.get('thumbnailImage2').get('url')
            daum_webtoon.site_name = '다음'

            daum_webtoon.save()

            # print(artist_name(webtoon.get('cartoon').get('artists')))
            # print(webtoon.get('title'))
            # for artist in webtoon.get('cartoon').get('artists'):
            #     print(artist.get('name'),end='/')
            #     print()
            #     print(webtoon.get('thumbnailImage2').get('url'))

def daum_webtoon():
    week_list=['mon','tue','wed','thu','fri','sat','sun']
    for week in week_list:
        daum_webtoon_week(week)
#
# daum_webtoon()