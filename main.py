import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('project2.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://my-final-project-be3b9-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')
ref.set({
    'Products':
        {
            'item_1': {
                'product_id': '001',
                'product_name': 'sugar',
                'quantity_have': 29,
                'quantity_sold': 22,
                'price_dollars': 3

            },
            'item_2': {
                'product_id': '002',
                'product_name': 'salt',
                'quantity_have': 35,
                'quantity_sold': 22,
                'price_dollars': 1.75


            }
        }
})
