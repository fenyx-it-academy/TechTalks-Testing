import requests
from pprint import pprint


def fetch_currency(currency):
    """
    this function gets currency as input, adds it to the connection string and makes the API request.
    """

    r = requests.get(f'https://v6.exchangerate-api.com/v6/177238a564c1c9bb78e5f671/latest/{currency}')
    return r.json()




pprint(fetch_currency("USD"))
