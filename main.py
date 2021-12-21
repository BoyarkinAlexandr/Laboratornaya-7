import psycopg2
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QAbstractScrollArea, QVBoxLayout, QHBoxLayout, \
    QTableWidget, QGroupBox, QTableWidgetItem, QPushButton, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Timetable")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_timetable_tab()
        self._create_teachers_tab()
        self._create_subjects_tab()


    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="bot",
                                     user="alexandrboyarkin",
                                     password="1234",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_timetable_tab(self):
        self.timetable_tab = QWidget()
        self.tabs.addTab(self.timetable_tab, "Timetable")


        self.timetable_gbox = QGroupBox("Timetable")


        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.timetable_gbox)

        self._create_timetable_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.timetable_tab.setLayout(self.svbox)

    def _create_timetable_table(self):
        self.timetable_table = QTableWidget()
        self.timetable_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.timetable_table.setColumnCount(8)
        self.timetable_table.setHorizontalHeaderLabels(["Id","Day","Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.timetable_table)
        self.timetable_gbox.setLayout(self.mvbox)

    def _update_timetable_table(self):
        self.timetable_table.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable")
        records = list(self.cursor.fetchall())

        self.timetable_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table.setItem(i, 0,QTableWidgetItem(str(r[0])))
            self.timetable_table.setItem(i, 1,QTableWidgetItem(str(r[1])))
            self.timetable_table.setItem(i, 2,QTableWidgetItem(str(r[2])))
            self.timetable_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table.setCellWidget(i, 6, joinButton)
            self.timetable_table.setCellWidget(i, 7, deleteButton)


            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_table(num))
        self.insertbutton = QPushButton("Insert")
        self.timetable_table.setCellWidget(len(records),6, self.insertbutton)
        self.timetable_table.resizeRowsToContents()


    def _change_day_from_table(self, rowNum):
        row = list()
        for column in range(self.timetable_table.columnCount()):
            try:
                row.append(self.timetable_table.item(rowNum, column).text())
            except:
                row.append(None)
            try:
                self.cursor.execute("UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s", (row[1],row[2],row[3],row[4],row[5],row[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Something wrong!")

    def _delete_day_from_table(self, rowNum):
        row = list()
        for column in range(self.timetable_table.columnCount()):
            try:
                row.append(self.timetable_table.item(rowNum, column).text())
            except:
                row.append(None)
            try:
                self.cursor.execute("Delete from timetable where id=%s",
                                    (row[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Something wrong!")



    #Таблица учителей
    def _create_teachers_tab(self):

        self.teachers_tab = QWidget()
        self.tabs.addTab(self.teachers_tab, "Teachers")

        self.teachers_gbox = QGroupBox("Teachers")

        self.svbox3 = QVBoxLayout()
        self.shbox4 = QHBoxLayout()
        self.shbox5 = QHBoxLayout()

        self.svbox3.addLayout(self.shbox4)
        self.svbox3.addLayout(self.shbox5)

        self.shbox4.addWidget(self.teachers_gbox)

        self._create_teachers_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox5.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.teachers_tab.setLayout(self.svbox3)

    def _create_teachers_table(self):
        self.teachers_table = QTableWidget()
        self.teachers_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teachers_table.setColumnCount(5)
        self.teachers_table.setHorizontalHeaderLabels(
            ["Id", "Full_name", "subjects", "", ""])

        self._update_teachers_table()

        self.mvbox1 = QVBoxLayout()
        self.mvbox1.addWidget(self.teachers_table)
        self.teachers_gbox.setLayout(self.mvbox1)

    def _update_teachers_table(self):
        self.teachers_table.setRowCount(0)
        self.cursor.execute("SELECT * FROM teacher")
        records1 = list(self.cursor.fetchall())

        self.teachers_table.setRowCount(len(records1) + 1)

        for i, r in enumerate(records1):
            r = list(r)
            joinButton1 = QPushButton("Join")
            deleteButton1 = QPushButton("Delete")

            self.teachers_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.teachers_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.teachers_table.setItem(i, 2, QTableWidgetItem(str(r[2])))

            self.teachers_table.setCellWidget(i, 3, joinButton1)
            self.teachers_table.setCellWidget(i, 4, deleteButton1)

            joinButton1.clicked.connect(lambda ch, num=i: self._change_day_from_table1(num))

            deleteButton1.clicked.connect(lambda ch, num=i: self._delete_day_from_table1(num))
        self.insertbutton1 = QPushButton("Insert")
        self.teachers_table.setCellWidget(len(records1), 4, self.insertbutton1)
        self.teachers_table.resizeRowsToContents()

    def _change_day_from_table1(self, rowNum1):
        row1 = list()
        for column1 in range(self.teachers_table.columnCount()):
            try:
                row1.append(self.teachers_table.item(rowNum1, column1).text())
            except:
                row1.append(None)
            try:
                self.cursor.execute(
                    "UPDATE teacher Set full_name =%s, subject=%s where id = %s",
                    (row1[1], row1[2], row1[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Something wrong!")

    def _delete_day_from_table1(self, rowNum1):
        row1 = list()
        for column1 in range(self.teachers_table.columnCount()):
            try:
                row1.append(self.teachers_table.item(rowNum1, column1).text())
            except:
                row1.append(None)
            try:
                self.cursor.execute("Delete from teacher where id=%s",
                                    (row1[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Something wrong!")



# Создание таблицы с предметами.
    def _create_subjects_tab(self):

        self.subjects_tab = QWidget()
        self.tabs.addTab(self.subjects_tab, "Subjects")

        self.subjects_gbox = QGroupBox("Subjects")

        self.svbox6 = QVBoxLayout()
        self.shbox7 = QHBoxLayout()
        self.shbox8 = QHBoxLayout()

        self.svbox6.addLayout(self.shbox7)
        self.svbox6.addLayout(self.shbox8)

        self.shbox7.addWidget(self.subjects_gbox)

        self._create_subjects_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox8.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.subjects_tab.setLayout(self.svbox6)

    def _create_subjects_table(self):
        self.subjects_table = QTableWidget()
        self.subjects_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subjects_table.setColumnCount(3)
        self.subjects_table.setHorizontalHeaderLabels(
            ["name", "", ""])

        self._update_subjects_table()

        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.subjects_table)
        self.subjects_gbox.setLayout(self.mvbox2)

    def _update_subjects_table(self):
        self.subjects_table.setRowCount(0)
        self.cursor.execute("SELECT * FROM subject")
        records1 = list(self.cursor.fetchall())

        self.subjects_table.setRowCount(len(records1) + 1)

        for i, r in enumerate(records1):
            r = list(r)
            joinButton1 = QPushButton("Join")
            deleteButton1 = QPushButton("Delete")

            self.subjects_table.setItem(i, 0, QTableWidgetItem(str(r[0])))

            self.subjects_table.setCellWidget(i, 1, joinButton1)
            self.subjects_table.setCellWidget(i, 2, deleteButton1)

            joinButton1.clicked.connect(lambda ch, num=i: self._change_day_from_table2(num))

            deleteButton1.clicked.connect(lambda ch, num=i: self._delete_day_from_table2(num))
        self.insertbutton1 = QPushButton("Insert")
        self.subjects_table.setCellWidget(len(records1), 2, self.insertbutton1)
        self.subjects_table.resizeRowsToContents()

    def _change_day_from_table2(self, rowNum1):
        row1 = list()
        for column1 in range(self.subjects_table.columnCount()):
            try:
                row1.append(self.subjects_table.item(rowNum1, column1).text())
            except:
                row1.append(None)
            try:
                self.cursor.execute(
                    "UPDATE subject Set name = %s",
                    (row1[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Something wrong!")

    def _delete_day_from_table2(self, rowNum1):
        row1 = list()
        for column1 in range(self.subjects_table.columnCount()):
            try:
                row1.append(self.subjects_table.item(rowNum1, column1).text())
            except:
                row1.append(None)
            try:
                self.cursor.execute("Delete from subject where name=%s",
                                    (row1[0],))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Something wrong!")






    def _update_shedule(self):
        self._update_timetable_table()
        self._update_teachers_table()
        self._update_subjects_table()






if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())