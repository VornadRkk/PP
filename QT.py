
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication,QMainWindow,QInputDialog,QFileDialog,QTextEdit,QLineEdit
from PyQt5.QtGui import QFont
import week
import year
import x_and_y
import function_data
import iterator_next

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.selected_csv_file = None
        self.text_edit = QTextEdit(self)
        self.setWindowTitle("Data")
        self.setGeometry(300,250,350,200)
        button_height = 40
        button_width = 200
        button_margin = 10
        self.create_data_week = QtWidgets.QPushButton("week_date",self)
        self.create_data_week.setGeometry(self.width() - button_width - button_margin, button_margin, button_width, button_height)
        self.create_data_week.clicked.connect(self.week_button_clicked)
        self.create_data_year = QtWidgets.QPushButton("year_date",self)
        self.create_data_year.setGeometry(self.create_data_week.x(), self.create_data_week.y() + button_height + button_margin, button_width, button_height)
        self.create_data_year.clicked.connect(self.year_button_clicked)
        self.create_x_and_y = QtWidgets.QPushButton("_x_and_y_date", self)
        self.create_x_and_y.setGeometry(self.create_data_week.x(), self.create_data_year.y() + button_height + button_margin, button_width, button_height)
        self.create_x_and_y.clicked.connect(self.x_and_y_button_clicked)
        self.create_function_data = QtWidgets.QPushButton("function_data", self)
        self.create_function_data.setGeometry(self.create_data_week.x(), self.create_x_and_y.y() + button_height + button_margin, button_width, button_height)
        self.create_function_data.clicked.connect(self.function_data_button_clicked)


    def week_button_clicked(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        week_data = week.process_week_data()
    def year_button_clicked(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        year_data = year.create_year()
    def x_and_y_button_clicked(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        x_and_y_data = x_and_y.create_x_and_y()

    def function_data_button_clicked(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.show_dialog_for_file()
        target_date = self.show_dialog_for_date()
        function_data_ = function_data.get_data_for_date(self.selected_csv_file[0],target_date)
        self.text_edit.clear()
        if function_data_ is not None:
            self.text_edit.append(f"Data for date {target_date}:")
            self.text_edit.append(str(function_data_))
        else:
            self.text_edit.append(f"No data found for date {target_date}")

    def show_dialog_for_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_name= file_dialog.getOpenFileName(self, 'Choose file', '', 'All Files (*)')
        if file_name:
            self.selected_csv_file = file_name
    def show_dialog_for_date(self):
        text, ok = QInputDialog.getText(self, 'input date', 'date')
        if ok:
            self.input_data = text
            return text

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    application()