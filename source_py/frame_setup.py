from PyQt5.QtWidgets import QGraphicsDropShadowEffect

from PyQt5 import QtCore

from PyQt5.QtGui import QColor, QIcon


# Меню настройки приложения
# Используется большинством окон
def setup_frame(widget, main_frame):
    # Убираем фон и рамку окна
    widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Устанавливаем имя и иконку окна
    widget.setWindowTitle("Своя Игра")
    widget.setWindowIcon(QIcon("../images/background_images/window_icon.png"))

    # Настраиваем тень от окна - для красоты
    widget.shadow = QGraphicsDropShadowEffect(widget)
    widget.shadow.setBlurRadius(30)
    widget.shadow.setXOffset(0)
    widget.shadow.setYOffset(0)
    widget.shadow.setColor(QColor(0, 0, 0, 60))
    main_frame.setGraphicsEffect(widget.shadow)


# Настройка общего для всех уровней игры UI оформления
# Связанного с участниками игры (отображение их иконок, фона, очков)
def setup_players(widget):
    # Настройка изображений и заднего фона участников игры
    widget.player_image.setPixmap(widget.game_manager.get_player_image())
    widget.enemy1_image.setPixmap(widget.game_manager.get_enemies_images()[0])
    widget.enemy2_image.setPixmap(widget.game_manager.get_enemies_images()[1])
    widget.player_frame.setStyleSheet(
        f"background-color: {widget.game_manager.get_player_background_color()}")

    # Настройка имён участников игры
    widget.player_name.setText(widget.game_manager.player.get_name())
    widget.enemy1_name.setText(widget.game_manager.enemy1.get_name())
    widget.enemy2_name.setText(widget.game_manager.enemy2.get_name())
