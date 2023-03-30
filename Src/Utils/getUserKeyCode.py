import random
from urllib.parse import quote
from Src.Utils.mongoScrape import get_specific_key_value, create_mongo_connection

password = "veHt1JK5"
encoded_password = quote(password)
user_name = 'qa_agency'
db_name = "trado_qa"
user_id = '6419e3027b57055c78b50ff2'



def find_db_login_key():
    db = create_mongo_connection(user_name, encoded_password, db_name)
    user_login_code = get_specific_key_value(db, 'users', user_id, 'loginCode')
    print(user_login_code)
    return user_login_code

def find_db_login_key_register(phone):
    db = create_mongo_connection(user_name, encoded_password, db_name)
    collection = db['users']
    object = collection.find_one({"phone": phone})
    phone_code = object['loginCode']
    return phone_code

def generate_phone_number():
    phone_number = "051"
    for number in range(7):
        random_number = str(random.randint(0,9))
        phone_number = phone_number + random_number
    return phone_number
