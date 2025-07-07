#Second project idea, just a small simple calc (calc is short for calculator if you didn't know) 
#Tbf its simpler and more easy to make than the Weather App but I wanna get my hands on this just to follow a roadmap
#Its a calc bro you aint reading all of this 

#Falta arreglar bugs y meter variables floats posta lil bro

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QGridLayout, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class CalQLaterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.btn_plus = QPushButton("+", self)
        self.btn_minus = QPushButton("-", self)
        self.btn_div = QPushButton("/", self)
        self.btn_multi = QPushButton("*", self)
        self.btn_result = QPushButton("=", self)
        self.btn_n0 = QPushButton("0", self)
        self.btn_n1 = QPushButton("1", self)
        self.btn_n2 = QPushButton("2", self)
        self.btn_n3 = QPushButton("3", self)
        self.btn_n4 = QPushButton("4", self)
        self.btn_n5 = QPushButton("5", self)
        self.btn_n6 = QPushButton("6", self)
        self.btn_n7 = QPushButton("7", self)
        self.btn_n8 = QPushButton("8", self)
        self.btn_n9 = QPushButton("9", self)
        self.lbl_input = QLabel("0", self)
        self.lbl_result = QLabel("", self)
        self.result_status = False
        self.initUI()

    def initUI(self):
        #la idea seria que solo se puedan meter inputs con lo visual no
        self.setWindowIcon(QIcon("catto.jpg"))
        self.setWindowTitle("CalQLater")
        self.lbl_input.setAlignment(Qt.AlignRight)
        self.lbl_result.setAlignment(Qt.AlignRight)
        self.resize(400, 225)

        VLayout = QVBoxLayout()
        VLayout.addWidget(self.lbl_input)
        VLayout.addWidget(self.lbl_result)

        ButtonsGrid = QGridLayout()

        ButtonsGrid.addWidget(self.btn_n7, 0, 0)
        ButtonsGrid.addWidget(self.btn_n8, 0, 1)
        ButtonsGrid.addWidget(self.btn_n9, 0, 2)
        ButtonsGrid.addWidget(self.btn_div, 0, 3)

        ButtonsGrid.addWidget(self.btn_n4, 1, 0)
        ButtonsGrid.addWidget(self.btn_n5, 1, 1)
        ButtonsGrid.addWidget(self.btn_n6, 1, 2)
        ButtonsGrid.addWidget(self.btn_multi, 1, 3)

        ButtonsGrid.addWidget(self.btn_n1, 2, 0)
        ButtonsGrid.addWidget(self.btn_n2, 2, 1)
        ButtonsGrid.addWidget(self.btn_n3, 2, 2)
        ButtonsGrid.addWidget(self.btn_minus, 2, 3)

        #Recordatorio, el 3 y 0 representa donde se aloja, el 1 y 2 cuanto ocupa (1 fila y 2 columnas)
        ButtonsGrid.addWidget(self.btn_n0, 3, 0, 1, 2)  
        ButtonsGrid.addWidget(self.btn_result, 3, 2)
        ButtonsGrid.addWidget(self.btn_plus, 3, 3)

        #Hago este for así le doy la propiedad a todos los botones de expandirse en altura si la app cambia de tamaño
        #Si no lo hago quedan todos re chatos en el fondo
        for item in range(ButtonsGrid.count()):
            widget = ButtonsGrid.itemAt(item).widget()
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        VLayout.addLayout(ButtonsGrid)
        self.setLayout(VLayout)

        #Eventos de click para los numeros, lambda es un metodo para hacer funciones sin declararlas, para el momento.
        self.btn_n0.clicked.connect(lambda: self.input_showcase("0"))
        self.btn_n1.clicked.connect(lambda: self.input_showcase("1"))
        self.btn_n2.clicked.connect(lambda: self.input_showcase("2"))
        self.btn_n3.clicked.connect(lambda: self.input_showcase("3"))
        self.btn_n4.clicked.connect(lambda: self.input_showcase("4"))
        self.btn_n5.clicked.connect(lambda: self.input_showcase("5"))
        self.btn_n6.clicked.connect(lambda: self.input_showcase("6"))
        self.btn_n7.clicked.connect(lambda: self.input_showcase("7"))
        self.btn_n8.clicked.connect(lambda: self.input_showcase("8"))
        self.btn_n9.clicked.connect(lambda: self.input_showcase("9"))

        self.btn_plus.clicked.connect(lambda: self.input_showcase("+"))
        self.btn_minus.clicked.connect(lambda: self.input_showcase("-"))
        self.btn_div.clicked.connect(lambda: self.input_showcase("/"))
        self.btn_multi.clicked.connect(lambda: self.input_showcase("*"))

        self.btn_result.clicked.connect(self.equations)

        self.setStyleSheet("""
        QWidget{
            background-color: #191a19;
            color: white;
        }
        QPushButton{
            background-color: #383838;
            border: none;
            padding: 8px;
            font-weight: bold;
            color: #cacbcc;
            font-family: calibri;
            font-size: 15px;
        }
        QPushButton:hover{
            background-color: #4d4c4c;
        }
        QLabel{
            font-size: 22px;
            font-family: calibri;
        }
        """)


    def equations(self):
        partes = self.lbl_input.text().strip().split()

        #Hago esto para ver que no hagan, por ejemplo: 3- y le den al "=" (se rompe todo si no)
        if len(partes) != 3:
            return
        
        #Aca parto el operador y los 2 numeros.
        num1, operator, num2 = partes
        num1 = int(num1) 
        num2 = int(num2)

        #Match para ver que operador fue usado
        match operator:
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "/":
                if num2 == 0:
                    self.lbl_result.setText("Resultado indefinido")
                    self.result_status = True
                    return
                else:
                    result = num1 / num2
            case "*":
                result = num1 * num2
            case _:
                return
        
        self.lbl_result.setText(str(result))
        self.result_status = True


    def input_showcase(self, value):
        showcased_inputs = self.lbl_input.text()
        operators = {"+", "-", "*", "/"}
        
        #Esto chequea si ya se hizo una operacion y, en caso de que sea asi, borra todo en el label para la siguiente operacion.
        if self.result_status:
            if value not in operators:
                self.lbl_input.setText(value)
                self.lbl_result.clear()
                self.result_status = False
                return
            else:
                self.result_status = False
                return
        
        #Todo este if hace la logica para la escritura, detecta los operadores e intenta que no se escriban post otro operador o por si solos.
        if showcased_inputs == "0" and value not in operators:
            self.lbl_input.setText(value)
        elif value in operators:
            partes = showcased_inputs.strip().split()
            if partes[-1] not in operators:
                self.lbl_input.setText(showcased_inputs + " " + value + " ")
            else:
                return
        else:
            self.lbl_input.setText(showcased_inputs + value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    CalcApp = CalQLaterApp()
    CalcApp.show()
    sys.exit(app.exec_())

