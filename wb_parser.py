from Helpers.data_loader import DataLoader
from Helpers.data_saver import DataSaver

def main():
    load_from_file = True # True если уже загружали все данные с wildberries и нет смысла напрягать сервер еще раз

    data_loader = DataLoader(load_from_file=load_from_file)
    loaded_products = data_loader.load_data()

    data_saver = DataSaver()

    if not load_from_file:
        data_saver.make_response_file(loaded_products)

    print("Задача завершена")

if __name__ == "__main__":
    main()