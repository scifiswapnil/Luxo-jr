#########################################################################################################

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from nodemcu import Ui_MainWindow
import sys, os
import serial
import paho.mqtt.client as mqtt

#########################################################################################################





#########################################################################################################
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("cvd")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.username_pw_set("rrarungx", "r8iTK4SHmgId")
client.connect("m13.cloudmqtt.com",18602, 60)
client.on_connect = on_connect
client.on_message = on_message
#client.loop_forever()


#########################################################################################################

class MyApp(QMainWindow, Ui_MainWindow):
    parse_triggered = pyqtSignal()
    def __init__(self, parent=None, name=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)

        self.btn.clicked.connect(self.on_button)

        self.servo_slider_1.valueChanged.connect(self.slider_valuechange_1)
        self.servo_slider_2.valueChanged.connect(self.slider_valuechange_2)
        self.servo_slider_3.valueChanged.connect(self.slider_valuechange_3)
        self.servo_slider_4.valueChanged.connect(self.slider_valuechange_4)
        self.servo_slider_5.valueChanged.connect(self.slider_valuechange_5)
        self.servo_slider_6.valueChanged.connect(self.slider_valuechange_6)
        self.servo_slider_7.valueChanged.connect(self.slider_valuechange_7)
        self.servo_slider_8.valueChanged.connect(self.slider_valuechange_8)
        self.servo_slider_9.valueChanged.connect(self.slider_valuechange_9)
        self.servo_slider_10.valueChanged.connect(self.slider_valuechange_10)

        self.servo_spinBox_1.valueChanged.connect(self.spinbox_valuechange_1)
        self.servo_spinBox_2.valueChanged.connect(self.spinbox_valuechange_2)
        self.servo_spinBox_3.valueChanged.connect(self.spinbox_valuechange_3)
        self.servo_spinBox_4.valueChanged.connect(self.spinbox_valuechange_4)
        self.servo_spinBox_5.valueChanged.connect(self.spinbox_valuechange_5)
        self.servo_spinBox_6.valueChanged.connect(self.spinbox_valuechange_6)
        self.servo_spinBox_7.valueChanged.connect(self.spinbox_valuechange_7)
        self.servo_spinBox_8.valueChanged.connect(self.spinbox_valuechange_8)
        self.servo_spinBox_9.valueChanged.connect(self.spinbox_valuechange_9)
        self.servo_spinBox_10.valueChanged.connect(self.spinbox_valuechange_10)

        self.ser_label.setDisabled(True)
        self.cnn_status.setDisabled(True)
        self.ser_comboBox.setDisabled(True)
        self.spd_comboBox.setDisabled(True)
        self.ser_comboBox.setDisabled(True)

        self.ser_checkBox.stateChanged.connect(self.ser_state)
        self.ser_comboBox.addItems([])
        self.spd_comboBox.addItems(["115200", "9600"])

        self.actionExit_.triggered.connect(self.quit)

        count=0;

        x = os.listdir('/dev/')
        for list in x:
            if list[:4] == "ttyU" or list[:4] == "ttyA" :
                self.ser_comboBox.addItem(list)
                count =count +1

        if count == 0:
            self.ser_checkBox.setDisabled(True)

#########################################################################################################

    def quit(self):
        QCoreApplication.instance().quit()

    def ser_state(self):
        if self.ser_checkBox.checkState()==2:
            self.ser_label.setDisabled(False)
            self.cnn_status.setDisabled(False)
            self.ser_comboBox.setDisabled(False)
            self.spd_comboBox.setDisabled(False)
            self.ser_comboBox.setDisabled(False)
        else:
            self.ser_label.setDisabled(True)
            self.cnn_status.setDisabled(True)
            self.ser_comboBox.setDisabled(True)
            self.spd_comboBox.setDisabled(True)
            self.ser_comboBox.setDisabled(True)
            del self.ser

    def on_button(self):
        if self.ser_checkBox.checkState()==2:
            self.ser = connect(self)
        else:
            self.statusbar.showMessage("Nothing pressed")

