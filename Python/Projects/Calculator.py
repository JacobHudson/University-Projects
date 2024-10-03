import sys
import ast
import operator
import math
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QMessageBox
)
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.memory = 0  # Initialize memory to 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scientific Calculator')
        self.setFixedSize(500, 600)  # Adjusted window size for more buttons

        # Create the main vertical layout
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # Display
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 24px;")
        vbox.addWidget(self.display)

        # Buttons layout
        grid = QGridLayout()

        # Define the buttons and their positions
        buttons = [
            # Row, Column, Button Text
            ('MC', 0, 0), ('MR', 0, 1), ('M+', 0, 2), ('M-', 0, 3), ('CE', 0, 4),
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('√', 1, 3), ('!', 1, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('(', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), (')', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('^', 4, 4),
            ('0', 5, 0), ('.', 5, 1), ('π', 5, 2), ('+', 5, 3), ('ln', 5, 4),
            ('log', 6, 0), ('exp', 6, 1), ('Ans', 6, 2), ('Clear', 6, 3), ('=', 6, 4)
        ]

        # Create and add buttons to the grid
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(80, 60)
            button.setStyleSheet("""
                QPushButton {
                    font-size: 16px;
                    background-color: #f0f0f0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #dcdcdc;
                }
            """)
            button.clicked.connect(self.on_click)
            grid.addWidget(button, row, col)

        vbox.addLayout(grid)

    def on_click(self):
        sender = self.sender()
        button_text = sender.text()
        current_expression = self.display.text()

        if button_text == 'Clear':
            self.display.clear()
            return
        elif button_text == '=':
            self.calculate_result()
            return
        elif button_text in {'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'ln', 'exp', '√'}:
            # Append function with opening parenthesis
            if button_text == '√':
                self.display.setText(current_expression + 'sqrt(')
            elif button_text == 'log':
                self.display.setText(current_expression + 'log10(')
            elif button_text == 'ln':
                self.display.setText(current_expression + 'log(')
            else:
                self.display.setText(current_expression + button_text + '(')
            return
        elif button_text == 'π':
            self.display.setText(current_expression + 'pi')
            return
        elif button_text == 'Ans':
            self.display.setText(current_expression + str(self.memory))
            return
        elif button_text in {'MC', 'MR', 'M+', 'M-'}:
            self.handle_memory(button_text)
            return
        elif button_text == '!':
            self.display.setText(current_expression + 'factorial(')
            return
        elif button_text == '^':
            self.display.setText(current_expression + '**')
            return
        elif button_text == 'CE':
            # Clear Entry: Remove the last entry
            self.display.setText(current_expression[:-1])
            return

        # Prevent multiple operators in a row
        if button_text in '+-*/**':
            if current_expression and current_expression[-1] in '+-*/':
                # Replace the last operator with the new one
                current_expression = current_expression[:-1]
            self.display.setText(current_expression + button_text)
        else:
            self.display.setText(current_expression + button_text)

    def calculate_result(self):
        expression = self.display.text()
        try:
            result = self.safe_eval(expression)
            self.memory = result  # Store the result in memory
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText('Error')
            QMessageBox.warning(self, "Error", "Invalid Expression")

    def handle_memory(self, action):
        if action == 'MC':
            self.memory = 0
        elif action == 'MR':
            self.display.setText(self.display.text() + str(self.memory))
        elif action == 'M+':
            try:
                self.memory += float(self.safe_eval(self.display.text()))
            except:
                QMessageBox.warning(self, "Error", "Invalid Expression for M+")
        elif action == 'M-':
            try:
                self.memory -= float(self.safe_eval(self.display.text()))
            except:
                QMessageBox.warning(self, "Error", "Invalid Expression for M-")

    def safe_eval(self, expr):
        """
        Safely evaluate a mathematical expression with support for scientific functions.
        """
        # Define supported operators and functions
        allowed_names = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'log10': math.log10,
            'log': math.log,
            'sqrt': math.sqrt,
            'exp': math.exp,
            'pi': math.pi,
            'e': math.e,
            'factorial': math.factorial,
            '__builtins__': {}
        }

        # Replace unicode square root symbol with 'sqrt'
        expr = expr.replace('√', 'sqrt')

        try:
            node = ast.parse(expr, mode='eval')

            def _eval(node):
                if isinstance(node, ast.Expression):
                    return _eval(node.body)
                elif isinstance(node, ast.Num):  # <number>
                    return node.n
                elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
                    left = _eval(node.left)
                    right = _eval(node.right)
                    return self.operators(type(node.op))(left, right)
                elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
                    operand = _eval(node.operand)
                    return self.operators(type(node.op))(operand)
                elif isinstance(node, ast.Call):  # Function calls
                    func = node.func.id
                    if func in allowed_names:
                        args = [_eval(arg) for arg in node.args]
                        return allowed_names[func](*args)
                    else:
                        raise ValueError(f"Unsupported function: {func}")
                elif isinstance(node, ast.Name):
                    if node.id in allowed_names:
                        return allowed_names[node.id]
                    else:
                        raise ValueError(f"Unsupported name: {node.id}")
                else:
                    raise TypeError(node)

            return _eval(node)
        except Exception as e:
            raise e

    def operators(self, op_type):
        """
        Map operator types to actual operations.
        """
        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.USub: operator.neg,
            ast.UAdd: operator.pos,
        }
        if op_type in operators:
            return operators[op_type]
        else:
            raise TypeError(f"Unsupported operator: {op_type}")

    def keyPressEvent(self, event):
        key = event.key()
        key_map = {
            Qt.Key_0: '0',
            Qt.Key_1: '1',
            Qt.Key_2: '2',
            Qt.Key_3: '3',
            Qt.Key_4: '4',
            Qt.Key_5: '5',
            Qt.Key_6: '6',
            Qt.Key_7: '7',
            Qt.Key_8: '8',
            Qt.Key_9: '9',
            Qt.Key_Plus: '+',
            Qt.Key_Minus: '-',
            Qt.Key_Asterisk: '*',
            Qt.Key_Slash: '/',
            Qt.Key_ParenLeft: '(',
            Qt.Key_ParenRight: ')',
            Qt.Key_AsciiCircum: '^',
            Qt.Key_Period: '.',
            Qt.Key_Equal: '=',
            Qt.Key_Return: '=',
            Qt.Key_Enter: '=',
            Qt.Key_Backspace: 'CE',
            Qt.Key_Delete: 'Clear',
            Qt.Key_Escape: 'Clear',
        }

        if key in key_map:
            value = key_map[key]
            if value == 'Clear':
                self.display.clear()
            elif value == '=':
                self.calculate_result()
            elif value == 'CE':
                # Clear Entry: Remove the last character
                current_expression = self.display.text()
                self.display.setText(current_expression[:-1])
            else:
                # Find the button with the corresponding text and click it
                for button in self.findChildren(QPushButton):
                    if button.text() == value:
                        button.click()
                        break
        else:
            super().keyPressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
