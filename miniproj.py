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
        
