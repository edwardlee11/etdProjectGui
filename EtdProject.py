# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ed\Desktop\ETDProject.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import ue9
import LabJackPython
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    ip = "10.32.89.108"
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Start_button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_button.setGeometry(QtCore.QRect(200, 140, 81, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Start_button.setPalette(palette)
        self.Start_button.setStyleSheet("\n"
"rgb")
        self.Start_button.setObjectName("Start_button")
        self.Reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_button.setGeometry(QtCore.QRect(200, 300, 81, 41))
        self.Reset_button.setObjectName("Reset_button")
        self.PWM_Slider = QtWidgets.QSlider(self.centralwidget)
        self.PWM_Slider.setGeometry(QtCore.QRect(170, 200, 160, 22))
        self.PWM_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.PWM_Slider.setObjectName("PWM_Slider")
        self.PWM_Label = QtWidgets.QLabel(self.centralwidget)
        self.PWM_Label.setGeometry(QtCore.QRect(140, 200, 31, 16))
        self.PWM_Slider.setMaximum(65535)
        self.PWM_Label.setObjectName("PWM_Label")
        self.Title_Label = QtWidgets.QLabel(self.centralwidget)
        self.Title_Label.setGeometry(QtCore.QRect(130, -10, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Title_Label.setFont(font)
        self.Title_Label.setObjectName("Title_Label")
        self.Forward_button = QtWidgets.QPushButton(self.centralwidget)
        self.Forward_button.setGeometry(QtCore.QRect(80, 140, 81, 41))
        self.Forward_button.setObjectName("Forward_button")
        self.Reverse_button = QtWidgets.QPushButton(self.centralwidget)
        self.Reverse_button.setGeometry(QtCore.QRect(320, 140, 81, 41))
        self.Reverse_button.setObjectName("Reverse_button")
        self.Stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.Stop_button.setGeometry(QtCore.QRect(190, 240, 101, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Stop_button.setPalette(palette)
        self.Stop_button.setObjectName("Stop_button")
        self.labjackip_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.labjackip_text.setGeometry(QtCore.QRect(160, 90, 161, 31))
        self.labjackip_text.setObjectName("labjackip_text")
        self.labjack_label = QtWidgets.QLabel(self.centralwidget)
        self.labjack_label.setGeometry(QtCore.QRect(160, 70, 151, 20))
        self.labjack_label.setObjectName("labjack_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(110, 360, 47, 13))
        self.pass_label.setObjectName("pass_label")
        self.password_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.password_text.setGeometry(QtCore.QRect(160, 349, 161, 31))
        self.password_text.setObjectName("password_text")
        self.labjackip_button = QtWidgets.QPushButton(self.centralwidget)
        self.labjackip_button.setGeometry(QtCore.QRect(330, 92, 75, 31))
        self.labjackip_button.setObjectName("labjackip_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Start_button.setText(_translate("MainWindow", "Start"))
        self.Reset_button.setText(_translate("MainWindow", "Reset"))
        self.PWM_Label.setText(_translate("MainWindow", "PWM"))
        self.Title_Label.setText(_translate("MainWindow", " Motor Controller"))
        self.Forward_button.setText(_translate("MainWindow", "Forward"))
        self.Reverse_button.setText(_translate("MainWindow", "Reverse"))
        self.Stop_button.setText(_translate("MainWindow", "EMERGENCY STOP"))
        self.labjack_label.setText(_translate("MainWindow", "                LabJack Ip"))
        self.pass_label.setText(_translate("MainWindow", "Password"))
        self.labjackip_button.setText(_translate("MainWindow", "Enter"))


                #Clicks
        self.Start_button.clicked.connect(self.Start_btn)
        self.Reset_button.clicked.connect(self.Reset_btn)
        self.Forward_button.clicked.connect(self.Forward_btn)
        self.Reverse_button.clicked.connect(self.Reverse_btn)
        self.Stop_button.clicked.connect(self.EmergencyStop)
        self.labjackip_button.clicked.connect(self.connection)


        
    import ue9
    import LabJackPython
    #myUE9 = input("Enter ip address:",labjackip_text.gettext())
    #print(myUE9)
   
    def Start_btn(self):
        
        #import ue9
        #import LabJackPython
        myUE9 = ue9.UE9(ethernet=True,ipAddress = self.ip)    
        print("Motor Starting")
        fio_mask = 0b11111111
        fio_dir = 0b11111111
        fio_state = 0b11111110
        results = myUE9.feedback(FIOMask = fio_mask,FIODir = fio_dir, FIOState=fio_state)
        print(results["FIOState"])
        
      #  print(bin(results["FIOState"]))

    def Reset_btn(self):
        #import ue9
        #import LabJackPython
        myUE9 = ue9.UE9(ethernet=True,ipAddress = self.ip)    
        password = input("Reset Button Pressed Please Re-Enter Password: ")
        if(password == 'pass'):
            print("password accepted restarting motor")
        else:
            print("invalid password")
 
    def PWM(self):
        #import ue9
        #import LabJackPython
        myUE9 = ue9.UE9(ethernet=True,ipAddress = self.ip)    
        print("test")
        #DC = str(int((self.PWM_Slider.value()/65535)*100))
        
        #self.myUE9.timerCounter(TimerClockBase=1, TimerClockDivisor=1, Timer0Mode=0, NumTimersEnabled=1, UpdateConfig=1, Timer0Value=65535-10000)
        myUE9.timerCounter(TimerClockDivisor=1, UpdateConfig=1,
                               NumTimersEnabled=1, Counter0Enabled=False,
                               Counter1Enabled=True, TimerClockBase=0,
                               ResetTimer0=False, ResetTimer1=False,
                               ResetTimer2=False, ResetTimer3=False,
                               ResetTimer4=False, ResetTimer5=False,
                               ResetCounter0=False, ResetCounter1=False,
                               Timer0Mode=0, Timer0Value=self.PWM_Slider.value())
    def Forward_btn(self):
        #import ue9
        #import LabJackPython    
        myUE9 = ue9.UE9(ethernet=True, ipAddress=self.ip)
        fio_mask = 0b11111111
        fio_dir = 0b11111111
        fio_state = 0b11111010 #Pins 0,1,2 (010)
        
        results = myUE9.feedback(FIOMask = fio_mask,FIODir = fio_dir, FIOState=fio_state)
        print(bin(results["FIOState"]))
        print("Motor Rotating Forward")
        
    def Reverse_btn(self):
        #import ue9
        #import LabJackPython    
        myUE9 = ue9.UE9(ethernet=True,ipAddress = self.ip)    
        fio_mask = 0b11111111
        fio_dir = 0b11111111
        fio_state = 0b11111100 #Pins 0,1,2 (001)
        results = myUE9.feedback(FIOMask = fio_mask,FIODir = fio_dir, FIOState=fio_state)
        print(bin(results["FIOState"]))
        print("Motor Rotating in Reverse")
        
    def EmergencyStop(self):
        #import ue9
        #import LabJackPython    
        myUE9 = ue9.UE9(ethernet=True,ipAddress = self.ip)    
        fio_mask = 0b11111111
        fio_dir = 0b11111111
        fio_state = 0b11111001 #Pins 0 (1 to stop)
        results = myUE9.feedback(FIOMask = fio_mask,FIODir = fio_dir, FIOState=fio_state)
        print("EMERGENCY STOP PRESSED!")
        

    def connection(self):
        self.myUE9 = ue9.UE9(ethernet=True, ipAddress=self.labjackip.text())
        print(self.labjackip.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

