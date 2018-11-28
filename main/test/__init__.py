# Created by wenchao.jia on 2018/11/28.
# Mail:wenchao.jia@qunar.com
from main.dao import UserDao
from main.model.user import User


def test_dao():
    # User.create(user_name="aaa",password="bbb",salt="ccc",email='dddd',tel='ffff')
    # user = {
    #     "id":1,
    #     "user_name":"aaa",
    #     "password":"bbb",
    #     "salt":"ccc",
    #     "email":"ddd",
    #     "tel":"fff"
    # }
    # UserDao().insert(user)
    user = UserDao().select(1, ['user_name', 'password']).dicts().execute()
    print(user['user_name'])


if __name__ == '__main__':
    test_dao()
