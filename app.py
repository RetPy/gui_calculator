import re

from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QGridLayout, QWidget, QApplication, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Инициализация атрибутов

        self.setWindowTitle('Калькулятор')  # Название окна
        with open('widget_style.css', 'r', encoding='utf-8') as file:  # Чтение файла стилей
            style = file.read()
        self.setStyleSheet(style)

        self.label = QLabel()  # Табличка для вывода данных

        # Кнопки калькулятора
        self.clear_button = QPushButton('C')
        self.delete_last = QPushButton('<-')
        self.l_bracket = QPushButton('(')
        self.r_bracket = QPushButton(')')
        self.dot = QPushButton('.')
        self.plus_button = QPushButton('+')
        self.minus_button = QPushButton('-')
        self.multiply_button = QPushButton('*')
        self.division_button = QPushButton('/')
        self.equal_button = QPushButton('=')
        self.button0 = QPushButton('0')
        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')
        self.button5 = QPushButton('5')
        self.button6 = QPushButton('6')
        self.button7 = QPushButton('7')
        self.button8 = QPushButton('8')
        self.button9 = QPushButton('9')

        # Обработка сигнала при нажатии кнопки
        self.clear_button.clicked.connect(lambda: self.add_symbol(self.clear_button.text()))
        self.delete_last.clicked.connect(lambda: self.add_symbol(self.delete_last.text()))
        self.l_bracket.clicked.connect(lambda: self.add_symbol(self.l_bracket.text()))
        self.r_bracket.clicked.connect(lambda: self.add_symbol(self.r_bracket.text()))
        self.dot.clicked.connect(lambda: self.add_symbol(self.dot.text()))
        self.plus_button.clicked.connect(lambda: self.add_symbol(self.plus_button.text()))
        self.minus_button.clicked.connect(lambda: self.add_symbol(self.minus_button.text()))
        self.multiply_button.clicked.connect(lambda: self.add_symbol(self.multiply_button.text()))
        self.division_button.clicked.connect(lambda: self.add_symbol(self.division_button.text()))
        self.equal_button.clicked.connect(lambda: self.add_symbol(self.equal_button.text()))
        self.button0.clicked.connect(lambda: self.add_symbol(self.button0.text()))
        self.button1.clicked.connect(lambda: self.add_symbol(self.button1.text()))
        self.button2.clicked.connect(lambda: self.add_symbol(self.button2.text()))
        self.button3.clicked.connect(lambda: self.add_symbol(self.button3.text()))
        self.button4.clicked.connect(lambda: self.add_symbol(self.button4.text()))
        self.button5.clicked.connect(lambda: self.add_symbol(self.button5.text()))
        self.button6.clicked.connect(lambda: self.add_symbol(self.button6.text()))
        self.button7.clicked.connect(lambda: self.add_symbol(self.button7.text()))
        self.button8.clicked.connect(lambda: self.add_symbol(self.button8.text()))
        self.button9.clicked.connect(lambda: self.add_symbol(self.button9.text()))

        grid = QGridLayout()  # Сетка для разметки позиции таблички и кнопок
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.clear_button, 1, 0)
        grid.addWidget(self.delete_last, 1, 1)
        grid.addWidget(self.l_bracket, 1, 2)
        grid.addWidget(self.r_bracket, 1, 3)
        grid.addWidget(self.button7, 2, 0)
        grid.addWidget(self.button8, 2, 1)
        grid.addWidget(self.button9, 2, 2)
        grid.addWidget(self.plus_button, 2, 3)
        grid.addWidget(self.button4, 3, 0)
        grid.addWidget(self.button5, 3, 1)
        grid.addWidget(self.button6, 3, 2)
        grid.addWidget(self.minus_button, 3, 3)
        grid.addWidget(self.button1, 4, 0)
        grid.addWidget(self.button2, 4, 1)
        grid.addWidget(self.button3, 4, 2)
        grid.addWidget(self.multiply_button, 4, 3)
        grid.addWidget(self.button0, 5, 0)
        grid.addWidget(self.dot, 5, 1)
        grid.addWidget(self.equal_button, 5, 2)
        grid.addWidget(self.division_button, 5, 3)

        container = QWidget()  # Создаём обычный виджет
        container.setLayout(grid)  # Указываем нашу сетку с кнопками для виджета

        self.setCentralWidget(container)  # Указываем наш контейнер для отображения главного виджета

    # Метод обрабатывающий сигнал кнопок
    def add_symbol(self, symbol):
        text = self.label.text()  # Получение текущего текста в табличке
        operators = ['+', '-', '*', '/', '.']
        # Логика для обработки сигнала кнопки
        if symbol == 'C':
            self.label.setText('')
        elif symbol == '<-':
            self.label.setText(text[:-1])
        elif symbol == '=':
            try:
                if re.search(r'\d+\(', text):  # Нахождение по паттерну "цифры(" и последующая замена на "цифры*("
                    all_patt = re.findall(r'\d+\(', text)
                    for patt in all_patt:
                        new_patt = '{0}*('.format((re.findall(r"\d+", patt))[0])
                        text = text.replace(patt, new_patt)
                self.label.setNum(eval(text))
            except ZeroDivisionError:
                zero_err = QMessageBox(self)
                zero_err.setWindowTitle('Ошибка!')
                zero_err.setText('На ноль делить нельзя!')
                zero_err.setStandardButtons(QMessageBox.StandardButton.Close)
                zero_err.exec()
        elif symbol in operators:
            if not text and symbol == '-':
                self.label.setText('-')
            elif not text:
                pass
            elif text[-1] in operators:
                self.label.setText(f'{text[:-1]}{symbol}')
            elif text != '' and symbol != text[-1]:
                self.label.setText(f'{text}{symbol}')
        else:
            self.label.setText(f'{text}{symbol}')


if __name__ == '__main__':  # Точка входа
    import sys

    app = QApplication(sys.argv)  # Создание приложения

    window = MainWindow()  # Создание окна
    window.show()  # Включение отображения окна, по дефолту оно выключено

    app.exec()  # Запуск приложения
