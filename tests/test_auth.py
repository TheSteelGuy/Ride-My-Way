'''test auth views'''
from flask_testing import TestCase
from flask import request
import unittest 
import json
from app import create_app

class Testbase(TestCase):
    """parent class"""
    def create_app(self):
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        self.client = self.app.test_client()
        self.register_user={
            'username':'testname',
            'phone': '30567263',
            'password':'testpass',
            'confirm_password ':'testpass'
        }
        self.login_user={
            'username':'test user',
            'password':'testpass'
        }

class TestAuth(Testbase):
    '''tests user authentication methods'''
    def test_signup(self):
        """test tregistaration"""
        response = self.client.post(
            '/api/v1/signup',
            data=json.dumps(self.register_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)


    def test_login(self):
        '''tests if a user can log in'''
        self.client.post(
           'auth/api/v1/signup',
           data=json.dumps(self.register_user),
           content_type='application/json'
        )
        sigin = self.cliet.post(
            'auth/api/v1/signin',
            data=json.dumps(self.login_user),
            content_type='application/json'
        )
        self.assertIn('login susccesful', str(login.data)) 


    def test_logout(self):
        '''tests_user logout'''
        
        signup = self.client.post(
            'auth/api/v1/register',
            data=json.dumps(self.register_user),
            content_type='application/json'
        )   
        self.assertEqual(signup.status_code,201) 
        self.data_ = json.loads(signup.data.decode())
        self.assertEqual(self.data_['message'],'registration successfull')

        logout = self.client.post(
            'auth/api/v1/logout',
            content_type='application/json'
        )
        res = json.loads(logout.data.decode())
        self.assertIn('successfully logged out', res['message'])
