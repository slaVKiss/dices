import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import random


class DiceRollSimulation(QWidget):
    def __init__(self):
        super().__init__()

        self.results = {}
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Dice Roll Simulation')
        layout = QVBoxLayout()

        label = QLabel('Сколько костей вы хотите бросить?')
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Введите число костей')
        roll_button = QPushButton('Бросить кости')
        roll_button.clicked.connect(self.roll_dice)
        self.result_label = QLabel('')

        layout.addWidget(label)
        layout.addWidget(self.input_field)
        layout.addWidget(roll_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def roll_dice(self):
        try:
            number_of_dice = int(self.input_field.text())
            for i in range(number_of_dice, (number_of_dice * 6) + 1):
                self.results[i] = 0

            for _ in range(1000000):
                total = 0
                for _ in range(number_of_dice):
                    total += random.randint(1, 6)
                self.results[total] += 1

            result_text = 'Число - Бросков - Проценты\n'
            for i in range(number_of_dice, (number_of_dice * 6) + 1):
                roll = self.results[i]
                percent = round(self.results[i] / 10000, 1)
                result_text += ' {} - {} бросков - {}%\n'.format(i, roll, percent)

            self.result_label.setText(result_text)
        except ValueError:
            self.result_label.setText('Пожалуйста, введите целое число костей.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiceRollSimulation()
    window.show()
    sys.exit(app.exec())


