from api.client import Client


class ProductsRecomendationApi(Client):
    BASE_URL = 'localhost'
    PRODUCTS_RECOMENDATION = '/products-recomendation/'

    def products_recomendation_retrieve(self, token: str):
        """
         Get product recomendation.

        :method: GET
        :route: /products-recomendation/
        :status: 200
        :return: Response.
        """
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        url = self.BASE_URL + self.PRODUCTS_RECOMENDATION
        return self.get(url, headers)


products_recomendation_api = ProductsRecomendationApi()
