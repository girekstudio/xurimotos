import uuid
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from Home.models import Envio_Email
from xurimotos.settings import BASE_DIR

import os

def Attr(cls):
    model= cls.__name__
    return cls.__doc__.replace(model,"").replace("(","").replace(")","").replace(" ","").split(",")

class ResizeImageMixin:
    def resize(self, imageField, ancho, alto, format='JPEG', marca=()):
        im = Image.open(imageField)  # Catch original
        source_image = im.convert('RGBA')
        source_image=source_image.resize((ancho,alto))  # Resize to size

        if marca:
            path=os.path.join(BASE_DIR, 'static/xurimotos.png')
            imgAgua=Image.open(path)
            source_image.paste(imgAgua,marca,imgAgua)
        output = BytesIO()
        source_image.save(output, format=format, optimize=True, quality=90) # Save resize image to bytes
        output.seek(0)
        content_file = ContentFile(output.read())  # Read output and create ContentFile in memory
        file = File(content_file)
        random_name = f'{uuid.uuid4()}.jpeg'
        imageField.save(random_name, file, save=False)





def enviar_email(destinatarios:list,asunto,mensaje_texto):
    datos_email = Envio_Email.objects.last()
    destinatarios.append(datos_email.copia)
    mensaje = MIMEMultipart()
    mensaje['From'] = datos_email.email
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(mensaje_texto, 'plain'))
    sesion_smtp = smtplib.SMTP(datos_email.servidor_smtp, datos_email.puerto)
    sesion_smtp.starttls()
    sesion_smtp.login(datos_email.email, datos_email.password)
    texto = mensaje.as_string()
    sesion_smtp.sendmail(datos_email.email, destinatarios, texto)
    sesion_smtp.quit()