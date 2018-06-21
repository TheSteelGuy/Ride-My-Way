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
    """tests user authentication methods"""
    def test_registration(self):
        """test tregistaration"""
        response = self.client.post(
            '/signup',
            data=json.dumps(self.register_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
