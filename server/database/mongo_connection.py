from logging import info

import motor.motor_asyncio

from server.common.mongo_config import ProjectConfigMongo


class MongoConnection:

    def __init__(self, config: ProjectConfigMongo):
        self.config = config
        self.client = self.connect()

    def connect(self):
        url = self.config.get_url()

        info(f'Connect by Mongo url {url}')

        return motor.motor_asyncio.AsyncIOMotorClient(url)

    def get_employees(self):
        return self.client[self.config.get_database()]['employees']
