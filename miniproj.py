'''

@author: Tudor Gabriela, Ilie Iulia
'''
from PyQt4 import QtGui,QtCore
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
    
    
    
   #  
   
   
   
   
    def initUi(self):
        
        
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
        



    # afisam regulile actiunii   


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




    # definim procesul de selectare  a nivelului jocului

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
        #clear everything already present in the layout
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
        #verify grid method.
        
        

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
        rules.setText("""What are the rules of Futoshiki?


    
        
