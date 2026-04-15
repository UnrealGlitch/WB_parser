if __name__ == "__main__":
    raise Exception("Нужно запускать wb_parser.py")

class DataParser:

    def __init__(self):
        pass

    def __product_url(self, id: int) -> str:
        return f"https://www.wildberries.ru/catalog/{id}/detail.aspx"
    
    def __seller_url(self, supplier_id: int) -> str:
        return f"https://www.wildberries.ru/seller/{supplier_id}"

    def __cost_to_rubles(self, value: int) -> str:
        return f"{value / 100}"

    def parse(self, loaded_products: list[dict]) -> list[dict]:
        rows = []
        for product in loaded_products:
            id = product.get("id", 0)
            pics = product.get("pics", 0)
    
            sizes_list = product.get("sizes", [])
    
            size_names = ""
            for s in sizes_list:
                if s.get("name"):
                    size_names = ", ".join((s.get("name"), size_names))
            
            total_qty = product.get("totalQuantity", 0)
    
            price_rub = ""
            for s in sizes_list:
                pr = s.get("price", {})
                if pr.get("product"):
                    price_rub = self.__cost_to_rubles(pr["product"])
                    break
            
            color = ""
            for c in product.get("colors", []):
                color = ", ".join((c.get("name", ""), color))
    
            rows.append({
                "Ссылка на товар":          self.__product_url(id),
                "Артикул":                  id,
                "Название":                 product.get("name", ""),
                "Цена (руб)":               price_rub,
                "Описание":                 "", # недоступно в каталоге
                "Ссылки на изображения":    pics, # айдишники картинок
                "Бренд":                    product.get("brand", ""),
                "Тип товара":               product.get("entity", ""),
                "Цвет":                     color,
                "Рейтинг":                  product.get("reviewRating", 0),
                "Количество отзывов":       product.get("feedbacks", 0),
                "Размеры":                  size_names,
                "Остатки":                  total_qty,
                "Название селлера":         product.get("supplier", ""),
                "Ссылка на селлера":        self.__seller_url(product.get("supplierId", 0)),
                "Рейтинг селлера":          product.get("supplierRating", 0),
            })
        return rows