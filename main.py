import psycopg2
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QAbstractScrollArea, QVBoxLayout, QHBoxLayout, \
    QTableWidget, QGroupBox, QTableWidgetItem, QPushButton, QMessageBox, QSizePolicy


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Timetable")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_timetable_tab()
        self._create_timetable_tab_down()
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
        self.tabs.addTab(self.timetable_tab, "Timetable_Up")

        # self.timetable_gbox = QGroupBox("Timetable")
        self.timetable_monday_gbox = QGroupBox("Понедельник")
        self.timetable_tuesday_gbox = QGroupBox("Вторник")
        self.timetable_wednesday_gbox = QGroupBox("Среда")
        self.timetable_thursday_gbox = QGroupBox("Четверг")
        self.timetable_friday_gbox = QGroupBox("Пятница")

        self.timetable_add_gbox = QGroupBox("Добавление строки")



        #Понедельник
        self.svbox = QVBoxLayout()


        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        # Понедельник
        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        #Вторник
        self.shbox_tu=QHBoxLayout()
        self.shbox_tu1=QHBoxLayout()

        #Вторник
        self.svbox.addLayout(self.shbox_tu)
        self.svbox.addLayout(self.shbox_tu1)

        # Среда
        self.shbox_wd = QHBoxLayout()
        self.shbox_wd1 = QHBoxLayout()

        # Среда
        self.svbox.addLayout(self.shbox_wd)
        self.svbox.addLayout(self.shbox_wd1)

        # Четверг
        self.shbox_th = QHBoxLayout()
        self.shbox_th1 = QHBoxLayout()

        # Четверг
        self.svbox.addLayout(self.shbox_th)
        self.svbox.addLayout(self.shbox_th1)

        # Пятница
        self.shbox_fr = QHBoxLayout()
        self.shbox_fr1 = QHBoxLayout()

        # Пятница
        self.svbox.addLayout(self.shbox_fr)
        self.svbox.addLayout(self.shbox_fr1)

        # Добавление строки
        self.shbox_add = QHBoxLayout()
        self.shbox_add1 = QHBoxLayout()

        # Добавление строки
        self.svbox.addLayout(self.shbox_add)
        self.svbox.addLayout(self.shbox_add1)

        # self.shbox1.addWidget(self.timetable_gbox)
        self.shbox1.addWidget(self.timetable_monday_gbox)
        self.shbox_tu.addWidget(self.timetable_tuesday_gbox)
        self.shbox_wd.addWidget(self.timetable_wednesday_gbox)
        self.shbox_th.addWidget(self.timetable_thursday_gbox)
        self.shbox_fr.addWidget(self.timetable_friday_gbox)
        self.shbox_add.addWidget(self.timetable_add_gbox)

        # self._create_timetable_table() #для всей недели
        self._create_timetable_Monday_table()
        self._create_timetable_Tuesday_table()
        self._create_timetable_Wednesday_table()
        self._create_timetable_Thursday_table()
        self._create_timetable_Friday_table()
        self._create_timetable_add_table()


        self.update_shedule_button = QPushButton("Update")
        self.svbox.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.timetable_tab.setLayout(self.svbox)


    def _create_timetable_Monday_table(self):  # Понедельник
        self.timetable_table_m = QTableWidget()
        # self.timetable_table_m.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_m.setMaximumHeight(80)
        self.timetable_table_m.setMaximumHeight(80)

        self.timetable_table_m.setColumnCount(8)
        self.timetable_table_m.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_Monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.timetable_table_m)
        self.timetable_monday_gbox.setLayout(self.mvbox)

    def _create_timetable_Tuesday_table(self): #Вторник
        self.timetable_table_tu = QTableWidget()
        # self.timetable_table_tu.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_tu.setMaximumHeight(100)
        self.timetable_table_tu.setMaximumHeight(100)

        self.timetable_table_tu.setColumnCount(8)
        self.timetable_table_tu.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_Tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.timetable_table_tu)
        self.timetable_tuesday_gbox.setLayout(self.mvbox)

    def _create_timetable_Wednesday_table(self):  # Среда
        self.timetable_table_wd = QTableWidget()
        # self.timetable_table_wd.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_wd.setMaximumHeight(100)
        self.timetable_table_wd.setMaximumHeight(100)

        self.timetable_table_wd.setColumnCount(8)
        self.timetable_table_wd.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_Wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.timetable_table_wd)
        self.timetable_wednesday_gbox.setLayout(self.mvbox)

    def _create_timetable_Thursday_table(self):
        self.timetable_table_th = QTableWidget()
        # self.timetable_table_th.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_th.setMaximumHeight(80)
        self.timetable_table_th.setMaximumHeight(80)

        self.timetable_table_th.setColumnCount(8)
        self.timetable_table_th.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_Thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.timetable_table_th)
        self.timetable_thursday_gbox.setLayout(self.mvbox)

    def _create_timetable_Friday_table(self):
        self.timetable_table_fr = QTableWidget()
        # self.timetable_table_fr.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_fr.setMaximumHeight(80)
        self.timetable_table_fr.setMaximumHeight(80)

        self.timetable_table_fr.setColumnCount(8)
        self.timetable_table_fr.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_Friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.timetable_table_fr)
        self.timetable_friday_gbox.setLayout(self.mvbox)

    def _create_timetable_add_table(self):
        self.timetable_table_add = QTableWidget()
        # self.timetable_table_fr.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_add.setMaximumHeight(55)
        self.timetable_table_add.setMaximumHeight(55)

        self.timetable_table_add.setColumnCount(8)
        self.timetable_table_add.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_add_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.timetable_table_add)
        self.timetable_add_gbox.setLayout(self.mvbox)


   #____________________________________UPDATE _ TIMETABLE____________________________________
    def _update_timetable_Monday_table(self):  # Понедельник
        self.timetable_table_m.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day = 'Понедельник' and week_numb = 'Вверхняя' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_m.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_m.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_m.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_m.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_m.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_m.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_m.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_m.setCellWidget(i, 6, joinButton)
            self.timetable_table_m.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_monday(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_monday(num))
        # insertButton = QPushButton("Insert")
        # self.timetable_table_m.setCellWidget(len(records), 6, insertButton)
        # insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        # self.timetable_table_m.resizeRowsToContents()

    def _update_timetable_Tuesday_table(self):
        self.timetable_table_tu.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day = 'Вторник' and week_numb = 'Вверхняя' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_tu.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_tu.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_tu.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_tu.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_tu.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_tu.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_tu.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_tu.setCellWidget(i, 6, joinButton)
            self.timetable_table_tu.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_tuesday(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_tuesday(num))
        # insertButton = QPushButton("Insert")
        # self.timetable_table_tu.setCellWidget(len(records), 6, insertButton)
        # insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        # self.timetable_table_tu.resizeRowsToContents()

    def _update_timetable_Wednesday_table(self):  # Среда
        self.timetable_table_wd.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day = 'Среда' and week_numb = 'Вверхняя' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_wd.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_wd.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_wd.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_wd.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_wd.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_wd.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_wd.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_wd.setCellWidget(i, 6, joinButton)
            self.timetable_table_wd.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_wednesday(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_wednesday(num))
        # insertButton = QPushButton("Insert")
        # self.timetable_table_wd.setCellWidget(len(records), 6, insertButton)
        # insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        # self.timetable_table_wd.resizeRowsToContents()

    def _update_timetable_Thursday_table(self):
        self.timetable_table_th.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day = 'Четверг' and week_numb = 'Вверхняя' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_th.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_th.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_th.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_th.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_th.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_th.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_th.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_th.setCellWidget(i, 6, joinButton)
            self.timetable_table_th.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_thursday(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_thursday(num))
        # insertButton = QPushButton("Insert")
        # self.timetable_table_th.setCellWidget(len(records), 6, insertButton)
        # insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        # self.timetable_table_th.resizeRowsToContents()

    def _update_timetable_Friday_table(self):
        self.timetable_table_fr.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day = 'Пятница' and week_numb = 'Вверхняя' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_fr.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_fr.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_fr.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_fr.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_fr.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_fr.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_fr.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_fr.setCellWidget(i, 6, joinButton)
            self.timetable_table_fr.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_friday(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_friday(num))
        # insertButton = QPushButton("Insert")
        # self.timetable_table_fr.setCellWidget(len(records), 6, insertButton)
        # insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        # self.timetable_table_fr.resizeRowsToContents()

    def _update_timetable_add_table(self):
        self.timetable_table_add.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day IS NULL OR day = '' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_add.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_add.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_add.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_add.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_add.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_add.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_add.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_add.setCellWidget(i, 6, joinButton)
            self.timetable_table_add.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_add(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_add(num))
        insertButton = QPushButton("Insert")
        self.timetable_table_add.setCellWidget(len(records), 7, insertButton)
        insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        self.timetable_table_add.resizeRowsToContents()






