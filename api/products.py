from api.client import Client


class ProductsApi(Client):
    BASE_URL = 'localhost'
    PRODUCTS = "/products/"
    KAZI_ADMIN = "/kazi_admin"

    def products_list(self):
        """
         Get product list

        :method: GET
        :route: /products/
        :status: 200
        :return: Response.
        """
        url = self.BASE_URL + self.PRODUCTS
        return self.get(url)

    def products_param_category(self, id_category: int, token: str):
        """
         Get admin product by id .

        :method: GET
        :route: /kazi_admin/products/
        :status: 200
        :return: Response.
        """
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        params = f"category={id_category}"
        url = self.BASE_URL + self.KAZI_ADMIN + self.PRODUCTS
        return self.get(url, headers, params)

    def products_retrieve(self, token: str, id: int):
        """
         Get product by id.

        :method: GET
        :route: /products/
        :status: 200
        :return: Response.
        """
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        url = self.BASE_URL + self.PRODUCTS + f"{id}"
        return self.get(url, headers)


products_api = ProductsApi()
