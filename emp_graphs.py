from PyQt5.Qt import Qt
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QHBoxLayout


class EmpBarChart:

    def __init__(self, emp_data):
        self.dataset = QBarSet("")
        self.x_data = []
        self.series = QBarSeries()
        self.chart = QChart()
        self.axisX = QBarCategoryAxis()
        self.axisY = QValueAxis()
        self.emp_data = emp_data

        self.create_axis()

    def build_chart(self):
        pass

    def create_axis(self):

        self.series.clear()
        self.dataset.remove(self.dataset.count())
        self.x_data.clear()

        y_range = 0
        for item in self.emp_data:
            if item[1] > y_range:
                y_range = item[1]
            self.x_data.append(f'{item[0][5:7]} - {item[0][:4]}')
            self.dataset.append(item[1])

        self.series.append(self.dataset)