#########################################################################################################

    def slider_valuechange_1(self):
        self.servo_spinBox_1.setValue(self.servo_slider_1.value())
        changer(str(self.servo_slider_1.objectName()),self.servo_slider_1.value(),self)

    def slider_valuechange_2(self):
        self.servo_spinBox_2.setValue(self.servo_slider_2.value())
        changer(str(self.servo_slider_2.objectName()),self.servo_slider_2.value(),self)

    def slider_valuechange_3(self):
        self.servo_spinBox_3.setValue(self.servo_slider_3.value())
        changer(str(self.servo_slider_3.objectName()),self.servo_slider_3.value(),self)

    def slider_valuechange_4(self):
        self.servo_spinBox_4.setValue(self.servo_slider_4.value())
        changer(str(self.servo_slider_4.objectName()),self.servo_slider_4.value(),self)

    def slider_valuechange_5(self):
        self.servo_spinBox_5.setValue(self.servo_slider_5.value())
        changer(str(self.servo_slider_5.objectName()),self.servo_slider_5.value(),self)

    def slider_valuechange_6(self):
        self.servo_spinBox_6.setValue(self.servo_slider_6.value())
        changer(str(self.servo_slider_6.objectName()),self.servo_slider_6.value(),self)

    def slider_valuechange_7(self):
        self.servo_spinBox_7.setValue(self.servo_slider_7.value())
        changer(str(self.servo_slider_7.objectName()),self.servo_slider_7.value(),self)

    def slider_valuechange_8(self):
        self.servo_spinBox_8.setValue(self.servo_slider_8.value())
        changer(str(self.servo_slider_8.objectName()),self.servo_slider_8.value(),self)

    def slider_valuechange_9(self):
        self.servo_spinBox_9.setValue(self.servo_slider_9.value())
        changer(str(self.servo_slider_9.objectName()),self.servo_slider_9.value(),self)

    def slider_valuechange_10(self):
        self.servo_spinBox_10.setValue(self.servo_slider_10.value())
        changer(str(self.servo_slider_10.objectName()),self.servo_slider_10.value(),self)

#########################################################################################################

    def spinbox_valuechange_1(self):
        self.servo_slider_1.setValue(self.servo_spinBox_1.value())

    def spinbox_valuechange_2(self):
        self.servo_slider_2.setValue(self.servo_spinBox_2.value())

    def spinbox_valuechange_3(self):
        self.servo_slider_3.setValue(self.servo_spinBox_3.value())

    def spinbox_valuechange_4(self):
        self.servo_slider_4.setValue(self.servo_spinBox_4.value())

    def spinbox_valuechange_5(self):
        self.servo_slider_5.setValue(self.servo_spinBox_5.value())

    def spinbox_valuechange_6(self):
        self.servo_slider_6.setValue(self.servo_spinBox_6.value())

    def spinbox_valuechange_7(self):
        self.servo_slider_7.setValue(self.servo_spinBox_7.value())

    def spinbox_valuechange_8(self):
        self.servo_slider_8.setValue(self.servo_spinBox_8.value())

    def spinbox_valuechange_9(self):
        self.servo_slider_9.setValue(self.servo_spinBox_9.value())

    def spinbox_valuechange_10(self):
        self.servo_slider_10.setValue(self.servo_spinBox_10.value())

#########################################################################################################

def changer(pin , data, self):
    try:
        if self.ser != None:
            print("pin", pin[-1:] , "data" , data , sep=":")
            temp1 = bytearray(pin[-1:],'utf8')
            temp2 = bytearray("#"+str(data),'utf8')
            ptr1 = bytearray("$",'utf8')
            self.ser.write(temp1+temp2+ptr1)
            client.publish("svd", "pin : " + pin[-1:] + " data : " + str(data), qos=0, retain=False)
    except AttributeError:
        self.statusbar.showMessage("No Connection")
        print("values error")


def connect(self):
    try:
        ser=serial.Serial("/dev/"+str(self.ser_comboBox.currentText()),str(self.spd_comboBox.currentText()))
        self.statusbar.showMessage("Connection Successful",2000)
        self.cnn_status.setText("Connected")
    except IOError:
        self.statusbar.showMessage("Permission Denied",2000)
        self.cnn_status.setText("Not Connected")
    return ser

#########################################################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


#########################################################################################################
