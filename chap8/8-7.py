def make_album(singer_name, album_name):
    album = {'singer': singer_name, 'album': album_name}
    return album


a1 = make_album('jaychou', 'love')
print(a1)
a2 = make_album('amei', 'beauty')
print(a2)
a3 = make_album('taylor', 'you')
print(a3)


def new_make_album(singer_name, album_name, album_nums=''):
    album = {'singer': singer_name, 'album': album_name}
    if album_nums:
        album['nums'] = album_nums
    return album


a4 = new_make_album('jaychou', 'love', 6)
print(a4)
a5 = new_make_album('amei', 'beauty')
print(a5)
a6 = new_make_album('taylor', 'you')
print(a6)
