import re

import mysql.connector

from connection_class import Conexao, connection

db = Conexao(connection, 'teste')
print(db.mostrar_tudo())
db.adicionar(434, 434)
db.fechar_conexao()
