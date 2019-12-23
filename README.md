# exportmyplaylist

# Sobre
O exportmyplaylist é um projeto para exportação de playlists do Spotify em formato CSV, desenvolvido em Python3

# Requirements
attrs==19.3.0
certifi==2019.9.11
chardet==3.0.4
idna==2.8
importlib-metadata==0.23
more-itertools==8.0.0
packaging==19.2
pluggy==0.13.1
py==1.8.0
pyparsing==2.4.5
python-decouple==3.3
requests==2.22.0
six==1.13.0
spotipy==2.4.4
urllib3==1.25.7
wcwidth==0.1.7
zipp==0.6.0
Python3

# Importante
É preciso criar um arquivo .env com o seguinte conteúdo:
CLIENT_ID=<ID de desenvolvedor do Spotify>
CLIENT_SECRET=<Senha de desenvolvedor do Spotify>
  
Ambas informações devem ser inseridas sem aspas.

O ID e senha do desenvolvedor podem ser obtidos em: https://developer.spotify.com/dashboard/

# Como usar
ExportPlaylist(username, playlist_id)
Informar o ID do usuário dono da playlist e o ID da playlist que se deseja exportar.
