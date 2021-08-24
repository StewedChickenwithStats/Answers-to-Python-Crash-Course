def make_album(singer_name, album_name):
    album = {'singer': singer_name, 'album': album_name}
    return album


while True:
    print("\nPlease tell me the names of the singer and the album: ")
    print("(enter 'q' at any time to quit)")

    s_name = input("Singer name: ")
    if s_name == 'q':
        break

    a_name = input("Album name: ")
    if a_name == 'q':
        break

    a = make_album(s_name, a_name)
    print(a)
