"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import unittest

from django.test import TestCase
from django.test.client import Client

from .models import UserMeta, User

import pprint
pp = pprint.PrettyPrinter(indent=4)


class TestUserMeta(TestCase):
    def test_create_meta(self):
        user = User.objects.create(username="bobby", email="bobby@dot.com")

        user.meta.create(key="favorite_animal", value="penguin")
        user.meta.create(key="some_important_id", value=123456789)

        #pp.pprint(user.__dict__)

        #pp.pprint(user.meta.values())

        self.assertEqual(
            unicode(user.meta.get(key="favorite_animal")),
            "penguin")

        self.assertEqual(
            unicode(user.meta.get(key="some_important_id")),
            "123456789")

        try:
            user.meta.create(key="favorite_animal", value="penguin")
        except Exception, e:
            self.assertEqual(
                e.message,
                "columns user_id, key are not unique")

    def test_meta_shortcuts(self):
        user = User.objects.create(username="bobby", email="bobby@dot.com")

        user.meta['favorite_animal'] = "penguin"
        user.meta['some_important_id'] = 123456789

        self.assertEqual(
            user.meta['favorite_animal'],
            "penguin")

        self.assertEqual(
            user.meta['some_important_id'],
            "123456789")

        self.assertIn('favorite_animal', user.meta)

        del user.meta['favorite_animal']

        self.assertNotIn('favorite_animal', user.meta)

        self.assertEqual(
            user.meta['favorite_animal'],
            None)
