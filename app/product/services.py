import requests

def getProducts():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    if response.ok:
            data = response.json()
            # print(len(data))
            return data

# getProducts()

def getProductInfo(prod_id):
    url = f'https://fakestoreapi.com/products/{prod_id}'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        # print(data['id'])
        return data

# getProductInfo(1)