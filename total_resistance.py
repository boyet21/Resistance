from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, \
    QLineEdit, QPushButton, QComboBox
import sys

class TotalResistanceCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Total Resistance Calculator")
        grid = QGridLayout()

        #Add Widgets
        r1label = QLabel("R1")
        self.r1_input = QLineEdit()

        r2label = QLabel("R2")
        self.r2_input =QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Series","Parallel"])

        calculate_button = QPushButton("Calculate")


        #Add widgets to grid
        grid.addWidget(r1label,0,0)
        grid.addWidget(self.r1_input,0,1)
        grid.addWidget(r2label,1,0)
        grid.addWidget(self.r2_input,1,1)
        grid.addWidget(self.unit_combo,1,2)
        grid.addWidget(calculate_button,3,0)

        self.setLayout(grid)

app = QApplication(sys.argv)
calculator = TotalResistanceCalculator()
calculator.show()
sys.exit(app.exec())