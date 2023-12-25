from api.client import Client


class KaziAdminApi(Client):
    BASE_URL = "localhost"
    CATEGORIES_BY_CATEGORY = "/categories-by-category/"
    CATEGORIES_BY_SEARCH = "/categories-by-search/"
    USERS = "/users/"
    TAGS = "/tags/"
    TAGS_BY_SOURCE = "/tags-by-source/"
    CATEGORY_TAGS = "/category-tags/"
    PRODUCT_CATEGORY = "/product-category/"

    def kazi_admin_categories_by_category_create(self, token: str, category: int, list_categories: list):
        """
        Add categories by categories

        :method: POST
        :route: /categories-by-category/
        :status:
        :return: Response.
        """
        url = self.BASE_URL + self.CATEGORIES_BY_CATEGORY
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        json = {
            "product_category": category,
            "action_categories": list_categories
        }
        return self.post(url, headers, json)

    def kazi_admin_categories_by_category_destroy(self, token: str, category: int, list_categories: list):
        """
        Delete categories by category

        :method: DELETE
        :route: /categories-by-category/
        :status:
        :return: Response.
        """
        url = self.BASE_URL + self.CATEGORIES_BY_CATEGORY
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        json = {
            "product_category": category,
            "action_categories": list_categories
        }
        return self.delete(url, headers, json)

    def kazi_admin_categories_by_search_create(self, token: str, category: list):
        """
        Add categories by search

        :method: POST
        :route: /categories-by-search/
        :status:
        :return: Response.
        """
        url = self.BASE_URL + self.CATEGORIES_BY_SEARCH
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        json = {
            "categories": category,
            "search": "rings"
        }
        return self.post(url, headers, json)

    def kazi_admin_list_users(self, token: str):
        """
        Get list users

        :method: GET
        :route: /users/
        :status: 200
        :return: Response.
        """
        url = self.BASE_URL + self.USERS
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        return self.get(url, headers)

    def kazi_admin_tags_list(self, token: str):
        """
        Get list tags

        :method: GET
        :route: /tags/
        :status: 200
        :return: Response.
        """
        url = self.BASE_URL + self.TAGS
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        return self.get(url, headers)

    def kazi_admin_tags_create(self, token: str, **kwargs):
        """
        Create tags

        :method: POST
        :route: /tags/
        :status:
        :return: Response.
        """
        url = self.BASE_URL + self.TAGS
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        body = {**kwargs}
        return self.post(url, headers, body)

    def kazi_admin_tags_by_source_create(self, token: str, id: list, source: str):
        """
        Add tags by source

        :method: POST
        :route: /tags_by source/
        :status: 201
        :return: Response.
        """
        url = self.BASE_URL + self.TAGS_BY_SOURCE
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        body = {
            "tags": id,
            "source": source
        }
        return self.post(url, headers, body)

    def kazi_admin_tags_by_source_destroy(self, token: str, id: list, source: str):
        """
        Delete tags by source

        :method: DELETE
        :route: /tags_by source/
        :status: 200
        :return: Response.
        """
        url = self.BASE_URL + self.TAGS_BY_SOURCE
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        body = {
            "tags": id,
            "source": source
        }
        return self.delete(url, headers, body)

    def kazi_admin_category_tags_create(self, token: str, id: list, category: int):
        """
        Add tags by category

        :method: POST
        :route: /category_tags/
        :status:
        :return: Response.
        """
        url = self.BASE_URL + self.CATEGORY_TAGS
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        body = {
            "tags": id,
            "category": category
        }
        return self.post(url, headers, body)

    def kazi_admin_category_tags_destroy(self, token: str, id: list, category: int):
        """
        Delete tags by category

        :method: DELETE
        :route: /category_tags/
        :status:
        :return: Response.
        """
        url = self.BASE_URL + self.CATEGORY_TAGS
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        body = {
            "tags": id,
            "category": category
        }
        return self.delete(url, headers, body)

    def kazi_admin_product_category_create(self, token, product: int, category: list):
        """
        Add product by category

        :method: POST
        :route: /product_category/
        :status:
        :return: Response.
        """
        url = self.BASE_URL + self.PRODUCT_CATEGORY
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        body = {
            "products": product,
            "categories": [category]
        }
        return self.post(url, headers, body)

    def kazi_admin_product_category_destroy(self, token, product: int, category: list):
        """
        Delete product by category

        :method: DELETE
        :route: /product_category/
        :status:
        :return: Response.
        """
        url = self.BASE_URL + self.PRODUCT_CATEGORY
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        body = {
            "products": product,
            "categories": [category]
        }
        return self.delete(url, headers, body)


kazi_admin_api = KaziAdminApi()
