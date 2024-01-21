import json

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


mainline = QHBoxLayout()
mainline.addWidget(line_edit)
mainline.addWidget(start)
mainline.addWidget(change_btn)

def change_data():
    settings["skin"] = line_edit.text()
    write_data()
change_btn.clicked.connect(change_data)
start.clicked.connect(start_game)

window.setLayout(mainline)

window.show()
app.exec()