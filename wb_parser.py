from Helpers.data_loader import DataLoader
from Helpers.data_saver import DataSaver
from Helpers.data_parser import DataParser

def main():
    load_from_file = False # True если уже загружали все данные с wildberries и нет смысла напрягать сервер еще раз

    data_loader = DataLoader(load_from_file=load_from_file)
    loaded_products = data_loader.load_data()

    data_saver = DataSaver()

    if not load_from_file:
        data_saver.make_response_file(loaded_products)
        loaded_products = loaded_products['products']
    
    data_parser = DataParser()
    parsed_products = data_parser.parse(loaded_products=loaded_products)
    sorted_products = data_parser.parse(loaded_products=loaded_products, need_sort=True)

    data_saver.save_xlsx(rows=parsed_products, output_path="Data/output.xlsx")
    data_saver.save_xlsx(rows=sorted_products, output_path="Data/sorted_output.xlsx")

    print("Задача завершена")

if __name__ == "__main__":
    main()