from flask import Flask, render_template, request, session, redirect, session
from model.class_acciones import Acciones
from model.class_usuario import Usuarios
from model.config import Db

app = Flask(__name__)
app.secret_key = "abc1234"
# ruta raiz
@app.route("/")
def index():
    # si la sesion esta creada redirecionara a inicio
    if Acciones().session() == True:
        if session['fk_role'] == 1:
            return redirect('/administrador')
        else:    
            return redirect('/inicio')
    else:
        return render_template('index.html', login = 0)

# registrame
@app.route("/registrarme")
def registrarme():
    if Acciones().session() == True:
        if session['fk_role'] == 1:
            return redirect('/administrador')
        else:    
            return redirect('/inicio')
    else:
        return render_template("registrar.html")

# guardar registro de un usuario
@app.route("/guardar_registro_cli", methods=['POST'])
def guardar_registro_cli():
    nombre = request.form['nombre']
    cedula = request.form['cedula']
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    correo = request.form['correo']
    hh = Usuarios().registrar_usuario(nombre, cedula, usuario, contrasena, correo)
    return redirect("/")
    
# enviar formulario de inicio de sesion
@app.route("/ini_sesion_usu", methods=['POST'])
def ini_sesion_usu():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    # si algun campo esta vacio
    if Acciones().val_cam_vacio(usuario) == False or Acciones().val_cam_vacio(contrasena) == False:
        return render_template('index.html', log_error=1, text_error='Algun campo esta vacio', usuario=usuario)
    
    login = Usuarios().inicio_sesion(usuario, contrasena)

    # si el usuario inicia sesion correctamente redirecionara a inicio
    if login == True:
        if session['fk_role'] == 1:
            return redirect('/administrador')
        else:    
            return redirect('/inicio')
    else:
        return render_template('index.html', log_error=1, text_error='Usuario o contraseña incorrecto', usuario=usuario)


# mostrar datos de la persona de sus bombonas
# clientes tabla pagos realizados
@app.route("/bombonas_todas", methods=["POST"])
def bombonas_todas():
    return Usuarios().bombonas_todas()

# agregar bombona como cliente
@app.route("/agregar_bombona")
def agregar_bombona():
    return render_template('agregar_bombona.html', tama_bom = Usuarios().mos_tama_bombo())

# guardar bombona como cliente
@app.route("/guardar_bombona", methods=["POST"])
def guardar_bombona():
    tamano_bom = request.form['tamano_bom']
    insert = Usuarios().guardar_bom(tamano_bom)
    return redirect("/inicio")

# eliminar bombona de un usuario propio, como cliente
@app.route("/eliminar_bombona", methods=["POST"])
def eliminar_bombona():
    id_bom = request.form['id_bombona']
    Usuarios().eliminar_bombona(id_bom)
    return redirect("/inicio")

# cerrar session y destruir
@app.route("/cerrar_session")
def cerrar_session():
    Acciones().cerrar_session()
    return redirect('/')

#----------------------------------------------------------------------------
#Cliente
#----------------------------------------------------------------------------

# personal se accede como CLIENTE
@app.route("/inicio")
def inicio():
    if Acciones().session() == False:
        return redirect("/")
    else:
        return render_template('inicio.html', llamar_metodo="ajax.tabla_bombonas", datos_usu = Usuarios().datos_usuario(), datos_cad_bom = Usuarios().catn_bombonas_usu())

@app.route("/inicio", methods=["POST"])
def actualizar_cilindro_cliente():
    tamano_bom = request.form['tamano_bom']
    id_bombona = request.form['id_bombona']
    Usuarios().actualizar_bombona_cliente(tamano_bom, id_bombona)
    return render_template('inicio.html', llamar_metodo="ajax.tabla_bombonas", datos_usu=Usuarios().datos_usuario(), datos_cad_bom=Usuarios().catn_bombonas_usu())

@app.route("/persona_usuario", methods=["POST"])
def persona_usuario():
    return Usuarios().persona_usuario()

#----------------------------------------------------------------------------
# Actualizar datos del  cilindro (cliente)
#----------------------------------------------------------------------------
@app.route("/Inicio/Actualizar/Cilindro")
def actualizar_cilindro():
    #id_bom = request.form['id_bombona']
    return render_template('actualizar.html', tama_bom = Usuarios().mos_tama_bombo())

@app.route("/Inicio/Actualizar/Cilindro", methods=["POST"])
def actualizar_datos_clientes():
    if int(request.form['id_bombon']) != 0:
        id_bom = request.form['id_bombon']
        return render_template('actualizar.html', tama_bom=Usuarios().mos_tama_bombo(), id_bom=id_bom)

#----------------------------------------------------------------------------
# Actualizar datos del cliente
#----------------------------------------------------------------------------

@app.route("/Inicio/Actualizar/Datos")
def actualizar_cliente():
     return render_template('actualizar_datos_usuario.html')

