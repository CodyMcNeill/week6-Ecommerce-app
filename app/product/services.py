import requests

def getProducts():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    if response.ok:
            data = response.json()
            return data
# getProducts()

def getProductID():
    data = getProducts()
    for i in data:
        prod_id = i['id']
        return prod_id
        # print(prod_id)
    # print(data)
            
# getProductID()