import mysql.connector
from mysql.connector import Error
import hashlib
import os

def hash_new_password(password):
    salt = os.urandom(16)  # Generate a random salt
    pw_hash = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'), 
        salt, 
        10  # Number of iterations (High = Slower/Safer)
    )
    # Store both the salt and the hash in your DB
    # We hex-encode them to store them as strings in MySQL
    return salt.hex() + ":" + pw_hash.hex()

def verify_password(stored_password, provided_password):
    salt_hex, hash_hex = stored_password.split(':')
    salt = bytes.fromhex(salt_hex)
    
    # Re-hash the login attempt
    new_hash = hashlib.pbkdf2_hmac(
        'sha256', 
        provided_password.encode('utf-8'), 
        salt, 
        600000
    )
    
    # Use 'compare_digest' to prevent timing attacks
    return hashlib.compare_digest(new_hash, bytes.fromhex(hash_hex))

class UserDatabase:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host='localhost',
            user='cafe_user',
            password='Cafe123',
            database='cafe'
            )
        self.cursor = self.conn.cursor()

    def get_user(self, id):
        query = "SELECT * FROM users WHERE id=%s"
        self.cursor.execute(query, (id,))
        res = self.cursor.fetchone()
        if not res:
            return None
        item_dict={}
        item_dict["id"]=res[0]
        item_dict["username"]=res[1]
        item_dict["password"]=res[2]
        return item_dict

    def add_user(self,body):
        username=body.get('username')
        password=body.get('password')
        hash_password = hash_new_password(password)
        query = "INSERT INTO users (username, psd) VALUES ( %s, %s)"
        try:
            self.cursor.execute(query, (username,hash_password))
            self.conn.commit()
            return True
        except mysql.connector.errors.IntegrityError:
            return False

    def del_user(self, id):
        query = "DELETE FROM users WHERE id=%s"
        self.cursor.execute(query, (id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def verify_user(self, data):
        username = data.get('username')
        pwd = data.get('password')
        query = "SELECT * FROM users WHERE username = %s AND psd = %s"
        self.cursor.execute(query, (username, pwd))
        result = self.cursor.fetchone()
        if result is not None:
            return result[0]