@app.route("/Inicio/Actualizar/Datos", methods=["POST"])
def actualizar_datos_client():
    nombre = request.form['nombre']
    contrasena = request.form['contrasena']
    correo = request.form['correo']
    
    if (not not nombre) and (not not contrasena) and (not not correo):
        hh = Usuarios().actualizar_usuario_cliente(nombre, correo, contrasena)
    
    elif (not not nombre) and (not contrasena) and (not correo):
        hh = Usuarios().actualizar_usuario_cliente_dos(nombre)
    
    elif (not nombre) and (not  contrasena) and (not not correo):
       hh = Usuarios().actualizar_usuario_cliente_tres(correo)
    
    elif (not nombre) and (not not contrasena) and (not  correo):
       hh = Usuarios().actualizar_usuario_cliente_cuatro(contrasena)

    elif (not not nombre) and (not   contrasena) and (not not correo):
       hh = Usuarios().actualizar_usuario_cliente_cinco(nombre, correo)

    elif (not not  nombre) and (not not contrasena) and (not  correo):
       hh = Usuarios().actualizar_usuario_cliente_seis(nombre, contrasena)

    elif (not nombre) and (not not contrasena) and (not not correo):
       hh = Usuarios().actualizar_usuario_cliente_siete(correo, contrasena)
    else:
        return redirect("/inicio")
    
    return redirect("/inicio")  


#----------------------------------------------------------------------------
#Admin
#----------------------------------------------------------------------------
# administrador
@app.route("/administrador")
def administrador():
    return render_template('administrador.html', llamar_metodo="ajax.persona_usuario", datos_usu=Usuarios().datos_usuario(), datos_cad_bom=Usuarios().catn_bombonas_usu())


#----------------------------------------------------------------------------
# Actualizar datos del cliente
#----------------------------------------------------------------------------
#Ruta actualizar
@app.route("/Administrador/Actualizar")
def actualizar_admin():
    return render_template('actualizar_datos_admin.html')

@app.route("/Administrador/Actualizar", methods=["POST"])
def actualizar_cliente_admin():
    if int(request.form['act_us']) != 0:
        act_us = request.form['act_us']
        return render_template('actualizar_datos_admin.html', act_us = act_us)

#Aqui se actualiza los datos del    
@app.route("/Administrador/Actualizar/Datos", methods=["POST"])
def actualizar_cliente_administrador():
        id_usuario = request.form['id_usuario']
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        correo = request.form['correo']
        
        if (not not nombre) and (not not cedula) and (not not correo):
            hh = Usuarios().actualizar_usuario_cliente_ocho(nombre, correo, cedula, id_usuario)
        
        elif (not not nombre) and (not cedula) and (not correo):
            hh = Usuarios().actualizar_usuario_cliente_doce(nombre, id_usuario)
        
        elif (not nombre) and (not  cedula) and (not not correo):
            hh = Usuarios().actualizar_usuario_cliente_trece(correo , id_usuario)
        
        elif (not nombre) and (not not cedula) and (not  correo):
            hh = Usuarios().actualizar_usuario_cliente_nueve(cedula, id_usuario)

        elif (not not nombre) and (not   cedula) and (not not correo):
            hh = Usuarios().actualizar_usuario_cliente_catorce(nombre, correo, id_usuario)

        elif (not not  nombre) and (not not cedula) and (not  correo):
            hh = Usuarios().actualizar_usuario_cliente_dies(nombre, cedula, id_usuario)

        elif (not nombre) and (not not cedula) and (not not correo):
            hh = Usuarios().actualizar_usuario_cliente_once(correo, cedula, id_usuario)
        else:
            return redirect('/administrador')
        
        return redirect('/administrador')    
   
#----------------------------------------------------------------------------
# Menu Visualizar(admin)
#----------------------------------------------------------------------------
@app.route("/Administrador/Visualizar")
def visualizar_admin():
    return render_template('visualizar.html', tama_bom=Usuarios().mos_tama_bombo())
    
#----------------------------------------------------------------------------
# Actualizar datos del  cilindro (admin)
#----------------------------------------------------------------------------
# actualizar tamaño de cilindro del cliente admin
@app.route("/Administrador/Cilindro")
def actualizar_cilindro_admin():
    usuarios = Usuarios()
    session['id_usu_log'] = request.form['vi_us']
    vi_us =  session['id_usu_log']
    datos_usu = usuarios.datos_usuario_admin(session['id_usu_log'])
    datos_cad_bom = usuarios.catn_bombonas_usu_dos(session['id_usu_log'])    
    return render_template('visualizar.html', 
                                datos_usu=datos_usu,
                                vi_us=vi_us,  
                                datos_cad_bom=datos_cad_bom,
                                llamar_metodo="ajax.tabla_bombonas_dos")
   

@app.route("/Administrador/Cilindro", methods=['POST'])
def actualizar_cilindro_admin2():
    usuarios = Usuarios()
    session['id_usu_log'] = request.form['vi_us']
    vi_us = request.form['vi_us']
    datos_usu = usuarios.datos_usuario_admin(vi_us)
    datos_cad_bom = usuarios.catn_bombonas_usu_dos(vi_us)    
    return render_template('visualizar.html', 
                                datos_usu=datos_usu,
                                vi_us=vi_us,  
                                datos_cad_bom=datos_cad_bom,
                                llamar_metodo="ajax.tabla_bombonas_dos")




