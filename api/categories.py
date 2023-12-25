from api.client import Client


class CategoriesApi(Client):
    BASE_URL = 'localhost'
    CATEGORIES = '/categories/'
    DELETE_CATEGORIES = '/delete-categories/'

    def categories_list(self):
        """
        Gets a list of categories using a GET request.

        :method: GET
        :route: /categories/
        :status: 200 - OK
        :return: Response.
        """
        url = self.BASE_URL + self.CATEGORIES
        return self.get(url)

    def categories_create(self, token: str, **kwargs):
        """
        Creates a new category using a POST request.

        :method: POST
        :route: /categories/
        :status: 201 - Created
        :return: Response.
        """
        headers = {
            f"Authorization": f"Bearer {token}"
        }

        data = {**kwargs}
        url = self.BASE_URL + self.CATEGORIES
        return self.post(url, headers, data)

    def categories_retrieve(self, id: int):
        """
        Sends a GET request to retrieve a category by its id.

        :method: GET
        :route: /categories/{id}/
        :status: 200 - OK
        :return: Response.
        """
        url = self.BASE_URL + self.CATEGORIES + f"{id}"
        return self.get(url)

    def categories_update(self, id: int, token: str, **kwargs):
        """
        Sends a PUT request to edit a category.

        :method: PUT
        :route: /categories/{id}/
        :status: 200 - OK
        :return: Response.
        """
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        data = {**kwargs}

        url = self.BASE_URL + self.CATEGORIES + f"{id}/"
        return self.put(url, headers, data)

    def categories_destroy(self, list_id: list, token: str):
        """
         Delete categories from a list.

        :method: DELETE
        :route: /delete-categories/
        :status: 204
        :return: Response.
        """
        headers = {
            f"Authorization": f"Bearer {token}"
        }
        payload = {
            "categories": [list_id]
        }

        url = self.BASE_URL + self.DELETE_CATEGORIES
        return self.delete(url, headers, json=payload)


categories_api = CategoriesApi()
