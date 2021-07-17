import sys
from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import *


class HoneyIncomeAccounting(QDialog):
    """Класс программы cобирающей данные и выовдящий результаты в output.txt."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.resize(600, 600)
        # Поля для ввода нужных данных.
        self.led_customer_name = QLineEdit("Имя покупателя:", self)
        self.led_quantity_of_jars = QLineEdit("Количество банок меда:", self)
        self.led_price_of_jar = QLineEdit("Цена за банку меда:", self)

        #Расстановка полей.
        self.led_customer_name.move(50, 40)
        self.led_quantity_of_jars.move(50, 70)
        self.led_price_of_jar.move(50, 100)

        #Кнопка заноса данных.
        self.btn_push_data = QPushButton("Занести данные", self)
        self.btn_push_data.move(50, 130)
        self.btn_push_data.clicked.connect(self.get_customer_info)

        #Поля для должников.
        self.led_debtor_name = QLineEdit("Имя должника:", self)
        self.led_debtor_num_of_jars = QLineEdit("Количество банок:", self)
        self.led_debtor_price_of_jar = QLineEdit("Цена за банку меда:", self)

        #Расствновка полей для должников.
        self.led_debtor_name.move(250, 40)
        self.led_debtor_num_of_jars.move(250, 70)
        self.led_debtor_price_of_jar.move(250, 100)

        #Кнопка заноча данных для должников.
        self.btn_push_debtor_data = QPushButton("Занести должника", self)
        self.btn_push_debtor_data.move(250, 130)
        self.btn_push_debtor_data.clicked.connect(self.push_debtor_info)

        #Полe для убора должников.
        self.led_debtor_remove_name = QLineEdit("Имя должника:", self)
        self.led_debtor_remove_name.move(450, 40)

        #Кнопка убора должника.
        self.btn_debtor_remove = QPushButton("Убрать должника", self)
        self.btn_debtor_remove.move(450, 70)
        self.btn_debtor_remove.clicked.connect(self.remove_debtor)

        #Кнопка вывода общего результата.
        self.btn_watch_main_data = QPushButton("Посмотреть количество проданных банок и заработок с них.", self)
        self.btn_watch_main_data.move(50, 200)
        self.btn_watch_main_data.clicked.connect(self.get_main_data)

        self.PATH_TO_OUTPUT = "D:\\GitHub projects\\honey_income_accounting\\txt_files\\output.txt"
        self.PATH_TO_DEBTORS = "D:\\GitHub projects\\honey_income_accounting\\txt_files\\debtors.txt"
        self.end_result = self.get_end_result()

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

            #Обновление общей инфы.
            self.end_result = new_result 

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

    def push_debtor_to_customer(self, customer_name, quantity_of_jars, price_for_jar):
        """Занесение к списку покупателей из списка должников."""
        with open(self.PATH_TO_OUTPUT, 'r', encoding="UTF-8") as file:
            # Вытаскивание данных.
            file_data = file.readlines()

        with open(self.PATH_TO_OUTPUT, 'w', encoding="UTF-8") as file:
            # Запись данных обратно, с добавлением нового покупателя и обновленной цены.
            old_quantity, old_price = map(int, file_data[-1].split()[3::4])
            new_quantity = old_quantity + quantity_of_jars
            new_price = old_price + (price_for_jar * quantity_of_jars)
            new_result = f"\nКоличество проданных банок: {new_quantity} Количество заработанных денег: {new_price} руб."

            #Обновление общей инфы.
            self.end_result = new_result 

            # Удаление устаревшой информации о цене и количестве купленных банок.
            del(file_data[-1])

            # Добавление в файл новой информации
            customer_info = f"{customer_name}    {quantity_of_jars}    {price_for_jar}"
            file_data.append(customer_info)
            file_data.append(new_result)

            for data in file_data:
                file.write(data)
        
        #Показ пользователю, что все хорошо.
        QMessageBox.information(self, "Успешно!", "Должник удален из списка должников и занесен в список покупателей.")

    def push_debtor_info(self):
        """Занос данных должника.""" 
        #Проверка на валидабельность пользователем.
        quest_correctness = QMessageBox.question(self, 
                            "Проверка корректности", "Проверьте на корректность введенные даннные. Если все правильно нажмите 'Yes'.")
        if quest_correctness == QMessageBox.No:
            return 0
        
        #Получение информации с полей для должников.
        debtor_name = self.led_debtor_name.text()
        deb_num_of_jars = int(self.led_debtor_num_of_jars.text())
        deb_price_for_jar = int(self.led_debtor_price_of_jar.text())

        with open(self.PATH_TO_DEBTORS, 'a', encoding="UTF-8") as file:
            debtor_all_info = f"{debtor_name}    {deb_num_of_jars}    {int(deb_price_for_jar)}\n" 
            file.write(debtor_all_info)

        #Показ пользователю, что все хорошо.
        QMessageBox.information(self, "Успешно!", "Должник занесен!")
    
    def remove_debtor(self):
        """Убирание из списка должников должника."""
        #Проверка на валидабельность пользователем.
        quest_correctness = QMessageBox.question(self, 
                            "Проверка корректности", "Проверьте на корректность введенные даннные. Если все правильно нажмите 'Yes'.")
        if quest_correctness == QMessageBox.No:
            return 0
        
        #Получение информации с полей убора должников.
        debtor_name = self.led_debtor_remove_name.text()

        with open(self.PATH_TO_DEBTORS, 'r', encoding="UTF-8") as file:
            debtors = file.readlines() 

            #Пробегание по именам должников и убирание нужного.
            for ind_debtor in range(len(debtors)):
                debtor = debtors[ind_debtor].split()
                if debtor[0] == debtor_name:
                    self.push_debtor_to_customer(debtor[0], int(debtor[1]), int(debtor[2]))
                    del(debtors[ind_debtor])
                    break
        
        #Открытие файла для записи обратно.
        with open(self.PATH_TO_DEBTORS, 'w', encoding="UTF-8") as file:
            file.writelines(debtors)
    
    def get_main_data(self):
        """Получение количества проданных банок и заработок с них."""
        QMessageBox.information(self, "Информация", self.end_result)

    def get_end_result(self):
        """Получение заработка."""
        with open(self.PATH_TO_OUTPUT, 'r', encoding="UTF-8") as file:
            end_result = file.readlines()[-1]
        return end_result


if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = HoneyIncomeAccounting()
    program.show()
    sys.exit(app.exec_())
