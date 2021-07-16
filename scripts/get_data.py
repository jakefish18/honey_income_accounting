import sys
from PyQt5.QtWidgets import *


class HoneyIncomeAccounting(QDialog):
    """Класс программы cобирающей данные и выовдящий результаты в output.txt."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.resize(600, 600)
        # Поля для ввода нужных данных.
        self.led_customer_name = QLineEdit("Имя покупателя", self)
        self.led_quantity_of_jars = QLineEdit("Количество банок меда:", self)
        self.led_price_of_jar = QLineEdit("Цена за банку меда:", self)

        #Расстановка полей.
        self.led_customer_name.move(50, 40)
        self.led_quantity_of_jars.move(50, 70)
        self.led_price_of_jar.move(50, 100)

        #Кнопка заноса данных.
        self.btn_push_data = QPushButton("Занести данные", self)
        self.btn_push_data.move(50, 130)

        #Привязка к кнопке функции заноса данных.
        self.btn_push_data.clicked.connect(self.get_customer_info)

        self.PATH_TO_OUTPUT = "D:\\GitHub projects\\honey_income_accounting\\txt_files\\output.txt"

    def get_customer_info(self):
        """Получение информации о покупке меда."""
        #Проверка на валидабельность пользователем.
        quest_correctness = QMessageBox.question(self, 
                            "Проверка корректности", "Проверьте на корректность введенные даннные. Если все правильно нажмите 'Yes'.")
        if quest_correctness == QMessageBox.No:
            return 0

        #Получение информации с полей.
        customer_name = self.led_customer_name.text()
        quantity_of_jars = int(self.led_quantity_of_jars.text())
        price_for_jar = int(self.led_price_of_jar.text())

        with open(self.PATH_TO_OUTPUT, 'r', encoding="UTF-8") as file:
            # Вытаскивание данных.
            file_data = file.readlines()

        with open(self.PATH_TO_OUTPUT, 'w', encoding="UTF-8") as file:
            # Запись данных обратно, с добавлением нового покупателя и обновленной цены.
            old_quantity, old_price = map(int, file_data[-1].split()[3::4])
            new_quantity = old_quantity + quantity_of_jars
            new_price = old_price + (price_for_jar * quantity_of_jars)
            new_result = f"\nКоличество проданных банок: {new_quantity} Количество заработанных денег: {new_price} руб."

            # Удаление устаревшой информации о цене и количестве купленных банок.
            del(file_data[-1])

            # Добавление в файл новой информации
            customer_info = f"{customer_name}    {quantity_of_jars}    {price_for_jar}"
            file_data.append(customer_info)
            file_data.append(new_result)

            for data in file_data:
                file.write(data)
        
        #Показ пользователю, что все хорошо.
        QMessageBox.information(self, "Успешно!", "Данные занесены!")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = HoneyIncomeAccounting()
    program.show()
    sys.exit(app.exec_())
