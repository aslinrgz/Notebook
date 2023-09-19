import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QTextEdit, QVBoxLayout, QPushButton, QMessageBox
from notebook_python import Ui_MainWindow
import os

class notebookPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.notebook = Ui_MainWindow()
        self.notebook.setupUi(self)
        self.notebook.pushButton_kaydet.clicked.connect(self.kaydet)
        self.notebook.pushButton_ac.clicked.connect(self.ac)
        self.notebook.pushButton_sil.clicked.connect(self.sil)
    
    def kaydet(self):
        dosya_adi, _ = QFileDialog.getSaveFileName(self, "Dosya Kaydet", "", "Metin Dosyaları (*.txt);;Tüm Dosyalar (*)")
        if not dosya_adi:
            QMessageBox.warning(self,"Uyarı","Dosya adı boş bırakılamaz")
        else:
            try:
                with open(dosya_adi, "w", encoding="utf-8") as dosya:
                    dosya.write(self.notebook.textEdit.toPlainText())
                QMessageBox.information(self, "Bilgi", "Dosya başarıyla kaydedildi.")
            except Exception as hata:
                QMessageBox.critical(self, "Hata", "Dosya kaydedilirken bir hata oluştu:\n{}".format(str(hata)))
    
    def ac(self):
        dosya_adi, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Metin Dosyaları (*.txt);;Tüm Dosyalar (*)")
        if dosya_adi:
            if not os.path.exists(dosya_adi):
                QMessageBox.warning(self,"Uyarı","Seçilen dosya mevcut değil.")
            try:
                with open(dosya_adi, "r", encoding="utf-8") as dosya:
                    icerik = dosya.read()
                    self.notebook.textEdit_2.setPlainText(icerik)  
            except Exception as hata:
                QMessageBox.critical(self, "Hata", "Dosya açılırken bir hata oluştu:\n{}".format(str(hata)))
    
    def sil(self):
        self.notebook.textEdit_2.clear()
           


if __name__ == '__main__':
    app = QApplication([])
    pencere = notebookPage()
    pencere.show()
    app.exec_()

