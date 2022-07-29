import requests
import json
from pprint import pprint


content_Hulk = json.loads(requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Hulk').content)
intel_Hulk = int(content_Hulk['results'][0]['powerstats']['intelligence'])
content_Captain = json.loads(requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Captain')
                             .content)
intel_Captain = int(content_Captain['results'][0]['powerstats']['intelligence'])
content_Thanos = json.loads(requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Thanos').content)
intel_Thanos = int(content_Thanos['results'][0]['powerstats']['intelligence'])
intel_dict = {'Hulk': intel_Hulk, 'Captain america': intel_Captain, 'Thanos': intel_Thanos}

print(f'{max(intel_dict)} - самый умный супергерой')


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {"Authorization": 'OAuth {}'.format(self.token)}

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        header = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=header, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str):
        href = self._get_upload_link(disk_file_path=d_file_path).get('href', '')
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    TOKEN = 'AQAAAABGItorAADLW6c0v7u9tEidsArARMEGUW4'
    d_file_path = 'important_file.txt'
    uploader = YaUploader(token=TOKEN)
    uploader.upload('important_file.txt')
