def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Tablet"
    }]

def get_products(kw):
    products = [{
        "id": 1,
        "name": "IPhone 13",
        "price": 20000000,
        "image": "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-13_2_.png",
        "category_id": 1
    }, {
        "id": 2,
        "name": "IPhone 15 Pro Max",
        "price": 40000000,
        "image": "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-pro-max_3.png",
        "category_id": 2
    }, {
        "id": 3,
        "name": "SumSung S22 Ultra",
        "price": 25000000,
        "image": "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/s/a/samsung-galaxy-s22-ultra-12gb-256gb.png",
        "category_id": 3
    }, {
        "id": 4,
        "name": "IPhone 13 Pro",
        "price": 22000000,
        "image": "https://cdn2.cellphones.com.vn/x/media/catalog/product/1/_/1_66_6_2_4.jpg",
        "category_id": 4
    }, {
        "id": 5,
        "name": "ROG Phone 5",
        "price": 18000000,
        "image": "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/a/s/asus-rog-phone-5_0002_gsmarena_001.jpg",
        "category_id": 1
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products