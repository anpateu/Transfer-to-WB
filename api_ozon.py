import requests

class OzonAPI:
    def __init__(self, client_id, api_key):
        self.client_id = client_id
        self.api_key = api_key

    def load_products(self, last_id, limit, offer_ids):
        endpoint = "https://api-seller.ozon.ru/v2/product/list"
        headers = {
            "Client-Id": self.client_id,
            "Api-Key": self.api_key
            }
        data = {
            "last_id": last_id,
            "limit": limit
            }
        response = requests.post(endpoint, headers=headers, json=data)

        if response.status_code == 200:
            if limit == 1:
                return response.json()["result"]["total"]
            else:
                for item in response.json()["result"]["items"]:
                    offer_ids.append(item["offer_id"])
                return offer_ids, response.json()["result"]["last_id"]

        else:
            print("Error: Request returned status code", response.status_code, "with message", response.reason)

    def check_info(self, offer_id):
        endpoint = "https://api-seller.ozon.ru/v2/product/info"
        headers = {
            "Client-Id": self.client_id,
            "Api-Key": self.api_key
        }
        data = {
            "offer_id": offer_id
        }
        response = requests.post(endpoint, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["result"]

        else:
            print("Error: Request returned status code", response.status_code, "with message", response.reason)

    def check_attributes(self, offer_id):
        endpoint = "https://api-seller.ozon.ru/v3/products/info/attributes"
        headers = {
            "Client-Id": self.client_id,
            "Api-Key": self.api_key
        }
        data = {
            "filter": {
                "offer_id": [
                    offer_id
                ]
            },
            "limit": 1
        }
        response = requests.post(endpoint, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["result"]

        else:
            print("Error: Request returned status code", response.status_code, "with message", response.reason)