import json

from pycsw.core import admin, config

with open("config.json", "r") as file_:
    pycsw_config = json.load(file_)

context = config.StaticContext()


def load(records_dir):
    database = pycsw_config['repository']['database']
    table = pycsw_config['repository']['table']
    
    admin.load_records(
        context, 
        database,
        table,
        records_dir,
        True,
        True, 
    )

if __name__ == "__main__":
    load("records")
    