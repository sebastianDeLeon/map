from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from algoritmo import prueba_UCS, empty_map
from geopy.geocoders import Nominatim

class Map_Displayer():

    def __init__(self, ady):
        self.ady = ady
        empty_map()
        self.window = QWidget()
        self.window.setWindowTitle("PROYECTO - MAP ROUTING")

        
        
        #UI
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.start = QTextEdit()
        self.start.setMaximumHeight(28)

        self.partida = QLabel("Punto De partida")
        self.destino = QLabel("Punto de destino")

        self.meta = QTextEdit()
        self.meta.setMaximumHeight(28)


        #search button
        self.search_btn = QPushButton("Search")
        self.search_btn.setMaximumHeight(30)
        self.search_btn.clicked.connect(lambda: self.search(
            self.start.toPlainText(), 
            self.meta.toPlainText()))


        #Reset Button
        self.reset_btn = QPushButton("Reset")
        self.reset_btn.setMaximumHeight(30)
        self.reset_btn.clicked.connect(lambda: self.reset())

        self.horizontal.addWidget(self.partida)
        self.horizontal.addWidget(self.start)
        self.horizontal.addWidget(self.destino)
        self.horizontal.addWidget(self.meta)
        self.horizontal.addWidget(self.search_btn)
        self.horizontal.addWidget(self.reset_btn)

        self.start.move(50, 50)

        self.browser  = QWebEngineView()

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        
        self.browser.setUrl(QUrl("file:///C:/Users/Sebastian/Documents/ITLA/7to periodo/Inteligencia artificial/OpenStreetMap-IA/index.html"))

        self.window.setLayout(self.layout)
        self.window.show()

    def search(self, start, meta):
        
        try:
            geolocator = Nominatim(user_agent="OpenStreen")
        
            ubicacionI = (geolocator.geocode("Santo Domingo Este, "+start))
            start = (str(ubicacionI.latitude)+", "+str(ubicacionI.longitude))
            ubicacionF = (geolocator.geocode("Santo Domingo Este, "+meta))
            meta = (str(ubicacionF.latitude)+", "+str(ubicacionF.longitude))
            
            origen = tuple([float(i) for i in start.split(",")])
            goal = tuple([float(i) for i in meta.split(',')])
            if origen in self.ady and goal in self.ady:
                prueba_UCS(origen, goal, self.ady)
            else:

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Es posible que estes pasando un nodo inexistente en este mapa")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

            # Debe modificar la URL con la URL absoluta de su máquina (abrir index.html y copiar ruta absoluta)
            self.browser.setUrl(QUrl("file:///C:/Users/Sebastian/Documents/ITLA/7to periodo/Inteligencia artificial/OpenStreetMap-IA/index.html"))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Es posible que estes pasando un nodo inexistente en este mapa")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        
    
    def reset(self):
        self.start.setText('')
        self.meta.setText('')
        empty_map()

         # Debe modificar la URL con la URL absoluta de su máquina (abrir index.html y copiar ruta absoluta)
        self.browser.setUrl(QUrl("file:///C:/Users/Sebastian/Documents/ITLA/7to periodo/Inteligencia artificial/OpenStreetMap-IA/index.html"))



