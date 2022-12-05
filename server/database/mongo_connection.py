import os
from logging import info

import motor.motor_asyncio

from server.common.mongo_config import ProjectConfigMongo


class MongoConnection:

    def __init__(self, config: ProjectConfigMongo):
        self.config = config
        self.client = self.connect()

    def connect(self):
        url = os.environ['DATABASE_URI']

        info(f'Connect by Mongo url {url}')

        return motor.motor_asyncio.AsyncIOMotorClient(url)

    def get_branches(self):
        return self.client.get_default_database()['branches']

    def get_suppliers(self):
        return self.client.get_default_database()['suppliers']

    def get_sales(self):
        return self.client[self.config.get_database()]['sales']
