#Ex01-bouton
#Quand on clique sur le bouton, on change le nom du label par Bonjour

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex04-bouton.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la méthode boutonOK
        self.pushButton.clicked.connect(self.boutonOk)
        #Quand on clique sur la checkbox, on appelle la méthode chkBox
        self.checkBox.stateChanged.connect(self.chkBox)
        self.show()             #affiche la fenêtre MainWindows


    def boutonOk(self):
        print('bouton cliqué')
        chk=self.checkBox.isChecked()    #récupére l'état du checkBox
        print('chk',chk,type(chk)) #affiche dans la console l'état du check box et le type
        txt=self.lineEdit.text()    #récupère le texte de lineEdit
        print('texte saisi:',txt,type(txt)) #affiche dans la console le texte et le type
        b=self.spinBox.value()  #récupère le nombre de la spinbox
        print('valeur de la spin box',b) #‗affiche cette valeur dans la console
        if txt.isnumeric():     #le texte est-il un chiffre ?
            a=int(txt)          #conversion en entier
            a=a+b              #ajoute la valeur b
            self.label.setText(str(a)) #affiche le résultat
        else:
            self.label.setText("nombre svp")

    def chkBox(self):
        chk=self.checkBox.isChecked()   #récupére l'état du checkBox
        if chk==True:
            self.label.setText("checkBox True") #affiche le résultat dans le label
        else:
            self.label.setText("checkBox False") #affiche le résultat dans le label


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()