import unittest

from repo import user_info


class testrepo(unittest.TestCase):
    def test_res(self):
        expected = ['User: ',
                    'Repo:', 'Number of commits:']

        self.assertEqual(user_info(), expected)

    def test_error_user(self):
        self.assertEqual(user_info)('zyx123'),  'error in user/repo'
        self.assertEqual(user_info(''), 'error in user/repo')


if __name__ == '__main__':
    unittest.main()
