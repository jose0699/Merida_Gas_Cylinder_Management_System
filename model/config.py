# Refleja la conexion a la base de datos de MYSQL

import pymysql
class Db:
    #metodo constructor instancia conecciona la base de datos y el cursor
    def __init__(self):
        self.connection = connection = pymysql.connect(host="localhost", user="root", password="", database="bombonas_sector_merida")
        self.cursor = self.connection.cursor()
    
    #devuelve true o flase
    def fetchone(self, q, parameters=None):
        self.cursor.execute(q, parameters)
        resultado = self.cursor.fetchone()
        self.connection.close()
        return resultado is not None
    
    #devuele todos los registros
    def fetchall(self, sql):
        conexion = self.connection
        array = []
        with conexion.cursor() as cursor:
            cursor.execute(sql)
            array = cursor.fetchall()
        conexion.close()
        return array
    
    #actualizar registro
    def actualizar(self, sql, parameters=None):
        conexion = self.connection
        with conexion.cursor() as cursor:
            cursor.execute(sql,parameters)
        conexion.commit()
        conexion.close()
        return True
    
    #inserttar registro
    def insertar(self, sql):
        conexion = self.connection
        with conexion.cursor() as cursor:
            cursor.execute(sql)
        conexion.commit()
        conexion.close()
        return True
