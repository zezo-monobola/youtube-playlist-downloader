#bibliotecas utilizadas
from pytube import YouTube
from pytube import Playlist

#p recebe o link da playlist, pode ser o link de um video da playlist que funciona tambem
playlist_url = input('insira o link:')
p = Playlist(playlist_url)
path = input('insira o caminho')
print(f'Downloading:{p.title}')

#para cada video da playlist baixe o video 
for video in p.videos:
    video.streams.get_audio_only().download(path)
print('done')
