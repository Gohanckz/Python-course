#!/usr/bin/python
# -*- coding: utf-8 -*-

# Enviar correo Gmail con Python

import smtplib

remitente = 'codigodata@gmail.com'
destinatario = 'carlosblancogomez69@gmail.com'
msg = 'Correo enviado utilizano Python + smtplib en www.codigodata.com'

# Datos
username = 'codigodata@gmail.com'
password = 'alzamanito'

# Enviando el correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(remitente, destinatario, msg)
server.quit()

# otro ejemplo de envío de correo esta vez sólo con smtlib que esta incluida como librería standard y envío con gmail