import requests


class Client:
    @staticmethod
    def get(url, headers=None, params=None):
        """
        Sends a GET request to the specified URL.

        :param: url: The URL to send the GET request to.
        :param: headers: The request headers.
        :param: params: The request parameters (optional).
        :return: A `Response` object.
        """
        return requests.get(url, headers=headers, params=params)

    @staticmethod
    def post(url, headers=None, json=None, data=None):
        """
        Sends a POST request to the specified URL.

        :param: url: The URL to send the POST request to.
        :param: headers: The request headers.
        :param: json: The request body in JSON format.
        :param: data: The request body in form-data format.
        :return: A `Response` object.
        """
        return requests.post(url, headers=headers, json=json, data=data)

    @staticmethod
    def delete(url, headers=None, json=None, params=None):
        """
        Sends a DELETE request to the specified URL.

        :param: url: The URL to send the DELETE request to.
        :param: headers: The request headers.
        :param: params: The request parameters (optional).
        :return: A `Response` object.
        """
        return requests.delete(url, headers=headers, json=json, params=params)

    @staticmethod
    def patch(url, headers=None, json=None, data=None):
        """
        Sends a PATCH request to the specified URL.

        :param: url: The URL to send the PATCH request to.
        :param: headers: The request headers.
        :param: json: The request body in JSON format.
        :param: data: The request body in form-data format.
        :return: A `Response` object.
        """
        return requests.patch(url, headers=headers, json=json, data=data)

    @staticmethod
    def put(url, headers=None, json=None, data=None):
        """
        Sends a PUT request to the specified URL.

        :param: url: The URL to send the PUT request to.
        :param: headers: The request headers.
        :param: json: The request body in JSON format.
        :param: data: The request body in form-data format.
        :return: A `Response` object.
        """
        return requests.put(url, headers=headers, json=json, data=data)
