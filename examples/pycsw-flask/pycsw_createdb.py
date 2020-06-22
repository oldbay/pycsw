import json

from pycsw.core import admin

with open("config.json", "r") as file_:
    pycsw_config = json.load(file_)


def create():
    database = pycsw_config['repository']['database']
    table = pycsw_config['repository']['table']
    home = pycsw_config['server']['home']
    
    admin.setup_db(database, table, home)

if __name__ == "__main__":
    create()
    