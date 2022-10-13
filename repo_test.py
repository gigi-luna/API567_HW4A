import unittest
from unittest import mock
import pytest

from repo import user_info


class testrepo(unittest.TestCase):

    @unittest.mock.patch('requests.get')
    def test_rep_1(self, mockedReq):
        mockedReq.return_value.json.return_value = [{"name": 'user'}]
        self.assertEqual(user_info())


if __name__ == '__main__':
    print('running unit test')
    unittest.main()
