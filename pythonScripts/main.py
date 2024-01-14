import sys
from PyQt5.QTWidgets import QApplication, QWidget,QPushButton,QVBoxLayout,QLabel,QGraphicsDropShadowEffect
from PyQt5.QtGUi import QColor
class HelloCore2WebApp(QWidget):
    def __init__(self):

        super().__init__()  
        self.init_ui()

    def init_ui(self):
    #create button
        hello_button = QPushButton("Say Hello",self)
        hello_button.setStyleSheet("background-color:white;width:300px;height:30px;color:black;margin-top:100px;")

    #need to import
        shadow =QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0,0,0,150)) #set Shadow color and opacity

        shadow.setBlurRadius(10)
        hello_button.setGraphicsEffect(shadow)
    #call to button
        hello_button.clicked.connect(self.say_hello)

    #create the label to display message
        self.message_label = QLabel(self)

    #setup the layout
        layout = QVBoxLayout()
        layout.addWidget(hello_button)
        layout.addWidget(self.message_label)

    #set the layout for main window

        self.setLayout(layout)
    #setup mian window
        self.setWindowTitle("Hello,core2web")
        self.setGeometry(500,500,500,500)

    def say_hello(self):
        self.message_label.setText("Hello,core2web!")
        self.message_label.setStyleSheet("color:red;font-size:20px;margin-left:150px")

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = HelloCore2WebApp()
    window.show()
    sys.exit(app.exec_())


