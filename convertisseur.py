

'''''les bib utilisè sont :'''
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(462, 600)
        MainWindow.setStyleSheet("")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 380, 171, 61))
        self.lineEdit_5.setStyleSheet("background-color:rgb(255, 189, 205);\n"
"color:#00000;\n"
"border-style:groove;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:blue; \n"
"font:bold 15px;\n"
"padding:6px;\n"
"min_width:10px;\n"
"")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(310, 380, 121, 41))
        self.comboBox_5.setStyleSheet("background-color:rgb(255, 189, 205);\n"
"color:black;\n"
"border-style:groove;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:blue; \n"
"font:italic 17px;\n"
"padding:6px;\n"
"min_width:10px;\n"
"")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 130, 171, 61))
        self.lineEdit_4.setStyleSheet("background-color:rgb(255, 189, 205);\n"
"color:#0000;\n"
"border-style:groove;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:blue; \n"
"font:bold 15px;\n"
"padding:6px;\n"
"min_width:10px;\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(300, 130, 121, 41))
        self.comboBox_4.setStyleSheet("background-color:rgb(255, 189, 205);\n"
"color:black;\n"
"border-style:groove;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:blue; \n"
"font:italic 17px;\n"
"padding:6px;\n"
"min_width:10px;\n"
"")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 291))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0#783aff, stop:1 #55ffff);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0#783aff, stop:1 #55ffff);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(380, 260, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Button1.setFont(font)
        self.Button1.setStyleSheet("color:blue;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:blue; \n"
"font:bold 30px;\n"
"padding:6px;\n"
"min_width:10px;\n"
"background-color: #55ffff;")
        self.Button1.setObjectName("Button1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 19, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #0000; font-size: 29px; font-family: blood, serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff;")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 540, 461, 31))
        self.label_3.setStyleSheet("background:#777; text-align: center; padding:5%;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(84, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 340, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.lineEdit_5.raise_()
        self.comboBox_5.raise_()
        self.comboBox_4.raise_()
        self.lineEdit_4.raise_()
        self.Button1.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Button1.clicked.connect(self.pressed)                       #on doit lieè le boutton a la fonction ou il ia notre traitement des donnè entrè par l'utilisateur''''

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "convertisseur"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "binaire"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "decimal"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "octal"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "hexadecimal"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "binaire"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "decimal"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "octal"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "hexadecimal"))
        self.Button1.setText(_translate("MainWindow", "↑↓"))
        self.Button1.setShortcut(_translate("MainWindow", "Return"))
        self.label_2.setText(_translate("MainWindow", "Convertisseur"))
        self.label_3.setText(_translate("MainWindow", "© Copyright 2020"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nombre à convertir :</span></p></body></html>"))
        self.label_4.adjustSize()
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Resultat :</span></p></body></html>"))
        self.label_5.adjustSize()
    def num_convert(from_number, from_base, to_base):
        """Convert from_number to another base number."""
        to_number = 0
        power = 0
        while from_number > 0:
            to_number += from_base ** power * (from_number % to_base)
            from_number //= to_base
            power += 1
        return to_number

    def pressed(self):                                                                        #la fonction ou il i a notre traitement des donnè entrè par l'utilisateur
        listehexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        listebinaire = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011","1100", "1101", "1110", "1111"]

        def hexabinaire(string):                                                           #une fonction qui convertie de l'hexadecimal au binaire
            res = ""
            for x in range(len(string)):
                i = listehexa.index(string[x])
                res = res + listebinaire[i]
            return res
        def binairehexa(string):                                                            #une fonction qui convertie de l'binaire au binaire hexadecimal
            liste = []
            res = ""
            while len(string) > 4:
                liste = liste + [string[-4:]]
                string = string[:-4]
            liste = liste + [string]
            while len(liste[-1]) != 4:
                liste[-1] = "0" + liste[-1]
            for x in range(len(liste)):
                i = listebinaire.index(liste[x])
                liste[x] = listehexa[i]
            while liste != []:
                res = res + liste[-1]
                liste = liste[:-1]
            return res
        def num_convert(from_number, from_base, to_base):
            #Convert from_number to another base number.
            to_number = 0
            power = 0
            while from_number > 0:
                to_number += from_base ** power * (from_number % to_base)
                from_number //= to_base
                power += 1
            return to_number
        #recuperer les donnè saisie par l'utilisateur
        x = self.comboBox_4.currentText()
        y = self.comboBox_5.currentText()
        z = self.lineEdit_4.text()
        #tester les donnè saisie par l'utilisateur
        if x == "binaire":
            l = ["0", "1"]
            c = 0
            for i in range(len(z)):
                if z[i] not in l:
                    c = 1
                    break
                else:
                    pass
            if c == 1:
                                        # afficher un erreur
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('veuillez saisir un nombre valide')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                if y == "binaire":
                    self.lineEdit_5.setText(z)
                elif y == "decimal":
                    z=int(z)
                    self.lineEdit_5.setText(str(num_convert(z,2,10)))
                elif y == "octal":
                    z=int(z)
                    b=num_convert(z,2,10)
                    b=int(b)
                    k=num_convert(b,10,8)
                    self.lineEdit_5.setText(str(k))

                elif y =="hexadecimal":
                    self.lineEdit_5.setText(binairehexa(z))

        elif x == "decimal":
# tester les donnè saisie par l'utilisateur
            l = ["0", "1","2","3","4","5","6","7","8","9"]
            c = 0
            for i in range(len(z)):
                if z[i] not in l:
                    c = 1
                    break
                else:
                    pass

            if c == 1:
# afficher un erreur
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('veuillez saisir un nombre valide')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:

                if y == "decimal":
                    self.lineEdit_5.setText(str(z))
                elif y=="binaire":
                    self.lineEdit_5.setText(str(num_convert(int(z),10,2)))
                elif y=="octal":
                    self.lineEdit_5.setText(str(num_convert(int(z),10,8)))
                elif y=="hexadecimal":
                    b=num_convert(int(z),10,2)
                    self.lineEdit_5.setText(binairehexa(str(b)))
        elif x == "octal":
# tester les donnè saisie par l'utilisateur
            l = ["0", "1", "2", "3", "4", "5", "6", "7"]
            c = 0
            for i in range(len(z)):
                if z[i] not in l:
                    c = 1
                    break
                else:
                    pass

            if c == 1:
# afficher un erreur
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('veuillez saisir un nombre valide')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:

                if y=="octal":
                    self.lineEdit_5.setText(str(z))
                elif y=="binaire":
                    b=num_convert(int(z),8,10)
                    self.lineEdit_5.setText(str(num_convert(b,10,2)))
                elif y=="decimal":
                    self.lineEdit_5.setText(str(num_convert(int(z),8,10)))
                elif y=="hexadecimal":
                    b=num_convert(int(z),8,10)
                    p=num_convert(b,10,2)
                    self.lineEdit_5.setText(str(binairehexa(str(p))))
        elif x== "hexadecimal":
# tester les donnè saisie par l'utilisateur
            l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","A","B","C","E","F","D"]
            c = 0
            for i in range(len(z)):
                if z[i] not in l:
                    c = 1
                    break
                else:
                    pass

            if c == 1:
# afficher un erreur
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('veuillez saisir un nombre valide')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                if y=="hexadecimal":
                    self.lineEdit_5.setText(z)
                elif y=="binaire":
                    self.lineEdit_5.setText(str(hexabinaire(z)))
                elif y=="decimal":
                    b=hexabinaire(z)
                    self.lineEdit_5.setText(str(num_convert(int(b),2,10)))
                elif y=="octal":
                    b=hexabinaire(z)
                    c=num_convert(int(b),2,10)
                    self.lineEdit_5.setText(str(num_convert(c,10,8)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
