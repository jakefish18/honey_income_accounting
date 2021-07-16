class HoneyIncomeAccounting:
    """Класс программы cобирающей данные и выовдящий результаты в output.txt."""

    def __init__(self):
        self.PATH_TO_OUTPUT = "D:\\GitHub projects\\honey_income_accounting\\txt_files\\output.txt"

    def get_customer_info(self):
        """Получение информации о покупке меда."""
        customer_name = input("Имя покупателя:")
        quantity_of_jars = int(input("Количество банок меда:"))
        price_for_jar = int(input("Цена за банку меда:"))

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


if __name__ == "__main__":
    program = HoneyIncomeAccounting()
    program.get_customer_info()