# ________________________________Insert Timetable_UP___________________________________

    def insert_timetable_day(self):
        self.cursor.execute("Insert INTO timetable DEFAULT VALUES")

        self.conn.commit()
        self._update_shedule()

#________________________________CHANGE DAY TIMETABLE UP__________________________________
    def _change_day_from_monday(self, rowNum):
        row = list()
        for column in range(self.timetable_table_m.columnCount()):
            try:
                row.append(self.timetable_table_m.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")

    def _change_day_from_tuesday(self, rowNum):
        row = list()
        for column in range(self.timetable_table_tu.columnCount()):
            try:
                row.append(self.timetable_table_tu.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")

    def _change_day_from_wednesday(self, rowNum):
        row = list()
        for column in range(self.timetable_table_wd.columnCount()):
            try:
                row.append(self.timetable_table_wd.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")

    def _change_day_from_thursday(self, rowNum):
        row = list()
        for column in range(self.timetable_table_th.columnCount()):
            try:
                row.append(self.timetable_table_th.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")

    def _change_day_from_friday(self, rowNum):
        row = list()
        for column in range(self.timetable_table_fr.columnCount()):
            try:
                row.append(self.timetable_table_fr.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")

    def _change_day_from_add(self, rowNum):
        row = list()
        for column in range(self.timetable_table_add.columnCount()):
            try:
                row.append(self.timetable_table_add.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")
        self._update_timetable_add_table()



#__________________________________DELETE DAY FROM TIMETABLE UP_____________________________________
    def _delete_day_from_monday(self, rowNum):
        row = list()
        for column in range(self.timetable_table_m.columnCount()):
            try:
                row.append(self.timetable_table_m.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")


    def _delete_day_from_tuesday(self, rowNum):
        row = list()
        for column in range(self.timetable_table_tu.columnCount()):
            try:
                row.append(self.timetable_table_tu.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")


    def _delete_day_from_wednesday(self, rowNum):
        row = list()
        for column in range(self.timetable_table_wd.columnCount()):
            try:
                row.append(self.timetable_table_wd.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")

    def _delete_day_from_thursday(self, rowNum):
        row = list()
        for column in range(self.timetable_table_th.columnCount()):
            try:
                row.append(self.timetable_table_th.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")

    def _delete_day_from_friday(self, rowNum):
        row = list()
        for column in range(self.timetable_table_fr.columnCount()):
            try:
                row.append(self.timetable_table_fr.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")

    def _delete_day_from_add(self, rowNum):
        row = list()
        for column in range(self.timetable_table_add.columnCount()):
            try:
                row.append(self.timetable_table_add.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")
        self._update_timetable_add_table()



#     # _________________________________________НИЖНЯЯ НЕДЕЛЯ____________________________________________
    def _create_timetable_tab_down(self):
        self.timetable_tab_down = QWidget()
        self.tabs.addTab(self.timetable_tab_down, "Timetable_Down")

        # self.timetable_gbox = QGroupBox("Timetable")
        self.timetable_monday_gbox1 = QGroupBox("Понедельник")
        self.timetable_tuesday_gbox1 = QGroupBox("Вторник")
        self.timetable_wednesday_gbox1 = QGroupBox("Среда")
        self.timetable_thursday_gbox1 = QGroupBox("Четверг")
        self.timetable_friday_gbox1 = QGroupBox("Пятница")
        self.timetable_add_gbox1 = QGroupBox("Добавление строки")



        #Понедельник
        self.svbox10 = QVBoxLayout()


        self.shbox_2 = QHBoxLayout()
        self.shbox_3 = QHBoxLayout()

        # Понедельник
        self.svbox10.addLayout(self.shbox_2)
        self.svbox10.addLayout(self.shbox_3)

        #Вторник
        self.shbox__tu=QHBoxLayout()
        self.shbox__tu1=QHBoxLayout()

        #Вторник
        self.svbox10.addLayout(self.shbox__tu)
        self.svbox10.addLayout(self.shbox__tu1)

        # Среда
        self.shbox__wd = QHBoxLayout()
        self.shbox__wd1 = QHBoxLayout()

        # Среда
        self.svbox10.addLayout(self.shbox__wd)
        self.svbox10.addLayout(self.shbox__wd1)

        # Четверг
        self.shbox__th = QHBoxLayout()
        self.shbox__th1 = QHBoxLayout()

        # Четверг
        self.svbox10.addLayout(self.shbox__th)
        self.svbox10.addLayout(self.shbox__th1)

        # Пятница
        self.shbox__fr = QHBoxLayout()
        self.shbox__fr1 = QHBoxLayout()

        # Пятница
        self.svbox10.addLayout(self.shbox__fr)
        self.svbox10.addLayout(self.shbox__fr1)

        # Добавление строки
        self.shbox__add = QHBoxLayout()
        self.shbox__add1 = QHBoxLayout()

        # Добавление строки
        self.svbox10.addLayout(self.shbox__add)
        self.svbox10.addLayout(self.shbox__add1)

        # self.shbox1.addWidget(self.timetable_gbox)
        self.shbox_2.addWidget(self.timetable_monday_gbox1)
        self.shbox__tu.addWidget(self.timetable_tuesday_gbox1)
        self.shbox__wd.addWidget(self.timetable_wednesday_gbox1)
        self.shbox__th.addWidget(self.timetable_thursday_gbox1)
        self.shbox__fr.addWidget(self.timetable_friday_gbox1)
        self.shbox__add.addWidget(self.timetable_add_gbox1)

        # self._create_timetable_table() #для всей недели
        self._create_timetable_Monday_table1()
        self._create_timetable_Tuesday_table1()
        self._create_timetable_Wednesday_table1()
        self._create_timetable_Thursday_table1()
        self._create_timetable_Friday_table1()
        self._create_timetable_add_table1()


        self.update_shedule_button1 = QPushButton("Update")
        self.svbox10.addWidget(self.update_shedule_button1)
        self.update_shedule_button1.clicked.connect(self._update_shedule)

        self.timetable_tab_down.setLayout(self.svbox10)


#________________________CREATE TABLE_DOWN_____________________________________________________________
    def _create_timetable_Monday_table1(self):  # Понедельник
        self.timetable_table_m1 = QTableWidget()
        # self.timetable_table_m1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_m1.setMaximumHeight(75)
        self.timetable_table_m1.setMinimumHeight(75)

        self.timetable_table_m1.setColumnCount(8)
        self.timetable_table_m1.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_Monday_table1()

        self.mvbox_1 = QVBoxLayout()
        self.mvbox_1.addWidget(self.timetable_table_m1)
        self.timetable_monday_gbox1.setLayout(self.mvbox_1)

    def _create_timetable_Tuesday_table1(self): #Вторник
        self.timetable_table_tu1 = QTableWidget()
        # self.timetable_table_tu1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_tu1.setMaximumHeight(75)
        self.timetable_table_tu1.setMinimumHeight(75)

        self.timetable_table_tu1.setColumnCount(8)
        self.timetable_table_tu1.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_Tuesday_table1()

        self.mvbox_1 = QVBoxLayout()
        self.mvbox_1.addWidget(self.timetable_table_tu1)
        self.timetable_tuesday_gbox1.setLayout(self.mvbox_1)

    def _create_timetable_Wednesday_table1(self):  # Среда
        self.timetable_table_wd1 = QTableWidget()
        # self.timetable_table_wd1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_wd1.setMaximumHeight(75)
        self.timetable_table_wd1.setMinimumHeight(75)

        self.timetable_table_wd1.setColumnCount(8)
        self.timetable_table_wd1.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_Wednesday_table1()

        self.mvbox_1 = QVBoxLayout()
        self.mvbox_1.addWidget(self.timetable_table_wd1)
        self.timetable_wednesday_gbox1.setLayout(self.mvbox_1)

    def _create_timetable_Thursday_table1(self):
        self.timetable_table_th1 = QTableWidget()
        # self.timetable_table_th1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_th1.setMaximumHeight(75)
        self.timetable_table_th1.setMinimumHeight(75)

        self.timetable_table_th1.setColumnCount(8)
        self.timetable_table_th1.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_Thursday_table1()

        self.mvbox_1 = QVBoxLayout()
        self.mvbox_1.addWidget(self.timetable_table_th1)
        self.timetable_thursday_gbox1.setLayout(self.mvbox_1)

    def _create_timetable_Friday_table1(self):
        self.timetable_table_fr1 = QTableWidget()
        # self.timetable_table_fr1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_fr1.setMaximumHeight(75)
        self.timetable_table_fr1.setMinimumHeight(75)

        self.timetable_table_fr1.setColumnCount(8)
        self.timetable_table_fr1.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_Friday_table1()

        self.mvbox_1 = QVBoxLayout()
        self.mvbox_1.addWidget(self.timetable_table_fr1)
        self.timetable_friday_gbox1.setLayout(self.mvbox_1)

    def _create_timetable_add_table1(self):
        self.timetable_table_add1 = QTableWidget()
        # self.timetable_table_fr.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_table_add1.setMaximumHeight(55)
        self.timetable_table_add1.setMaximumHeight(55)

        self.timetable_table_add1.setColumnCount(8)
        self.timetable_table_add1.setHorizontalHeaderLabels(
            ["Id", "Day", "Subject", "Room_numb", "Start_time", "Week_numb", "", ""])

        self._update_timetable_add_table1()

        self.mvbox_1 = QVBoxLayout()
        self.mvbox_1.addWidget(self.timetable_table_add1)
        self.timetable_add_gbox1.setLayout(self.mvbox_1)



    #_________________________UPDATE ____ TIMETABLE_DOWN__________________________________________

    def _update_timetable_Monday_table1(self):  # Понедельник
        self.timetable_table_m1.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day = 'Понедельник' and week_numb = 'Нижняя' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_m1.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_m1.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_m1.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_m1.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_m1.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_m1.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_m1.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_m1.setCellWidget(i, 6, joinButton)
            self.timetable_table_m1.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_monday1(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_monday1(num))
        # insertButton = QPushButton("Insert")
        # self.timetable_table_m.setCellWidget(len(records), 6, insertButton)
        # insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        # self.timetable_table_m.resizeRowsToContents()

    def _update_timetable_Tuesday_table1(self):
        self.timetable_table_tu1.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day = 'Вторник' and week_numb = 'Нижняя' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_tu1.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_tu1.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_tu1.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_tu1.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_tu1.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_tu1.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_tu1.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_tu1.setCellWidget(i, 6, joinButton)
            self.timetable_table_tu1.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_tuesday1(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_tuesday1(num))
        # insertButton = QPushButton("Insert")
        # self.timetable_table_tu.setCellWidget(len(records), 6, insertButton)
        # insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        # self.timetable_table_tu.resizeRowsToContents()

    def _update_timetable_Wednesday_table1(self):  # Среда
        self.timetable_table_wd1.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day = 'Среда' and week_numb = 'Нижняя' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_wd1.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_wd1.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_wd1.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_wd1.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_wd1.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_wd1.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_wd1.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_wd1.setCellWidget(i, 6, joinButton)
            self.timetable_table_wd1.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_wednesday1(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_wednesday1(num))
        # insertButton = QPushButton("Insert")
        # self.timetable_table_wd.setCellWidget(len(records), 6, insertButton)
        # insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        # self.timetable_table_wd.resizeRowsToContents()

    def _update_timetable_Thursday_table1(self):
        self.timetable_table_th1.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day = 'Четверг' and week_numb = 'Нижняя' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_th1.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_th1.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_th1.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_th1.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_th1.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_th1.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_th1.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_th1.setCellWidget(i, 6, joinButton)
            self.timetable_table_th1.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_thursday1(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_thursday1(num))
        # insertButton = QPushButton("Insert")
        # self.timetable_table_th.setCellWidget(len(records), 6, insertButton)
        # insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        # self.timetable_table_th.resizeRowsToContents()

    def _update_timetable_Friday_table1(self):
        self.timetable_table_fr1.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day = 'Пятница' and week_numb = 'Нижняя' or day IS NULL OR day = '' "
                            "order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_fr1.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_fr1.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_fr1.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_fr1.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_fr1.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_fr1.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_fr1.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_fr1.setCellWidget(i, 6, joinButton)
            self.timetable_table_fr1.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_friday1(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_friday1(num))
        # insertButton = QPushButton("Insert")
        # self.timetable_table_fr1.setCellWidget(len(records), 6, insertButton)
        # insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        # self.timetable_table_fr1.resizeRowsToContents()

    def _update_timetable_add_table1(self):
        self.timetable_table_add1.setRowCount(0)
        self.cursor.execute("SELECT * FROM timetable where day IS NULL OR day = '' order by id")
        records = list(self.cursor.fetchall())

        self.timetable_table_add1.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")

            self.timetable_table_add1.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.timetable_table_add1.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.timetable_table_add1.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.timetable_table_add1.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.timetable_table_add1.setItem(i, 4, QTableWidgetItem(str(r[4])))
            self.timetable_table_add1.setItem(i, 5, QTableWidgetItem(str(r[5])))

            self.timetable_table_add1.setCellWidget(i, 6, joinButton)
            self.timetable_table_add1.setCellWidget(i, 7, deleteButton)
            # self.timetable_table.setCellWidget(len(records), 6, insertButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_add1(num))

            deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_add1(num))
        insertButton = QPushButton("Insert")
        self.timetable_table_add1.setCellWidget(len(records), 7, insertButton)
        insertButton.clicked.connect(lambda ch: self.insert_timetable_day())
        self.timetable_table_add1.resizeRowsToContents()


#_______________________________CHANGE_DAY_FROM_TIMETABLE_DOWN
    def _change_day_from_monday1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_m1.columnCount()):
            try:
                row.append(self.timetable_table_m1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")

    def _change_day_from_tuesday1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_tu1.columnCount()):
            try:
                row.append(self.timetable_table_tu1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")

    def _change_day_from_wednesday1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_wd1.columnCount()):
            try:
                row.append(self.timetable_table_wd1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")

    def _change_day_from_thursday1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_th1.columnCount()):
            try:
                row.append(self.timetable_table_th1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")

    def _change_day_from_friday1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_fr1.columnCount()):
            try:
                row.append(self.timetable_table_fr1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")

    def _change_day_from_add1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_add1.columnCount()):
            try:
                row.append(self.timetable_table_add1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute(
                "UPDATE timetable Set day=%s, subject=%s, room_numb=%s, start_time=%s, week_numb=%s where id = %s",
                (row[1], row[2], row[3], row[4], row[5], row[0],))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")
        self._update_timetable_add_table1()

        # __________________________________DELETE DAY FROM TIMETABLE UP_____________________________________
    def _delete_day_from_monday1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_m1.columnCount()):
            try:
                row.append(self.timetable_table_m1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")

    def _delete_day_from_tuesday1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_tu1.columnCount()):
            try:
                row.append(self.timetable_table_tu1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")

    def _delete_day_from_wednesday1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_wd1.columnCount()):
            try:
                row.append(self.timetable_table_wd1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")

    def _delete_day_from_thursday1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_th1.columnCount()):
            try:
                row.append(self.timetable_table_th1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")

    def _delete_day_from_friday1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_fr1.columnCount()):
            try:
                row.append(self.timetable_table_fr1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")

    def _delete_day_from_add1(self, rowNum):
        row = list()
        for column in range(self.timetable_table_add1.columnCount()):
            try:
                row.append(self.timetable_table_add1.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("Delete from timetable where id=%s",
                                (row[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong! Not Delete!")
        self._update_timetable_add_table1()




# _______________________________________ТАБЛИЦА С УЧИТЕЛЯМИ_______________________________________________________
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
        self.cursor.execute("SELECT * FROM teacher order by id")
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
        insertButton1 = QPushButton("Insert")
        self.teachers_table.setCellWidget(len(records1), 4, insertButton1)
        insertButton1.clicked.connect(lambda ch: self.insert_teacher())
        self.teachers_table.resizeRowsToContents()

    def insert_teacher(self):
        self.cursor.execute("Insert INTO teacher DEFAULT VALUES")

        self.conn.commit()
        self._update_teachers_table()

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
        # except:
        #     QMessageBox.about(self, "Error", "Something wrong!")
        except Exception:
            self.conn.rollback()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")
        self._update_teachers_table()

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
        self._update_teachers_table()

#________________________________СОЗДАНИЕ ТАБЛИЦЫ С ПРЕДМЕТАМИ_________________________________________
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

        self.subjects_table.setColumnCount(4)
        self.subjects_table.setHorizontalHeaderLabels(
            ["id", "name", "", ""])

        self._update_subjects_table()

        self.mvbox2 = QVBoxLayout()
        self.mvbox2.addWidget(self.subjects_table)
        self.subjects_gbox.setLayout(self.mvbox2)

    def _update_subjects_table(self):
        self.subjects_table.setRowCount(0)
        self.cursor.execute("SELECT * FROM subject order by id")
        records1 = list(self.cursor.fetchall())

        self.subjects_table.setRowCount(len(records1) + 1)

        for i, r in enumerate(records1):
            r = list(r)
            joinButton1 = QPushButton("Join")
            deleteButton1 = QPushButton("Delete")

            self.subjects_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.subjects_table.setItem(i, 1, QTableWidgetItem(str(r[1])))

            self.subjects_table.setCellWidget(i, 2, joinButton1)
            self.subjects_table.setCellWidget(i, 3, deleteButton1)

            joinButton1.clicked.connect(lambda ch, num=i: self._change_day_from_table2(num))

            deleteButton1.clicked.connect(lambda ch, num=i: self._delete_day_from_table2(num))
        insertButton2 = QPushButton("Insert")
        self.subjects_table.setCellWidget(len(records1), 3, insertButton2)
        insertButton2.clicked.connect(lambda ch: self.insert_subjects())
        self.subjects_table.resizeRowsToContents()

    def insert_subjects(self):
        self.cursor.execute("Insert INTO subject DEFAULT VALUES")

        self.conn.commit()
        self._update_subjects_table()

    def _change_day_from_table2(self, rowNum1):
        row1 = list()
        for column1 in range(self.subjects_table.columnCount()):
            try:
                row1.append(self.subjects_table.item(rowNum1, column1).text())
            except:
                row1.append(None)
        try:
            self.cursor.execute(
                "UPDATE subject Set name = %s where id=%s",
                (row1[1], row1[0],))
            self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Error", "Something wrong!")
        except Exception:
            self.conn.rollback()
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
            self.cursor.execute("Delete from subject where id=%s",
                                    (row1[0],))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Something wrong!")
        self._update_subjects_table()

    def _update_shedule(self):

        self._update_timetable_Monday_table()
        self._update_timetable_Thursday_table()
        self._update_timetable_Wednesday_table()
        self._update_timetable_Tuesday_table()
        self._update_timetable_Friday_table()
        self._update_timetable_add_table()

        self._update_timetable_Monday_table1()
        self._update_timetable_Thursday_table1()
        self._update_timetable_Wednesday_table1()
        self._update_timetable_Tuesday_table1()
        self._update_timetable_Friday_table1()
        self._update_timetable_add_table1()

        self._update_teachers_table()
        self._update_subjects_table()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())