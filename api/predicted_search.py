from api.client import Client
from faker import Faker


class PredictedsSearch(Client):
    BASE_URL = 'localhost'
    PREDICTED_SEARCH = "/predicted-search/"

    def __init__(self):
        super().__init__()
        self.fake = Faker()

    def predicted_search_retrieve(self):
        """
         Predicted search, random word

        :method: GET
        :route: /predicted-search/
        :status: 200
        :return: Response.
        """
        url = self.BASE_URL + self.PREDICTED_SEARCH + f"?search={self.fake.word}"
        return self.get(url)


predicted_search = PredictedsSearch()
