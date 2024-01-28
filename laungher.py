import json

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from main import start_game

app = QApplication([])
settings = {}
window = QWidget()

def read_data():
    global settings
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)
def write_data():
    global settings
    with open ("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file)
read_data()

print(settings)

start = QPushButton("Старт")
line_edit = QLineEdit(settings["skin"])
change_btn = QPushButton("Change")
skin_1 = QLabel("Картинка")
skin_1_img = QPixmap("asteroid.png")
skin_1_img = skin_1_img.scaledToWidth(64)
skin_1.setPixmap(skin_1_img)
buy_skin_1_btn = QPushButton("Купити скін")
line_edit = QLineEdit(settings["skin"])

mainline = QHBoxLayout()
mainline.addWidget(line_edit)
mainline.addWidget(start)
mainline.addWidget(change_btn)
mainline.addWidget(skin_1)
mainline.addWidget(buy_skin_1_btn)

def buy_skin_1():
    if settings["money"] >= 7:
        settings["money"] -= 7
        settings ["skin"] = "asteroid.png"
        write_data()
    else:
        print("Грошей не вистачає")


def change_data():
    settings["skin"] = line_edit.text()
    write_data()
change_btn.clicked.connect(change_data)
start.clicked.connect(start_game)

window.setLayout(mainline)

window.show()
app.exec()