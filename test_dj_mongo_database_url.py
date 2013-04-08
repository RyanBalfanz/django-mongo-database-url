# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import unittest

import dj_mongo_database_url


MONGOLAB_URL = "mongodb://username:password@ds029297.mongolab.com:29297/my_db"


class DatabaseTestSuite(unittest.TestCase):

    def test_truth(self):
        assert True

    def test_mongodb_parsing(self):
        url = 'mongodb://username:password@ds029297.mongolab.com:29297/my_db?my_option=true'
        url = dj_mongo_database_url.parse(url)

        assert url['NAME'] == 'my_db'
        assert url['HOST'] == 'ds029297.mongolab.com'
        assert url['USER'] == 'username'
        assert url['PASSWORD'] == 'password'
        assert url['PORT'] == 29297

    def test_database_url(self):
        a = dj_mongo_database_url.config()
        assert not a

        os.environ['MONGO_DATABASE_URL'] = 'mongodb://username:password@ds029297.mongolab.com:29297/my_db'

        url = dj_mongo_database_url.config()

        assert url['NAME'] == 'my_db'
        assert url['HOST'] == 'ds029297.mongolab.com'
        assert url['USER'] == 'username'
        assert url['PASSWORD'] == 'password'
        assert url['PORT'] == 29297


if __name__ == '__main__':
    unittest.main()
