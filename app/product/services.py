import requests

def getProducts():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    if response.ok:
            data = response.json()
            for i in data:
                product = {}
                product['id'] = i['id']
                product['title'] = i['title']
                product['price'] = i['price']
                product['description'] = i['description']
                product['image'] = i['image']
                print(product)
            return data
getProducts()