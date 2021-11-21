from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from User import User

client = MongoClient('mongodb+srv://admin01:admin0_1@chatdwh.tpxj1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
chat_DB = client.get_database('ChatDB')

users = chat_DB.get_collection('users')
rooms = chat_DB.get_collection("rooms")
room_members = chat_DB.get_collection("room_members")

def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users.insert_one({'_id': username, 'email': email, 'password':password_hash }) # подчеркивание определяет ключ

def get_user(username):
    user_info = users.find_one({'_id':username})
    if user_info is not None :
        return User(user_info['_id'], user_info['email'], user_info['password'])
    else:
        return None

# save_user('Alex', 'al@yandex.ru', '123456')