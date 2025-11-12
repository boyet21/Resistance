from PyQt6.QtCore import QLine
from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, \
    QLineEdit, QPushButton, QComboBox
from PyQt6.QtGui import QIcon
import sys



class TotalResistanceCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resistance Calculator")
        self.setMinimumSize(250,150)
        self.setWindowIcon(QIcon('icons/Lion.png'))
        self.setStyleSheet('background-color: orangered;')

        grid = QGridLayout()

        #Add widgets
        r1label = QLabel("R1 (in ohms)")
        font1 = r1label.font()
        font1.setPointSize(12)
        r1label.setFont(font1)
        self.r1_input = QLineEdit()
        self.r1_input.setStyleSheet("QLineEdit{background-color: #87CEEB;"
                                    "color:maroon;font-size:16px;}")

        r2label = QLabel("R2 (in ohms)")
        font2 = r2label.font()
        font2.setPointSize(12)
        r2label.setFont(font2)
        self.r2_input =QLineEdit()
        self.r2_input.setStyleSheet("QLineEdit{background-color:#87CEEB;"
                                    "color:maroon;font-size:16px;}")

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Series","Parallel"])

        calculate_button = QPushButton("Calculate")
        calculate_button.setStyleSheet("QPushButton{background-color:green;}")
        calculate_button.clicked.connect(self.calculate)

        self.result_label = QLabel()

        #Add widgets to grid
        grid.addWidget(r1label,0,0)
        grid.addWidget(self.r1_input,0,1)
        grid.addWidget(r2label,1,0)
        grid.addWidget(self.r2_input,1,1)
        grid.addWidget(self.unit_combo,2,1)
        grid.addWidget(calculate_button,2,0)
        grid.addWidget(self.result_label,3,0,1,2)

        self.setLayout(grid)

    def calculate(self):
        try:
            # Get the resistances from the input boxes
            r1 = float(self.r1_input.text())
            r2 = float(self.r2_input.text())
        except ValueError:
            self.result_label.setText("Please enter valid numeric values for R1 and R2.")
            return

        # Check for division by zero in parallel resistance
        if r1 + r2 == 0:
            self.result_label.setText("R1 and R2 cannot both be zero for parallel resistance.")

        # Calculate the total resistances in series
        total_resistance1 = r1 + r2

        # Calculate the total resistance in parallel
        total_resistance2 = (r1*r2)/(r1+r2)

        # Check what the user chose in the combo
        if self.unit_combo.currentText() == 'Series':
            total_resistance = round(total_resistance1, 2)
            unit = "ohms"

        elif self.unit_combo.currentText() == 'Parallel':
            total_resistance = round(total_resistance2, 2)
            unit = "ohms"

        self.result_label.setText(f"The Total Resistance is: {total_resistance} {unit}")


app = QApplication(sys.argv)
calculator = TotalResistanceCalculator()
calculator.show()
sys.exit(app.exec())