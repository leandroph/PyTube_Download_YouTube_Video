from pytube import YouTube

# caminho onde salvar o arquivo que sera baixado
SAVE_PATH = "Downloads"

# link do vídeo a ser baixado
link = input("Link do vídeo: ")

try:
    # criação de objetos usando o YouTube
    # que foi importado no início
    yt = YouTube(link)
except:
    print("Erro de conexão")  # para lidar com a exceção

# filtrar se ira baixar video ou audio
option = input("1 para download do video \n 2 para donload do audio ")

if option == "1":
    mp4files = yt.streams.get_highest_resolution()
elif option == "2":
    mp4files = yt.streams.get_audio_only()
else:
    print("Opção Inválida")
    option = input("1 para download do video"
                   "2 para donload do audio ")

try:
    # baixando o vídeo
    mp4files.download(SAVE_PATH)
except:
    print("Algum erro!")
print('Tarefa completa!')