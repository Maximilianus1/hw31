import requests
import json
import os
import sys
from PyQt6.QtWidgets import QLabel,QPushButton,QMainWindow,QApplication,QGridLayout,QWidget,QLineEdit
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        id_label = QLabel("id:", self)
        button = QPushButton("Save")
        id_entry=QLineEdit(self)
        button.clicked.connect(lambda : self.save(id_entry.text()))
        layout.addWidget(id_label,0,0)
        layout.addWidget(id_entry,0,1)
        layout.addWidget(button,1,0)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    def save(self,id_num):
        response = requests.get(f'https://jsonplaceholder.org/posts/{id_num}')
        y = json.loads(response.text)
        os.mkdir(f"file{id_num}")
        with open(f"file{id_num}/file{id_num}.txt", "w") as file:
            file.write(str(y))

os.chdir(os.getcwd())
app = QApplication(sys.argv)

window = Main()
window.show()

app.exec()


