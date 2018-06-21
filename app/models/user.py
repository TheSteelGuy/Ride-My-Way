"""
User class. Contains the relevant methods for the user class
"""


class User():
    '''a base pssanger class from which a driver can be made'''

    def __init__(self, name, phone, pwd, c_pwd):
        ''' constructor method to give a user its attributes'''
        self.name = name
        self.phone = phone
        self.pwd = pwd
        self.c_pwd = c_pwd


    def verify_password(self, pwd, confirm_pass):
        '''verifies if the password and confirm pass matches'''
        if pwd == confirm_pass:
            return True
        return False
