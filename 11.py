from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QLabel,QLineEdit,QVBoxLayout
from PyQt6.QtCore import Qt

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(100, 100,
                         300, 500)
        self.Board()
        self.show()


    def Board(self):
        self.turn = 0
        self.times = 0
        self.push_list = []

        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
            self.push_list.append(temp)
        x = 90
        y = 90
        for i in range(3):
            for j in range(3):
                self.push_list[i][j].setGeometry(x * i + 20,
                                                 y * j + 20,
                                                 80, 80)
                self.push_list[i][j].clicked.connect(self.clik)


        self.label = QLabel(self)

        self.label.setGeometry(30, 300, 250, 30)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        reset_game = QPushButton("Reset-Game", self)

        reset_game.setGeometry(50, 350, 200, 50)

        reset_game.clicked.connect(self.reset_game)

    def reset_game(self):

        self.turn = 0
        self.times = 0

        self.label.setText("")

        for buttons in self.push_list:
            for button in buttons:
                button.setEnabled(True)
                button.setText("")

    def clik(self):

        self.times += 1
        button = self.sender()
        button.setEnabled(False)
        if self.turn == 0:
            button.setText("X")
            self.turn = 1
        else:
            button.setText("O")
            self.turn = 0

        win = self.check_winner()
        text = ""

        if win == True:
            if self.turn == 0:
                text = "O Won"
            else:
                text = "X Won"

            for buttons in self.push_list:
                for push in buttons:
                    push.setEnabled(False)

        elif self.times == 9:
            text = "It's Draw"

        self.label.setText(text)

    def check_winner(self):
        for i in range(3):
            if self.push_list[0][i].text() == self.push_list[1][i].text() \
                    and self.push_list[0][i].text() == self.push_list[2][i].text() \
                    and self.push_list[0][i].text() != "":
                return True

        for i in range(3):
            if self.push_list[i][0].text() == self.push_list[i][1].text() \
                    and self.push_list[i][0].text() == self.push_list[i][2].text() \
                    and self.push_list[i][0].text() != "":
                return True

        if self.push_list[0][0].text() == self.push_list[1][1].text() \
                and self.push_list[0][0].text() == self.push_list[2][2].text() \
                and self.push_list[0][0].text() != "":
            return True

        if self.push_list[0][2].text() == self.push_list[1][1].text() \
                and self.push_list[1][1].text() == self.push_list[2][0].text() \
                and self.push_list[0][2].text() != "":
            return True

        return False


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())