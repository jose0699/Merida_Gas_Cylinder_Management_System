from flask import session
# from datetime import datetime
# from io import BytesIO
# from fpdf import FPDF
# from model.config import Db

class Acciones():
	# verfificar si un campo esta vacio
	def val_cam_vacio(self, var):
		text = len(var)
		if text == 0:
			return False
		else:
			return True 
	# verificar si la session existe
	def session(self):
		if 'id_usu_log' in session:
			log = True
		else:
			log = False
		return log
	#destruir sessiones creadas para cerrar session
	def cerrar_session(self):
		session.clear()
	# crear excel
	def reporte_clientes(self):
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font("Arial", size=12)
		pdf.cell(200, 10, txt="Notas de ", ln=1, align="C")
		pdf.cell(200, 20, txt="Materia               Nota1               Nota2               Nota3               Nota final", ln=1)
        
		pdf.output("notas.pdf")
		return 1