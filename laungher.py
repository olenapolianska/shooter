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
skin_2 = QLabel("Картинка")
skin_3 = QLabel("Картинка")
skin_1_img = QPixmap("asteroid.png")
skin_2_img = QPixmap("ufo.png")
skin_3_img = QPixmap("rocket.png")
skin_1_img = skin_1_img.scaledToWidth(64)
skin_2_img = skin_2_img.scaledToWidth(64)
skin_3_img = skin_3_img.scaledToWidth(64)
skin_1.setPixmap(skin_1_img)
skin_2.setPixmap(skin_2_img)
skin_3.setPixmap(skin_3_img)
buy_skin_1_btn = QPushButton("Купити скін")
buy_skin_2_btn = QPushButton("Купити скін")
buy_skin_3_btn = QPushButton("Купити скін")
line_edit = QLineEdit(settings["skin"])

mainline = QVBoxLayout()
line = QHBoxLayout()
line2 = QHBoxLayout()
mainline.addLayout(line)
mainline.addLayout(line2)

mainline.addWidget(line_edit)
mainline.addWidget(start)
mainline.addWidget(change_btn)
line.addWidget(skin_1)
line2.addWidget(buy_skin_1_btn)
line.addWidget(skin_2)
line2.addWidget(buy_skin_2_btn)
line.addWidget(skin_3)
line2.addWidget(buy_skin_3_btn)

def buy_skin_1():
    if settings["money"] >= 7:
        settings["money"] -= 7
        settings["skin"] = "asteroid.png"
        write_data()
    else:
        print("Грошей не вистачає")

def buy_skin_2():
    if settings["money"] >= 20:
        settings["money"] -= 20
        settings["skin"] = "ufo.png"
        write_data()
    else:
        print("Грошей не вистачає")

def buy_skin_3():
    if settings["money"] >= 30:
        settings["money"] -= 30
        settings["skin"] = "rocket.png"
        write_data()
    else:
        print("Грошей не вистачає")



def change_data():
    settings["skin"] = line_edit.text()
    write_data()

buy_skin_1_btn.clicked.connect(buy_skin_1)
buy_skin_2_btn.clicked.connect(buy_skin_2)
buy_skin_3_btn.clicked.connect(buy_skin_3)
change_btn.clicked.connect(change_data)
start.clicked.connect(start_game)

window.setLayout(mainline)

window.show()
app.exec()