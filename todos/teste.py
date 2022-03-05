import unittest.mock
import os
import rds


@unittest.mock.patch.dict('os.environ', {'DB_NAME': '1',
                                         'db_password': '2',
                                         'db_name_user': '3',
                                         'rds-instance-endpoint': '4'})
class MyTestCase1(unittest.TestCase):

    def test_feature_one(self):
        self.assertEqual(os.environ['DB_NAME'], '1')
        self.assertEqual(os.environ['db_password'], '2')
        self.assertEqual(os.environ['db_name_user'], '3')
        self.assertEqual(os.environ['rds-instance-endpoint'], '4')

        with self.assertRaises(Exception) as context:
            rds.handler()
            self.assertTrue('This is broken' in str(context.exception))


if __name__ == '__main__':
        unittest.main()