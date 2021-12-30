# Иморт PyQt5 компонент
from PyQt5 import QtCore
from PyQt5 import QtMultimedia


# Аудио-проигрыватель, разделяет одну инстанцию
# В течение всей работы приложения
class AudioPlayer:
    def __init__(self):
        self.player = QtMultimedia.QMediaPlayer()

    # При загрузке новой мелодии, останавливаем старую, предупреждая
    # Тем самым возможную ошибку и вылет приложения
    def load(self, filename):
        self.stop()
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player.setMedia(content)

    def set_volume(self, volume):
        self.player.setVolume(volume)

    def get_volume(self):
        return self.player.volume()

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
