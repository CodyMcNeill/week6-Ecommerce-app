import requests

def getProducts():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    if response.ok:
            data = response.json()
            print(data)
getProducts()