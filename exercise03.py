'''
练习3
    编写一个程序,模拟用户注册,登录的 数据库行为
    注册和登录接口 要求用户名不能重复   要包含用户名和密码字段
'''

import pymysql

class User:
    def __init__(self):
        self.db = pymysql.connect(user ='root',passwd='123456',database=database,charset='utf8')
        self.cur




if __name__ =='__main__':

    user = User('stu')

    if user.register('Abby','123'):
        print('注册成功')

    # if user.login('Abby','123'):
    #     print('')