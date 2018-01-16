"""
Programa que envía un email a un correo personal
"""

import os
import smtplib

from configobj import ConfigObj
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from errorSendEmail import SendError


def main():
    """
    Función principal donde se recolectan los datos
    y se realiza el envío
    """
    name = 'Usuario anonimo'
    from_addr = 'camd.jun@hotmail.com'
    subject = 'Contactar'
    msg_text = 'Hola quisiera poder hacer un proyecto'
    try:
        send_email(name, from_addr, subject, msg_text)
        print('Correo enviado correctamente.')
    except SendError as inst:
        print(inst.message)
    except Exception:
        print('Error desconocido.')


def send_email(
        name, from_addr, subject, msg_text):
    """
    A partir de los datos obtenidos por el usuario se crea
    las partes del email y se procede a enviarlo
    """
    svr, to_addrs = get_smtp()
    msg = get_msg(name, from_addr, to_addrs, subject, msg_text)
    try:
        svr.send_message(msg, from_addr=from_addr, to_addrs=to_addrs)
    except Exception:
        raise SendError('NO se completó correctamente el envío del correo.')
    svr.quit()


def get_data_config(
        filename):
    """
    Envia los datos almacenados en la configuración
    que está ubicada en la ruta indicada por el
    parametro filename
    Los datos devueltos son 5:
    host, port, user, password, email_to
    """
    if not os.path.exists(filename):
        raise SendError('No se encontró el archivo de configuración')

    config = ConfigObj(filename)
    config_dict = config.dict()
    try:
        host = config_dict['host']
        port = config_dict['port']
        user = config_dict['user']
        password = config_dict['password']
        email_to = config_dict['email_to']
    except Exception:
        raise SendError('La información de configuración no está correcta.')

    if not host or not port or not user or not password or not email_to:
        raise SendError('La información de configuración no está completa.')

    return host, port, user, password, email_to


def get_msg(
        name, from_addr, to_addrs, subject, msg_text):
    """
    Devuelve un objeto MIMEMultipart que es la representación
    completa de las partes que tiene un email
    """
    msg = MIMEMultipart()
    msg['From'] = from_addr
    if(type(to_addrs) == str):
        msg['To'] = to_addrs
    else:
        msg['To'] = ', '.join(to_addrs)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    # Agregando al cuerpo del mensaje
    msg_text = 'Nombre: {}\n' \
        'Email: {}\n' \
        'Mensaje: {}' \
        .format(name, from_addr, msg_text)
    msg.attach(MIMEText(msg_text, 'plain'))

    return msg


def get_smtp():
    """
    Devuelve el objeto SMTP y el email al que se enviará
    el mensaje de contacto
    """

    # Toma de datos del archivo de configuración
    # necesario para iniciar el protocolo SMTP
    path_dir = os.path.dirname(os.path.abspath(__file__))
    path_config = os.path.join(path_dir, 'config.ini')
    host, port, user, password, to_addrs = \
        get_data_config(path_config)

    # Inicio del protocolo SMTP
    try:
        srv = smtplib.SMTP(host=host, port=port)
        srv.ehlo()
        srv.starttls()
        srv.login(user, password)
    except Exception:
        raise SendError('Error al iniciar el protocolo SMTP')

    return srv, to_addrs


if __name__ == '__main__':
    main()
