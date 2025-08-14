from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from random import randint,choice
import string
letters = string.ascii_letters

class Widget(QMainWindow):
    global letters
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.randomizer) # нажатие на кнопку
    def randomizer(self): #функция random
        result = "" #переменная куда сохроняються сгенерирование числа
        if self.ui.checkBox_2.isChecked():
            for i in range(8): #перебор и количество чисел в пароле
                a = randint(0,9 )
                result+= str(a)
        self.ui.label_2.setText(result) #КРЕПИМ
        if self.ui.checkBox.isChecked(): # ПРОВЕРКА ЧТО КНОПКА НАЖАТА
            print(letters) # ВИВОД
        #print(result) #виводим
            for p in range(8): # 
                save  = choice(letters)
                result += save
        if self.ui.
            print(result)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()