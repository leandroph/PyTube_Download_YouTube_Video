from youtube_dl import YoutubeDL
import ffmpeg

NOME = 'YOUTUBE DOWNLOADER'
MSG = f'Encerrando o Programa {NOME}'

#https://www.ti-enxame.com/pt/python/baixar-apenas-o-audio-do-video-do-youtube-usando-o-youtube-dl-no-script-python/1050145910/
#https://dev.to/kalebu/how-to-download-youtube-video-as-audio-using-python-33g9
def download_video(url):
    ydl_opts = {'format': 'bestvideo[height<=?720]+bestaudio/best'}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_audio(url):
    audio_downloader = YoutubeDL({'format': 'bestaudio',
                                  'preferredcodec': 'mp3'})
    audio_downloader.extract_info(url)

def informacao(url):
    ydl_opts = {}

    with YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)

    print('upload date : %s' % (meta['upload_date']))
    print('uploader    : %s' % (meta['uploader']))
    print('views       : %d' % (meta['view_count']))
    print('likes       : %d' % (meta['like_count']))
    print('dislikes    : %d' % (meta['dislike_count']))
    print('id          : %s' % (meta['id']))
    print('format      : %s' % (meta['format']))
    print('duration    : %s' % (meta['duration']))
    print('title       : %s' % (meta['title']))
    print('description : %s' % (meta['description']))

def painel():
    print('-' * len(NOME))
    print(NOME)
    print('-' * len(NOME))

def encerrando_sistema():
    print('-' * len(MSG))
    print(MSG)
    print('-' * len(MSG))

#download_video('https://www.youtube.com/watch?v=G0YHlf7GT1k')
while True:
    painel()
    opcao = input('1 - Video \n2 - Audio\n3 - PARA SAIR\n')
    link = input('Informe o link link do video do YOUTUBE: ')

    if opcao == '1':
        download_video(str(link))
    elif opcao == '2':
        download_audio(str(link))
    elif opcao == '3':
        encerrando_sistema()
        break

