# uncompyle6 version 3.6.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.5 (default, Oct 27 2019, 15:43:29) 
# [GCC 9.2.1 20191022]
# Embedded file name: .\skillshare.py
# Size of source mod 2**32: 10032 bytes
import requests, json, sys, re, os, base64
from slugify import slugify

class Skillshare(object):

    def __init__(self, scrumbledata='\nZGV2aWNlX3Nlc3Npb25faWQ9MmQ0NTZlMDAtN2JlZi00MDQ0LWI3OGYtYmM1ZjUwN2I0NzhmOyBzaG93LWxpa2UtY29weT0wOyBZSUlfQ1NSRl9UT0tFTj1lVXBIUVc5b2FXWlRNM0ZaT0hCdFEzbEphakZNVldNMVlVMUZjR1JYU1RkelFkdDdsUjhtbUI1MTBYRWtjRDNnTmtuSFdKTmlia09OVGZnT3pRS2phZyUzRCUzRDsgdmlzaXRvcl90cmFja2luZz11dG1fY2FtcGFpZ24lM0QlMjZ1dG1fc291cmNlJTNEJTI4ZGlyZWN0JTI5JTI2dXRtX21lZGl1bSUzRCUyOG5vbmUlMjklMjZyZWZlcnJlciUzRCUyNnJlZmVycmluZ191c2VybmFtZSUzRDsgZmlyc3RfbGFuZGluZz11dG1fY2FtcGFpZ24lM0QlMjZ1dG1fc291cmNlJTNEJTI4ZGlyZWN0JTI5JTI2dXRtX21lZGl1bSUzRCUyOG5vbmUlMjklMjZyZWZlcnJlciUzRCUyNnJlZmVycmluZ191c2VybmFtZSUzRDsgX191dG1hPTk5NzA0OTg4LjE1MDY4MjY1MTYuMTU2NjE5MTY1NC4xNTY2MTkxNjU0LjE1NjYxOTE2NTQuMTsgX191dG1jPTk5NzA0OTg4OyBfX3V0bXo9OTk3MDQ5ODguMTU2NjE5MTY1NC4xLjEudXRtY3NyPShkaXJlY3QpfHV0bWNjbj0oZGlyZWN0KXx1dG1jbWQ9KG5vbmUpOyBfX3V0bXQ9MTsgX2djbF9hdT0xLjEuMjU4MTA1NzA5LjE1NjYxOTE2NTQ7IF9fc3RyaXBlX21pZD01MDg2NGU5NS1lZTgwLTQ3NjktOGVlNi03MGVjNjY4YzQyMTU7IF9fc3RyaXBlX3NpZD1kZmU2YTllMC05MjkwLTQxNmMtYWVjYS0xMTYzMTMxNTg4NzA7IElSX2diZD1za2lsbHNoYXJlLmNvbTsgX19wZHN0PWJlMzgyYTI4MmUxYTQ1ZTFhYWQ4MTk5NWY4NDgwNzkxOyBfZmJwPWZiLjEuMTU2NjE5MTY1OTk3MS40MzI0ODE3OyBHX0VOQUJMRURfSURQUz1nb29nbGU7IHNzX2hpZGVfc2l0ZV9iYW5uZXI9MTU2NjE5MTY2MS41MzE7IF9fcWNhPVAwLTE5MTM1MDc1Ny0xNTY2MTkxNjYwNzI5OyBfX3NzaWQ9ZTgzZTg1MTk1MGZiY2Q5MDJjY2U1YzRlNmQ0NDAyMTsgUEhQU0VTU0lEPTMyMzhjMTcxNjY1ODg3MzBlYTZmZDY1ODBjMDk0M2I3OyBza2lsbHNoYXJlX3VzZXJfPTRiOTM3M2I3N2Q3OTMxY2IyODg5ZDMwNmI2MGM1ZDhmN2YxYmVlNDdhJTNBNCUzQSU3QmklM0EwJTNCcyUzQTclM0ElMjIxMDk5MzIwJTIyJTNCaSUzQTElM0JzJTNBMjIlM0ElMjJhZGVsdXp1cmlhZ2ElNDBnbWFpbC5jb20lMjIlM0JpJTNBMiUzQmklM0EyNTkyMDAwJTNCaSUzQTMlM0JhJTNBMTElM0ElN0JzJTNBNSUzQSUyMmVtYWlsJTIyJTNCcyUzQTIyJTNBJTIyYWRlbHV6dXJpYWdhJTQwZ21haWwuY29tJTIyJTNCcyUzQTklM0ElMjJmaXJzdE5hbWUlMjIlM0JzJTNBNiUzQSUyMkFydGh1ciUyMiUzQnMlM0E4JTNBJTIybGFzdE5hbWUlMjIlM0JzJTNBMTIlM0ElMjJEZStMdXp1cmlhZ2ElMjIlM0JzJTNBOCUzQSUyMmhlYWRsaW5lJTIyJTNCTiUzQnMlM0EzJTNBJTIycGljJTIyJTNCcyUzQTY3JTNBJTIyaHR0cHMlM0ElMkYlMkZzdGF0aWMuc2tpbGxzaGFyZS5jb20lMkZhc3NldHMlMkZpbWFnZXMlMkZkZWZhdWx0LXByb2ZpbGUtbHJnLmpwZyUyMiUzQnMlM0E1JTNBJTIycGljU20lMjIlM0JzJTNBNjYlM0ElMjJodHRwcyUzQSUyRiUyRnN0YXRpYy5za2lsbHNoYXJlLmNvbSUyRmFzc2V0cyUyRmltYWdlcyUyRmRlZmF1bHQtcHJvZmlsZS1zbS5qcGclMjIlM0JzJTNBNSUzQSUyMnBpY0xnJTIyJTNCcyUzQTY3JTNBJTIyaHR0cHMlM0ElMkYlMkZzdGF0aWMuc2tpbGxzaGFyZS5jb20lMkZhc3NldHMlMkZpbWFnZXMlMkZkZWZhdWx0LXByb2ZpbGUtbHJnLmpwZyUyMiUzQnMlM0E5JTNBJTIyaXNUZWFjaGVyJTIyJTNCcyUzQTElM0ElMjIwJTIyJTNCcyUzQTglM0ElMjJ1c2VybmFtZSUyMiUzQnMlM0E3JTNBJTIyMTUyMTQ5OCUyMiUzQnMlM0EzJTNBJTIyemlwJTIyJTNCcyUzQTAlM0ElMjIlMjIlM0JzJTNBNiUzQSUyMmNpdHlJRCUyMiUzQnMlM0ExJTNBJTIyMCUyMiUzQiU3RCU3RDsgb3JpZW50YXRpb24tZmxvdy1kYXRhPSU3QiUyMm9yaWVudGF0aW9uUGF0aCUyMiUzQSU3QiUyMm9yaWVudGF0aW9uJTVDJTJGaW5kZXglMjIlM0ElMjJvcmllbnRhdGlvbiU1QyUyRmZvbGxvd3NraWxscyUyMiUyQyUyMm9yaWVudGF0aW9uJTVDJTJGZm9sbG93c2tpbGxzJTIyJTNBJTIyb3JpZW50YXRpb24lNUMlMkZjbGFzc2VzJTIyJTJDJTIyb3JpZW50YXRpb24lNUMlMkZjbGFzc2VzJTIyJTNBJTIyb3JpZW50YXRpb24lNUMlMkZyZWZlcnJhbHMlMjIlMkMlMjJvcmllbnRhdGlvbiU1QyUyRnJlZmVycmFscyUyMiUzQSUyMm9yaWVudGF0aW9uJTVDJTJGY29tcGxldGUlMjIlN0QlMkMlMjJ2aWV3ZWRQYWdlcyUyMiUzQSU1QiU1RCUyQyUyMmZpbmFsUmVkaXJlY3QlMjIlM0ElMjJodHRwcyUzQSU1QyUyRiU1QyUyRnd3dy5za2lsbHNoYXJlLmNvbSU1QyUyRmhvbWUlM0Z2aWElM0Rsb2dnZWQtaW4taG9tZSUyMiUyQyUyMmNvbXBsZXRlc09yaWVudGF0aW9uJTIyJTNBdHJ1ZSUyQyUyMmZvcmNlJTIyJTNBdHJ1ZSU3RDsgX191dG12PTk5NzA0OTg4LnwxPXZpc2l0b3ItdHlwZT11c2VyPTE7IF9fdXRtYj05OTcwNDk4OC4yLjEwLjE1NjYxOTE2NTQ7IElSTVNfbGE0NjUwPTE1NjYxOTE2OTA4MzY7IG1wX2MwZmZhMjA5M2QwMmUwZDUwM2RiMDdmZTE0MmFhYjk4X21peHBhbmVsPSU3QiUyMmRpc3RpbmN0X2lkJTIyJTNBJTIwJTIyMTZjYTg0YzFkODAyMmEtMGU4N2IzZDViODlkYjQtNjU1YzdkMjEtMTQ0MDAwLTE2Y2E4NGMxZDgxMzI5JTIyJTJDJTIyJTI0ZGV2aWNlX2lkJTIyJTNBJTIwJTIyMTZjYTg0YzFkODAyMmEtMGU4N2IzZDViODlkYjQtNjU1YzdkMjEtMTQ0MDAwLTE2Y2E4NGMxZDgxMzI5JTIyJTJDJTIyJTI0aW5pdGlhbF9yZWZlcnJlciUyMiUzQSUyMCUyMiUyNGRpcmVjdCUyMiUyQyUyMiUyNGluaXRpYWxfcmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMCUyMiUyNGRpcmVjdCUyMiUyQyUyMiUyNHVzZXJfaWQlMjIlM0ElMjAlMjIxNmNhODRjMWQ4MDIyYS0wZTg3YjNkNWI4OWRiNC02NTVjN2QyMS0xNDQwMDAtMTZjYTg0YzFkODEzMjklMjIlN0Q7IHBzZXM9eyJpZCI6Ijl3dHhwOW5mN29xIiwic3RhcnQiOjE1NjYxOTE2NTcwMDgsImxhc3QiOjE1NjYxOTE2OTExNjF9OyBzc19oaWRlX2RlZmF1bHRfYmFubmVyPTE1NjYxOTE2OTQuMjEx\n                 ', download_path=os.environ.get('FILE_PATH', './data'), pk='BCpkADawqM2OOcM6njnM7hf9EaK6lIFlqiXB0iWjqGWUQjU7R8965xUvIQNqdQbnDTLz0IAO7E6Ir2rIbXJtFdzrGtitoee0n1XXRliD-RH9A-svuvNW9qgo3Bh34HEZjXjG4Nml4iyz3KqF', brightcove_account_id=3695997568001):
        self.scrumbledata = base64.b64decode(scrumbledata.strip().strip('"'))
        self.download_path = download_path
        self.pk = pk.strip()
        self.brightcove_account_id = brightcove_account_id
        self.pythonversion = 3 if sys.version_info >= (3, 0) else 2

    def is_unicode_string(self, string):
        if self.pythonversion == 3 and isinstance(string, str) or self.pythonversion == 2:
            return True
            #if isinstance(string, unicode):
                #pass
            #else:
                #return True
        return False

    def download_course_by_url(self, url):
        m = re.match('https://www.skillshare.com/classes/.*?/(\\d+)', url)
        if not m:
            raise Exception('Failed to parse class ID from URL')
        self.download_course_by_class_id(m.group(1))

    def download_course_by_class_id(self, class_id):
        data = self.fetch_course_data_by_class_id(class_id=class_id)
        teacher_name = None
        if 'vanity_username' in data['_embedded']['teacher']:
            teacher_name = data['_embedded']['teacher']['vanity_username']
        if not teacher_name:
            teacher_name = data['_embedded']['teacher']['full_name']
        if not teacher_name:
            raise Exception('Failed to read teacher name from data')
        if self.is_unicode_string(teacher_name):
            teacher_name = teacher_name.encode('ascii', 'replace')
        title = data['title']
        if self.is_unicode_string(title):
            title = title.encode('ascii', 'replace')
        base_path = os.path.abspath(os.path.join(self.download_path, slugify(teacher_name), slugify(title))).rstrip('/')
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        for u in data['_embedded']['units']['_embedded']['units']:
            for s in u['_embedded']['sessions']['_embedded']['sessions']:
                video_id = None
                if 'video_hashed_id' in s:
                    if s['video_hashed_id']:
                        video_id = s['video_hashed_id'].split(':')[1]
                if not video_id:
                    raise Exception('Failed to read video ID from data')
                s_title = s['title']
                if self.is_unicode_string(s_title):
                    s_title = s_title.encode('ascii', 'replace')
                file_name = '{} - {}'.format(str(s['index'] + 1).zfill(2), slugify(s_title))
                self.download_video(fpath='{base_path}/{session}.mp4'.format(base_path=base_path,
                  session=file_name),
                  video_id=video_id)
                print('')

    def fetch_course_data_by_class_id(self, class_id):
        res = requests.get(url=('https://api.skillshare.com/classes/{}'.format(class_id)),
          headers={'Accept':'application/vnd.skillshare.class+json;,version=0.8', 
         'User-Agent':'Skillshare/4.1.1; Android 5.1.1', 
         'Host':'api.skillshare.com', 
         'cookie':self.scrumbledata})
        if not res.status_code == 200:
            raise Exception('Fetch error, code == {}'.format(res.status_code))
        return res.json()

    def download_video(self, fpath, video_id):
        meta_url = 'https://edge.api.brightcove.com/playback/v1/accounts/{account_id}/videos/{video_id}'.format(account_id=(self.brightcove_account_id),
          video_id=video_id)
        meta_res = requests.get(meta_url,
          headers={'Accept':'application/json;pk={}'.format(self.pk), 
         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0', 
         'Origin':'https://www.skillshare.com'})
        if meta_res.status_code != 200:
            raise Exception('Failed to fetch video meta')
        
        for x in meta_res.json()['sources']:
            print(x)
        #     if x['container'] == 'MP4' and 'src' in x:
        #         dl_url = x['src']
        #         break

        # print('Downloading {}...'.format(fpath))
        # if os.path.exists(fpath):
        #     print('Video already downloaded, skipping...')
        #     return
        # with open(fpath, 'wb') as f:
        #     response = requests.get(dl_url, allow_redirects=True, stream=True)
        #     total_length = response.headers.get('content-length')
        #     if not total_length:
        #         f.write(response.content)
        #     else:
        #         dl = 0
        #         total_length = int(total_length)
        #         for data in response.iter_content(chunk_size=4096):
        #             dl += len(data)
        #             f.write(data)
        #             done = int(50 * dl / total_length)
        #             sys.stdout.write('\r[%s%s]' % ('=' * done, ' ' * (50 - done)))
        #             sys.stdout.flush()

        #     print('')
# okay decompiling skillshare.pyc
