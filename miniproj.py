'''
@author: Tudor Gabriela, Ilie Iulia
'''
import QtGui,QtCore
import sys
import random

# definim clasa programului si ceea ce contine aceasta ( fereastra principala, matricea jocului, grila jocului, numarul de patrate)

class Futoshiki_interface(QtGui.QApplication):
    main_window=""  
    game_matrix=""
    game_grid=""
    nrsquares=""
     
    # metoda constructor(definim programul)
 
    def __init__(self, args):  
        
        # Inițializează sistemul de ferestre și construiește un obiect aplicație cu argumente în linia de comandă argv.
        QtGui.QApplication.__init__(self, args) 
        self.initUi()  // Delegăm crearea interfetei utilizatorului la metoda initUI().
    
    def initUi(self):
         #  definim metoda initUI(self) 
         #  definim functiile ferestrei principale, bara de meniu si optiunea de joc nou
        
        self.main_window=QtGui.QFrame()
        self.main_window.setLayout(QtGui.QVBoxLayout())
        self.main_window.setFixedSize(600,600)
        self.main_window.setWindowTitle('Futoshiki')
        
        menubar=QtGui.QMenuBar(self.main_window)
        app_menu=QtGui.QMenu('Game',menubar)
        help_menu=QtGui.QMenu('Help',menubar)
    
        menubar.addMenu(app_menu)
        menubar.addMenu(help_menu)
        
        startgame_action = QtGui.QAction( '&Start a new game', self)      
        startgame_action.triggered.connect(self.selectLevel)
        startgame_action.setShortcut('F5')
        app_menu.addAction(startgame_action)
        



    # afisam regulile actiunii, meniul de ajutor, optiunea hint, imagini si ecranul principal
        showrules_action=QtGui.QAction('&Rules',self)
        showrules_action.triggered.connect(self.showrules)
        help_menu.addAction(showrules_action) 
        
        showtips_action=QtGui.QAction('Tips',self)
        showtips_action.triggered.connect(self.showtips)
        help_menu.addAction(showtips_action)
        
        imagelabel=QtGui.QLabel(self.main_window)
        imagelabel.setPixmap(QtGui.QPixmap('fimage.jpg'))
        imagelabel.setScaledContents(True)
        
        self.main_window.layout().addWidget(imagelabel)
        
        self.main_window.layout().setMenuBar(menubar)
        self.main_window.show()

    # definim procesul de selectare  a nivelului jocului(aplicam for)

    def selectLevel(self):
        for i in reversed(range(self.main_window.layout().count())):
            try: 
                self.main_window.layout().itemAt(i).widget().setParent(None)
            except:
                 for j in reversed(range(self.game_grid.count())):
                    self.game_grid.itemAt(j).widget().setParent(None)
        easy_button=QtGui.QPushButton('Easy',self.main_window)
        
        medium_button=QtGui.QPushButton('Medium',self.main_window)
        hard_button=QtGui.QPushButton('Hard',self.main_window)
        
        easy_button.clicked.connect(self.levelclick)
        medium_button.clicked.connect(self.levelclick)
        hard_button.clicked.connect(self.levelclick)
        self.main_window.layout().addWidget(easy_button)
        self.main_window.layout().addWidget(medium_button)
        self.main_window.layout().addWidget(hard_button)
        
        

    def levelclick(self):
        sender=self.sender()
        if(sender.text()=='Easy'):
            self.newgameclick(16)
        elif(sender.text()=='Medium'):
            self.newgameclick(19)
        else:
            self.newgameclick(22)
    def newgameclick(self,level):

        #stergem orice este deja prezent in schema
        for i in reversed(range(self.main_window.layout().count())):
            try: 
                self.main_window.layout().itemAt(i).widget().setParent(None)
            except:
                 for j in reversed(range(self.game_grid.count())):
                    self.game_grid.itemAt(j).widget().setParent(None)
               
                
        self.game_matrix=readfile('futoshiki1.txt')         
                
        self.game_grid=generategrid(self.game_matrix,level
                                    ,self.main_window)
        self.main_window.layout().addLayout(self.game_grid)
        verify_button=QtGui.QPushButton('Verify',self.main_window)
        verify_button.clicked.connect(self.verifygrid)
        self.main_window.layout().addWidget(verify_button)
        
      
    def verifygrid(self):
        #verificam metoda grid.
        
        numbermat=[[0 for x in range(5)] for y in range(5)]
        aidlist=[0 for z in range(25)]
        aidlist1=[0 for z in range(25)]
       
        row=0
        column=0
        i=0
        j=0
        k=0
        
        for i in range(9):
            for j in range(9):
                
                try:
                    int(self.game_matrix[i][j])
                    aidlist[k]=self.game_matrix[i][j]
                    k=k+1
                except ValueError:
                    ok=True
                    
        k=0
        for row in range(5):
            for column in range(5):
                numbermat[row][column]=aidlist[k]
                k=k+1
        k=0
        for z in range(0,self.game_grid.count()):
            try:
                int(self.game_grid.itemAt(z).widget().toPlainText())
                aidlist1[k]=self.game_grid.itemAt(z).widget().toPlainText().strip(" ")
                k=k+1
            except:
                ok=True
        
        verifymatrix=[[0 for x in range(5)] for y in range(5)]
        k=0
        for i in range(0,5):
            for j in range(0,5):
                verifymatrix[i][j]=aidlist1[k]
                k=k+1
        
        result=QtGui.QMessageBox(self.main_window)
        if verifymatrix==numbermat:
            
            result.setText('You have completed this puzzle!Great job!')
            
        else:
            result.setText('The solution you have found is not correct.Try again!')
            
        for i in range(0,9,2):
           for j in range(0,9,2):
               
                self.game_grid.itemAtPosition(i,j).widget().setStyleSheet('color:black')
        for i in range(0,9,2):
           for j in range(0,9,2):
               if self.game_matrix[i][j]!=self.game_grid.itemAtPosition(i,j).widget().toPlainText().strip(' '):
                   x=self.game_grid.itemAtPosition(i, j).widget().toPlainText().strip(' ')
                   
                   self.game_grid.itemAtPosition(i,j).widget().setStyleSheet('color:red')
        
        
        result.setFixedSize(10,10)
        
        result.setWindowTitle('Result')
        result.show()
             
    def showrules(self):
        rulesdialog=QtGui.QDialog(self.main_window)
        rules=QtGui.QTextBrowser(rulesdialog)
        rules.setText("""Care sunt regulile jocului Futoshiki?

    Futoshiki este un joc puzzle amuzant. Regulile jocului Futoshiki sunt urmatoarele:
Incepi cu o grila de forma 5x5, sau 7 x 7 pentru puzzle-uri Futoshiki mai mari..
Scopul este de a umple fiecare rând și coloană cu numere de la 1 – 5, fiecare aparand o singura dată (presupunând o grilă 5x5) - această regulă este familiară din sudoku.
Cu toate acestea, nu există regiuni caseta ca în sudoku. Marea diferență sunt  semnele de inegalitate, iar jucatorul  trebuie să se supună acestora în răspunsurile  pe care le va da. De exemplu, dacă avem  o celulă mai mare decât cea de lângă ea, atunci știm ca celula din stânga nu poate fi  1, iar celula din dreapta nu poate fi 5.
Utilizati  logica pentru a deduce unde merge fiecare  număr pentru a rezolva puzzle-ul.
""")
        rules.show()
        rules.setFixedSize(500,200)
        rulesdialog.show()
        rulesdialog.setWindowTitle("Futoshiki rules")
        
    def showtips(self): 
        tipsdialog=QtGui.QDialog(self.main_window) 
        tips=QtGui.QTextBrowser(tipsdialog)
        tips.setText("""Rezolvarea puzzle-ului necesită o combinație de tehnici logice.  Numerele în fiecare rând și coloană limiteaza numărul de valori posibile pentru fiecare poziție, așa cum fac inegalitățile.
Odată ce masa de posibilități a fost determinată, o tactică crucială pentru a rezolva puzzle-ului implică "eliminarea AB", în care diverse  subseturi sunt identificate într-un rând al cărui interval de valori pot fi determinate. De exemplu, în cazul în care primele două pătrate într-un rând trebuie să conțină 1 sau 2, atunci aceste numere pot fi excluse din pătratele rămase. În mod similar, în cazul în care primele trei pătrate trebuie să conțină 1 sau 2; 1 sau 3; și 1 sau 2 sau 3, atunci cei rămași trebuie să conțină alte valori (4 și 5 într-un puzzle 5x5).
O altă tehnică importantă este de a lucra prin gama de posibilități în inegalități deschise. O valoare de pe o parte a unei inegalități determină o alta, care apoi poate fi prelucrata prin intermediul puzzle-ului până când se ajunge la o contradicție, iar prima valoare este exclusă.
In plus, multe puzzle-uri Futoshiki sunt promise să posede soluții unice
""")
        tips.show()
        tips.setFixedSize(500,200)
        tipsdialog.show()
        tipsdialog.setWindowTitle("Tips & Tricks")
        
  
