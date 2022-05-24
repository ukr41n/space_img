import os, requests
from datetime import datetime
from urllib.parse import urlparse, unquote


url_spacex = 'https://api.spacexdata.com/v4/launches/'
path_spacex = "images/spacex"


def get_extension(url):
    '''Функция, возвращающая расширение файла'''
    ext = (
        os.path.splitext(
            os.path.split(
                urlparse(
                    unquote(url)
                ).path
            )[-1]
        )[-1]
    )[1:]
    return ext


def downl_img_to_fold(url, path, serial_number):
    '''Функция загружает фотографии по ссылке, полученной в качестве аргумента <url>'''
    filename = f'{path}/{serial_number}.{get_extension(url)}'
    if not os.path.exists(path):
        os.makedirs(path)
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url_spacex, path_spacex):
    '''Функция получает фотографии последнего запуска шатла.'''
    response = requests.get(url_spacex)
    response.raise_for_status()
    for item in reversed(response.json()):
        if item['links']['flickr']['original'] != []:
            list_of_spacex_links = item['links']['flickr']['original']
            break
    for serial_number, link in enumerate(list_of_spacex_links):
        downl_img_to_fold(link, path_spacex, serial_number)


def main():
    fetch_spacex_last_launch(url_spacex, path_spacex)
    

if __name__ == '__main__':
   main()
