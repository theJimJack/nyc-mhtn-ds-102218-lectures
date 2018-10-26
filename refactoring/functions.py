import pandas as pd

records = pd.read_csv('./data.csv')
albums_original = records.to_dict('records')

def convert_album_to_name(album_list):
    coverted_album_list_local = []
    for album in album_list:
        coverted_album_dict = album.copy()
        coverted_album_dict['name'] = coverted_album_dict['album']
        coverted_album_dict.pop('album')
        coverted_album_dict['rank'] = coverted_album_dict['number']
        coverted_album_dict.pop('number')
        coverted_album_list_local.append(coverted_album_dict)
    return coverted_album_list_local

albums_converted = convert_album_to_name(albums_orginal)
