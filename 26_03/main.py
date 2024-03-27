#
from repositorio import *
from db import *

db_connec = PostgresDB()
repo = Repositorio()
db_connec2 = MySQLDB()
repo.insert(db_connec)
repo.select(db_connec)
repo.insert(db_connec2)
repo.select(db_connec2)