# Putem face de fapt ceva în cazul în care acest scenariu este rulat independent, astfel încât să putem testa 
# aplicatia noasra, dar, de asemenea, suntem capabili de a importa acest program fără a fi rulat vreun cod.
def readfile(filename):       
        matric=[[0 for j in range(9)] for i in range(9)]
        with open(filename, mode="r",encoding="utf-8") as my_file:
            animals = my_file.read().strip('\n').split(" ")
            
        k=0  
        for i in range(0,9):
            for j in range(0,9):
                matric[i][j]=animals[k].rstrip('\n')
                k=k+1
        return matric
def generategrid(matrice,nrsquares,parent):
    
    matrice=readfile("futoshiki1.txt")
    xi=0
    
    while(xi<nrsquares):
        
        x=random.randrange(0,10,2)
        y=random.randrange(0,10,2)
        if matrice[x][y]!="0":
                matrice[x][y]="0"
                xi=xi+1
                      
    grid=QtGui.QGridLayout()
        
    for i in range (0,9):
        for j in range (0,9):
            try:
                 
                int(matrice[i][j])
                    
                box=QtGui.QTextEdit(matrice[i][j])
                box.setAlignment(QtCore.Qt.AlignCenter)
                if int(matrice[i][j])==0:
                    box.setText("")
                    
                    box.setFixedSize(40,40)
   
                else:
                    box.setReadOnly(True)
                    
                        
                    box.setFixedSize(40,40)
                box.setFont(QtGui.QFont("Courier",16))    
                grid.addWidget(box,i,j)
                    
            except ValueError:
                if matrice[i][j]=='|' or matrice [i][j]=='-':
                    label=QtGui.QTextEdit(parent)
                   
                    label.setReadOnly(True)
                    label.setFixedSize(40,40)
                    label.setStyleSheet('background-color:rgba(139,0,0,0);border:0px')
                        
                else:
                        
                    label=QtGui.QTextEdit(parent)
                    label.setText(matrice[i][j])
                   
                    label.setAlignment(QtCore.Qt.AlignCenter)
                    label.setReadOnly(True)
                    label.setFixedSize(40,40)
                    label.setStyleSheet('background-color:rgba(139,0,0,0);border:0px;font-size:20px')
                
                grid.addWidget(label,i,j)
                
    return grid

def printGrid(grid):
    for i in range(0,5):
        for j in range(0,5):
            if i==5:
                print(grid[i][j])
            else:
                print(grid[i][j],end="")
if __name__ == "__main__":
    Game = Futoshiki_interface(sys.argv)
    sys.exit(Game.exec_())
