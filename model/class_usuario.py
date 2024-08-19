from flask import Flask, session
from datetime import datetime
import json
from model.config import Db

class Usuarios():
	# inicio de sesion en el formulario
    def inicio_sesion(self, usuario, contrasena):
        datos_usu = Db().fetchall("SELECT id_usuario, usuario, contrasena, fk_role FROM usuarios WHERE usuario = '"+usuario+"'")
        contra = ""
        for row in datos_usu:
            contra = row[2]
        if contrasena == contra:
            session['id_usu_log'] = row[0]
            session['usu_log'] = row[1]
            session['fk_role'] = row[3]
            return True
        else:
            return False


    # registrar un usuario
    def registrar_usuario(self, nombre, cedula, usuario, contrasena, correo):
        guar_usu = Db().insertar("INSERT INTO usuarios (nombre, cedula, usuario, correo, contrasena, fk_role) VALUES ('"+ nombre +"', '"+ cedula +"', '"+ usuario +"', '"+ correo +"', '"+ contrasena +"', 2)")
        return guar_usu
    
    # bombonas por persona
    def bombonas_todas(self):
        json_data = []
        datos_db =  Db().fetchall( 
            """
                SELECT tb.nombre, esb.descripcion, esb.id_estatus, eb.id_entraga_bombona 
                    FROM 
                        tamano_bombona tb INNER JOIN  entrega_bombona eb 
                            ON tb.id_bombona = eb.fk_tamano 
                        INNER JOIN estatus_bombona  esb
                            ON esb.id_estatus = eb.fk_estatus_bombona
                        INNER JOIN usuarios us
                            ON us.id_usuario = eb.fk_usuario 
                WHERE fk_usuario =
            """ + str(session['id_usu_log']) )
        n = 0
        for row in datos_db:
            n = n + 1
            json_data.append({                
                "num": str(n), 
                "tamano_bombona": row[0],
                "estatus": row[1],
                "id_estatus": row[2],
                "id_entrega_bombona": row[3]
                })
        return json_data
    
    def bombonas_todas_dos(self, vi_us):
        json_data = []
        datos_db =  Db().fetchall( 
            """
                SELECT tb.nombre, esb.descripcion, esb.id_estatus, eb.id_entraga_bombona 
                    FROM 
                        tamano_bombona tb INNER JOIN  entrega_bombona eb 
                            ON tb.id_bombona = eb.fk_tamano 
                        INNER JOIN estatus_bombona  esb
                            ON esb.id_estatus = eb.fk_estatus_bombona
                        INNER JOIN usuarios us
                            ON us.id_usuario = eb.fk_usuario 
                WHERE fk_usuario =
            """ + str(vi_us ))
        n = 0
        for row in datos_db:
            n = n + 1
            json_data.append({                
                "num": str(n), 
                "tamano_bombona": row[0],
                "estatus": row[1],
                "id_estatus": row[2],
                "id_entrega_bombona": row[3]
                })
        return json_data
    
    # datos de un usuario en especifico
    def datos_usuario(self):
        datos_usuario = Db().fetchall("SELECT nombre, cedula FROM usuarios WHERE id_usuario  = "+ str(session['id_usu_log']) +"")
        return datos_usuario
    

    def datos_usuario_admin(self, cliente):
        datos_usuario = Db().fetchall("SELECT nombre, cedula, correo  FROM usuarios WHERE id_usuario  = "+ str(cliente))
        return datos_usuario
    

    # cantidad de bombonas por usuario
    def catn_bombonas_usu(self):
        catn_bombonas_usu = Db().fetchall("SELECT count(*) FROM entrega_bombona eb WHERE eb.fk_usuario = " + str(session['id_usu_log']))
        return catn_bombonas_usu
    
     # cantidad de bombonas por usuario
    def catn_bombonas_usu_dos(self, vi_us):
        catn_bombonas_usu = Db().fetchall("SELECT count(*) FROM entrega_bombona eb WHERE eb.fk_usuario = " + str(vi_us))
        return catn_bombonas_usu
    
    # mostrar tamaño de bombonas
    def mos_tama_bombo(self):
        mos_tama_bombo = Db().fetchall("SELECT * FROM tamano_bombona")
        return mos_tama_bombo
    
        # mostrar tamaño de bombonas
    def mos_tama_bombo_dos(self):
        mos_tama_bombo = Db().fetchall("SELECT * FROM estatus_bombona")
        return mos_tama_bombo
    
    # insertar bombona de un usuario por si solo
    def guardar_bom(self, tamano_bom):
        bom_guardado = Db().insertar("INSERT INTO entrega_bombona (fk_usuario, fk_tamano, fk_estatus_bombona) VALUES ("+ str(session['id_usu_log']) +", "+ str(tamano_bom) +", 2)")
        return bom_guardado
    
    # eliminar bombona de un usuario en especifico, como cliente
    def eliminar_bombona(self, id_bom):
        eli_bom = Db().insertar("DELETE FROM entrega_bombona WHERE id_entraga_bombona = "+ str(id_bom) +"")
        return eli_bom
    
    #-------------------------------------------------------------------------------------------
    # En esta Parte empezamos a trabajar
    #-------------------------------------------------------------------------------------------

   #Para actualizar la informacion de la bombona de una persona
    def actualizar_bombona_cliente(self, tamano_bom, id_bombona):
        sql = """
            UPDATE entrega_bombona
            SET fk_tamano = %s
            WHERE fk_usuario = %s
            AND id_entraga_bombona = %s
        """
        parameters = (tamano_bom, session['id_usu_log'], id_bombona)
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom


    
    def actualizar_bombona_admin(self, id_bom):
        eli_bom = Db().insertar("UPDATE entrega_bombona SET fk_tamano = "+ str(session('id_usu_log'))+ ", fk_estatus_bombona = " + str(session('fk_estatus')) + "WHERE id_entraga_bombona = "+ str(id_bom))
        return eli_bom
    

    


    def actualizar_usuario_admin(self, id_usuario, ):
        eli_bom = Db().actualizar("UPDATE usuarios SET nombre = " + str(session('nombre'))+ ", cedula ="+ str(session('cedula')) + ", correo = " + str(session('correo'))  + "WHERE id_usuario = "+ str(id_usuario))
        return eli_bom
    
    # Para extraer la informacion de la persona
    def persona_usuario(self):
        json_data = []
        datos_db = Db().fetchall("SELECT us.nombre, us.cedula, us.correo FROM usuarios us")
        n = 0
        for row in datos_db:
            n = n + 1
            json_data.append({                
                "num": str(n), 
                "nombre": row[0],
                "cedula": row[1],
                "correo": row[2]
                })
        return json_data 
    #-------------------------------------------------------------------------------------------------------------------
    def actualizar_estado_cilindro(self, estado, id_bom):
        sql = """
            UPDATE entrega_bombona
            SET fk_estatus_bombona = %s
            WHERE fk_usuario = %s
            AND id_entraga_bombona = %s
        """
        parameters = ( estado, session['id_usu_log'], id_bom)
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom
    
    #-------------------------------------------------------------------------------------------------------------------

    def actualizar_usuario_cliente(self, nombre, correo, contrasena):
        sql = """
            UPDATE usuarios
            SET nombre = %s,
            correo = %s,
            contrasena = %s
            WHERE id_usuario = %s
        """
        parameters = ( nombre, correo , contrasena, session['id_usu_log'])
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom
    
    def actualizar_usuario_cliente_dos(self, nombre):
        sql = """
            UPDATE usuarios
            SET nombre = %s
            WHERE id_usuario = %s
        """
        parameters = ( nombre, session['id_usu_log'])
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom
    
    def actualizar_usuario_cliente_tres(self, correo):
        sql = """
            UPDATE usuarios
            SET correo = %s
            WHERE id_usuario = %s
        """
        parameters = ( correo, session['id_usu_log'])
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom

    def actualizar_usuario_cliente_cuatro(self, contrasena ):
        sql = """
            UPDATE usuarios
            SET  contrasena = %s
            WHERE id_usuario = %s
        """
        parameters = ( contrasena, session['id_usu_log'])
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom   
    
    def actualizar_usuario_cliente_cinco(self, nombre, correo ):
        sql = """
            UPDATE usuarios
            SET nombre = %s,
            correo = %s
            WHERE id_usuario = %s
        """
        parameters = ( nombre, correo, session['id_usu_log'])
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom

    def actualizar_usuario_cliente_seis(self, nombre, contrasena ):
        sql = """
            UPDATE usuarios
            SET nombre = %s,
            contrasena = %s
            WHERE id_usuario = %s
        """
        parameters = ( nombre, contrasena, session['id_usu_log'])
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom


    def actualizar_usuario_cliente_siete(self, correo, contrasena ):
        sql = """
            UPDATE usuarios
            SET correo = %s,
            contrasena = %s
            WHERE id_usuario = %s
        """
        parameters = ( correo, contrasena, session['id_usu_log'])
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom
    
    
    def actualizar_usuario_cliente_ocho(self, nombre, correo, cedula, id_usuario):
            sql = """
                UPDATE usuarios
                SET nombre = %s,
                correo = %s,
                cedula = %s
                WHERE cedula = %s
            """
            parameters = ( nombre, correo, cedula, id_usuario)
            eli_bom = Db().actualizar(sql, parameters)
            return eli_bom
    
    def actualizar_usuario_cliente_nueve(self, cedula, id_usuario ):
        sql = """
            UPDATE usuarios
            SET  cedula = %s
            WHERE cedula = %s
        """
        parameters = ( cedula, id_usuario)
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom  
    
    def actualizar_usuario_cliente_dies(self, nombre, cedula , id_usuario):
        sql = """
            UPDATE usuarios
            SET nombre = %s,
            cedula = %s
            WHERE cedula = %s
        """
        parameters = ( nombre, cedula, id_usuario)
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom
    
    def actualizar_usuario_cliente_once(self, correo, cedula, id_usuario):
        sql = """
            UPDATE usuarios
            SET correo = %s,
            cedula = %s
            WHERE cedula = %s
        """
        parameters = ( correo, cedula, id_usuario)
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom

    def actualizar_usuario_cliente_doce(self, nombre, id_usuario):
        sql = """
            UPDATE usuarios
            SET nombre = %s
            WHERE cedula = %s
        """
        parameters = ( nombre, id_usuario)
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom
 
    def actualizar_usuario_cliente_trece(self, correo, id_usuario):
        sql = """
            UPDATE usuarios
            SET correo = %s
            WHERE cedula = %s
        """
        parameters = ( correo, id_usuario)
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom
    
    def actualizar_usuario_cliente_catorce(self, nombre, correo , id_usuario):
        sql = """
            UPDATE usuarios
            SET nombre = %s,
            correo = %s
            WHERE cedula = %s
        """
        parameters = ( nombre, correo, id_usuario)
        eli_bom = Db().actualizar(sql, parameters)
        return eli_bom