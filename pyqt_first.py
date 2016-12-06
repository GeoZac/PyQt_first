from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "tax_calc.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.CalculateTax)
    
    def CalculateTax(self):
        price = int(self.price_box.toPlainText())
        tax = (self.tax_rate.value())
        calc_tax = ((tax / 100) * price)
        total_price = price  + calc_tax
        total_price_string = str(total_price)
        price_str = str(price)
        tax_str = str(calc_tax)
        self.textEdit_2.setText(price_str)
        self.textEdit.setText(tax_str)
        self.results_window.setText(total_price_string)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())