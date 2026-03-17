import mysql.connector
from mysql.connector import Error

class ItemDatabase:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host='localhost',
            user='cafe_user',
            password='Cafe123',
            database='cafe'
            )
        self.cursor = self.conn.cursor()

    def get_item(self, id):
        query = "SELECT * FROM items WHERE id=%s"
        self.cursor.execute(query, (id,))
        res = self.cursor.fetchone()
        if not res:
            return None
        item_dict={}
        item_dict["id"]=res[0]
        item_dict["item"]=res[1]
        item_dict["price"]=res[2]
        return item_dict

    def get_items(self):
        query = "SELECT * FROM items"
        result = []
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict={}
            item_dict["id"]=row[0]
            item_dict["item"]=row[1]
            item_dict["price"]=row[2]
            result.append(item_dict)
        return result

    def add_item(self,body):
        item=body.get('item')
        price=body.get('price')
        query = "INSERT INTO items (item, price) VALUES ( %s, %s)"
        self.cursor.execute(query, (item,price))
        self.conn.commit()

    def put_item(self, id, body):
        item=body.get('item')
        price=body.get('price')
        query = f"UPDATE items SET item=%s, price=%s WHERE id=%s"
        self.cursor.execute(query, (item,price,id))
        self.conn.commit()

    def del_item(self, id):
        query = "DELETE FROM items WHERE id=%s"
        self.cursor.execute(query, (id,))
        self.conn.commit()





# class Items():
#     __tablename__ = 'items'
#     id = db.Column(db.Integer, primary_key = True)
#     item = db.Column(db.String(100), nullable = False)
#     price = db.Column(db.Integer, nullable = False)

#     def repr(self):
#         return f"item: {self.item} - price: {self.price}"

# items = {
#     101 : {
#         "item": "Momos",
#         "price": 100
#     },
#     102: {
#         "item": "Pakoda",
#         "price": 50
#     }
# }