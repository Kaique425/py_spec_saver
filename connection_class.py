import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(
    host='localhost',
    database='pc_spec',
    user='root',
    password='KSunimed197')


class Conexao:
    def __init__(self, conexao, table):
        self.table_name = table
        self.conexao = conexao
        self.cursor = conexao.cursor(buffered=True)
        self.execute = self.cursor.execute
        self.execute('select database();')

    def databases(self):
        self.execute('select database();')
        self.execute('show databases')
        databases = self.cursor.fetchall()
        return databases

    def mostrar_tudo(self):
        self.execute(f'select * from {self.table_name};')
        dados = self.cursor.fetchall()
        return dados

    def adicionar(self, nome, idade):
        try:
            self.execute(
                f'insert into {self.table_name} values("{nome}", {idade});')
            self.conexao.commit()
            print('adicionado')
        except Error as e:
            print(f'Erro: {e}')

    def fechar_conexao(self):
        self.conexao.close()
