import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            #调用password，password的getter操作按理是不能执行的，因为数据库只会存hash
            u.password

    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)
