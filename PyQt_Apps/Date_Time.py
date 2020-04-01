from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
now = QDate.currentDate()
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()
print(datetime.toString())

time = QTime.currentTime()

print(time.toString(Qt.DefaultLocaleLongDate))
print("\n")
print("Local datetime: ", datetime.toString(Qt.DefaultLocaleLongDate))
print("Universal Time : ", datetime.toUTC().toString(Qt.DefaultLocaleLongDate))

print("The offset from UTC is : {} seconds".format(datetime.offsetFromUtc()))
print("\n")
print("Days in month: {}".format(now.daysInMonth()))
print("Days in year: {}".format(now.daysInYear()))
