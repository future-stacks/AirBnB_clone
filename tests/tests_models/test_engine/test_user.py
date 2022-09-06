#!/usr/bin/python3
"""
This module is designed to test the user model
"""
import unittest
import os
from unittest.mock import patch
from datetime import datetime
from io import StringIO
import uuid
import models.base_model
from models.user import User


class TestUser(unittest.TestCase):
    """
    Class to define the unittest
    """

    def test_user(self):
        """
        Test the UserModel class
        """
        b = User()
        self.assertIsInstance(b, models.base_model.BaseModel)
        self.assertTrue(issubclass(type(b), models.base_model.BaseModel))
        with patch('models.base_model.uuid4') as mock_id:
            mock_id.return_value = str(
                uuid.UUID("b6a6e15c-c67d-4312-9a75-9d084935e579"))

            base = User()
            self.assertEqual(base.id, "b6a6e15c-c67d-4312-9a75-9d084935e579")

        with patch('models.base_model.datetime') as mock_date:
            mock_date.now.return_value = datetime(2022, 8, 7, 19, 2, 19, 10000)
            mock_date.side_effect = lambda *args, **kw: datetime(*args, **kw)

            base = User()
            self.assertEqual(base.created_at, datetime(
                2022, 8, 7, 19, 2, 19, 10000))
            self.assertEqual(type(base.created_at), datetime)
            self.assertEqual(base.updated_at, datetime(
                2022, 8, 7, 19, 2, 19, 10000))
            self.assertEqual(type(base.updated_at), datetime)

        with patch('models.base_model.uuid4') as mock_id:
            with patch('models.base_model.datetime') as mock_date:
                mock_id.return_value = str(
                    uuid.UUID("4c977185-d3f7-4aaa-a46f-c9d27ec4bd5e"))
                mock_date.now.return_value = datetime(
                    2022, 8, 7, 19, 2, 19, 10000)
                mock_date.side_effect = lambda *args, **kw: datetime(
                    *args, **kw)
                b1 = User('foo')
                self.assertEqual(b1.id, "4c977185-d3f7-4aaa-a46f-c9d27ec4bd5e")
                self.assertEqual(b1.created_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.created_at), datetime)
                self.assertEqual(b1.updated_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.updated_at), datetime)

                b1 = User(2)
                self.assertEqual(b1.id, "4c977185-d3f7-4aaa-a46f-c9d27ec4bd5e")
                self.assertEqual(b1.created_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.created_at), datetime)
                self.assertEqual(b1.updated_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.updated_at), datetime)

                b1 = User({})
                self.assertEqual(b1.id, "4c977185-d3f7-4aaa-a46f-c9d27ec4bd5e")
                self.assertEqual(b1.created_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.created_at), datetime)
                self.assertEqual(b1.updated_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.updated_at), datetime)

                b1 = User(2, 'foo')
                self.assertEqual(b1.id, "4c977185-d3f7-4aaa-a46f-c9d27ec4bd5e")
                self.assertEqual(b1.created_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.created_at), datetime)
                self.assertEqual(b1.updated_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.updated_at), datetime)

        clsdict = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                   "created_at": "2017-09-28T21:05:54.119434",
                   "updated_at": "2017-09-28T21:05:54.119434",
                   "__class__": "User"}
        b2 = User(**clsdict)
        self.assertEqual(b2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(b2.created_at, datetime(
            2017, 9, 28, 21, 5, 54, 119434))
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(b2.updated_at, datetime(
            2017, 9, 28, 21, 5, 54, 119434))
        self.assertEqual(type(b2.updated_at), datetime)

        clsdict = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                   "created_at": "2017-09-28T21:05:54.119434",
                   "__class__": "User"}
        b2 = User(**clsdict)
        self.assertEqual(b2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(b2.created_at, datetime(
            2017, 9, 28, 21, 5, 54, 119434))
        self.assertEqual(type(b1.created_at), datetime)
        with self.assertRaises(AttributeError):
            print(b2.updated_at)

        clsdict = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                   "__class__": "User"}
        b2 = User(**clsdict)
        self.assertEqual(b2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        with self.assertRaises(AttributeError):
            print(b2.created_at)
        with self.assertRaises(AttributeError):
            print(b2.updated_at)

    @ patch('sys.stdout', new_callable=StringIO)
    def test_str(self, stdout):
        """
        Test the User class __str__ method
        """
        with patch('models.base_model.uuid4') as mock_id:
            with patch('models.base_model.datetime') as mock_date:
                mock_id.return_value = str(
                    uuid.UUID("b6a6e15c-c67d-4312-9a75-9d084935e579"))
                mock_date.now.return_value = datetime(
                    2017, 9, 28, 21, 5, 54, 119434)
                mock_date.side_effect = lambda *args, **kw: datetime(
                    *args, **kw)
                base = User()
                print(base)
                expted_out = ("[User] "
                              "(b6a6e15c-c67d-4312-9a75-9d084935e579) "
                              "{'id': 'b6a6e15c-c67d-4312-9a75-9d08493"
                              "5e579', 'created_at': datetime.datetime"
                              "(2017, 9, 28, 21, 5, 54, 119434), "
                              "'updated_at': datetime.datetime(2017, "
                              "9, 28, 21, 5, 54, 119434)}\n")
                self.assertEqual(stdout.getvalue(), expted_out)
                stdout.truncate(0)
                stdout.seek(0)

    def test_save(self):
        """
        Test the User class save method
        """
        PATH = 'file.json'
        with patch('models.base_model.uuid4') as mock_id:
            with patch('models.base_model.datetime') as mock_date:
                mock_id.return_value = str(
                    uuid.UUID("788f5f32-d874-4387-872c-e925314ba80a"))
                mock_date.now.return_value = datetime(
                    2017, 9, 28, 21, 5, 54, 119434)
                mock_date.side_effect = lambda *args, **kw: datetime(
                    *args, **kw)
                base = User()
                self.assertEqual(base.updated_at, datetime(
                    2017, 9, 28, 21, 5, 54, 119434))
                mock_date.now.return_value = datetime(
                    2017, 9, 28, 21, 5, 54, 119572)
                base.save()
                self.assertEqual(base.updated_at, datetime(
                    2017, 9, 28, 21, 5, 54, 119572))
                self.assertEqual(os.path.isfile(
                    PATH) and os.access(PATH, os.R_OK), True)
                cont = self.write_file(PATH)
                expected = ('"User.788f5f32-d874-4387-872c-e925314ba80a":'
                            ' {"id": "788f5f32-d874-4387-872c-e925314ba80a", '
                            '"created_at": "2017-09-28T21:05:54.119434", '
                            '"updated_at": "2017-09-28T21:05:54.119572", '
                            '"__class__": "User"}')
                self.assertIn(expected, cont)
        with self.assertRaises(TypeError):
            base.save(2)
        with self.assertRaises(TypeError):
            base.save('foo')
        os.remove(PATH)

    def test_to_dict(self):
        """
        Test the User class to_dict method
        """
        with patch('models.base_model.uuid4') as mock_id:
            with patch('models.base_model.datetime') as mock_date:
                mock_id.return_value = str(
                    uuid.UUID("07331301-1393-4f7f-8da5-1f9be6216ad4"))
                mock_date.now.return_value = datetime(
                    2017, 9, 28, 21, 5, 54, 119434)
                mock_date.side_effect = lambda *args, **kw: datetime(
                    *args, **kw)
                base = User()
                clsdict = {"id": "07331301-1393-4f7f-8da5-1f9be6216ad4",
                           "created_at": "2017-09-28T21:05:54.119434",
                           "updated_at": "2017-09-28T21:05:54.119434",
                           "__class__": "User"}
                self.assertEqual(base.to_dict(), clsdict)

        with self.assertRaises(TypeError):
            base.to_dict(2)
        with self.assertRaises(TypeError):
            base.to_dict('foo')

    def test_attrib(self):
        """
        Test the User class public attributes
        """
        b = User()
        self.assertTrue(hasattr(b, 'email'))
        self.assertEqual(b.email, "")
        self.assertEqual(type(b.email), str)

        self.assertTrue(hasattr(b, 'password'))
        self.assertEqual(b.password, "")
        self.assertEqual(type(b.password), str)

        self.assertTrue(hasattr(b, 'first_name'))
        self.assertEqual(b.first_name, "")
        self.assertEqual(type(b.first_name), str)

        self.assertTrue(hasattr(b, 'last_name'))
        self.assertEqual(b.last_name, "")
        self.assertEqual(type(b.last_name), str)

    @staticmethod
    def write_file(filename):
        """
        A function that opens and reads a file
        Args:
            filename (str)
        Returns:
            number of characters written into file
        """
        with open(filename, 'r', encoding="utf-8") as f:
            text = ""
            for line in f:
                text += line
            return text