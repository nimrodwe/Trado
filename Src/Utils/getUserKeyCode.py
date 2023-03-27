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