#  return render_template(', llamar_metodo="ajax.tabla_bombonas",  )
#----------------------------------------------------------------------------
# Actualizar datos del  cilindro (cliente)
#----------------------------------------------------------------------------
@app.route("/Administrador/Actualizar/Cilindro")
def actualizar_cilindros():
    #id_bom = request.form['id_bombona']
    return render_template('actualizar_admin.html', tama_bom = Usuarios().mos_tama_bombo())

@app.route("/Administrador/Actualizar/Cilindro", methods=["POST"])
def actualizar_datos_clientess():
    if int(request.form['id_bombon']) != 0:
        id_bom = request.form['id_bombon']
        return render_template('actualizar.html', tama_bom=Usuarios().mos_tama_bombo(), id_bom=id_bom)
    
#----------------------------------------------------------------------------
#  agregar cilindro (admin)
#----------------------------------------------------------------------------    
@app.route("/Administrador/Cilindro/Agregar")
def agregar_bombona_admin():
    vi_us = session['id_usu_log']
    return render_template('agregar_bombona_admin.html', tama_bom = Usuarios().mos_tama_bombo(), vi_us = vi_us)

@app.route("/Administrador/Cilindro/2", methods=['POST'])
def actualizar_cilindro_admin3():
    usuarios = Usuarios()

    vi_us = session['id_usu_log']
    tamano_bom = request.form['tamano_bom']
    usuarios.guardar_bom(tamano_bom)
    datos_usu = usuarios.datos_usuario_admin(vi_us)
    datos_cad_bom = usuarios.catn_bombonas_usu_dos(vi_us)    
    return render_template('visualizar.html', 
                                datos_usu=datos_usu,
                                vi_us=vi_us,  
                                datos_cad_bom=datos_cad_bom,
                                llamar_metodo="ajax.tabla_bombonas_dos")

#----------------------------------------------------------------------------
# Eliminar cilindro (admin)
#----------------------------------------------------------------------------  
@app.route("/Administrador/Cilindro/5", methods=["POST"])
def actualizar_cilindro_admin5():
    usuarios = Usuarios()

    id_bom = request.form['id_bombona']    
    usuarios.eliminar_bombona(id_bom)

    vi_us =  session['id_usu_log']
    datos_usu = usuarios.datos_usuario_admin(session['id_usu_log'])
    datos_cad_bom = usuarios.catn_bombonas_usu_dos(session['id_usu_log'])    
    return render_template('visualizar.html', 
                                datos_usu=datos_usu,
                                vi_us=vi_us,  
                                datos_cad_bom=datos_cad_bom,
                                llamar_metodo="ajax.tabla_bombonas_dos")

#----------------------------------------------------------------------------
# Actualiza cilindro (admin)
#---------------------------------------------------------------------------- 
@app.route("/Administrador/Cilindro/Actualizar")
def actualizar_bombona_admin():
    return render_template('actualizar_admin.html', tama_bom = Usuarios().mos_tama_bombo_dos())

@app.route("/Administrador/Cilindro/Actualizar", methods=["POST"])
def actualizar_cilindro_estado_admin():
    if int(request.form['id_bombon']) != 0:
        id_bom = request.form['id_bombon']
        return render_template('actualizar_admin.html', tama_bom=Usuarios().mos_tama_bombo_dos(), id_bom=id_bom)
    #return render_template('', tama_bom = Usuarios().mos_tama_bombo(), vi_us = vi_us)

@app.route("/Administrador/Cilindro/3", methods=['POST'])
def actualizar_cilindro_admin4():
    usuarios = Usuarios()

    tamano_bom = request.form['tamano_bom']
    id_bombona = request.form['id_bombona']
    usuarios.actualizar_estado_cilindro(tamano_bom, id_bombona)

    vi_us =   session['id_usu_log'] 
    datos_usu = usuarios.datos_usuario_admin(vi_us)
    datos_cad_bom = usuarios.catn_bombonas_usu_dos(vi_us)    
    return render_template('visualizar.html', 
                                datos_usu=datos_usu,
                                vi_us=vi_us,  
                                datos_cad_bom=datos_cad_bom,
                                llamar_metodo="ajax.tabla_bombonas_dos")
   
#----------------------------------------------------------------------------
# Regresar cilindro (admin)
#----------------------------------------------------------------------------  
@app.route("/Regresar_admin", methods=["GET"])
def Regresar_admin():
    session['id_usu_log'] = 1
    return render_template('administrador.html', llamar_metodo="ajax.persona_usuario",
                            datos_usu=Usuarios().datos_usuario(), 
                            datos_cad_bom=Usuarios().catn_bombonas_usu())


#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#ini servidor
if __name__ == '__main__':
    app.run(port=5000, debug=True)

