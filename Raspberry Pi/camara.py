from picamera2 import Picamera2
from email.message import EmailMessage
import smtplib
from io import BytesIO
from time import sleep

picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)

#Set the sender email and password and recipient emaiç
from_email_addr ="isaacfelipe2007@gmail.com"
from_email_pass ="ygjj xljc prhw dmgp"
to_email_addr = ["isaacmn24@estudiantec.cr", "6183@'estudiantec.cr", "pablop@estudiantec.cr"]
#to_email_addr ="isaacmn24@estudiantec.cr"

def tomar_foto():
    picam2.start()
    
    sleep(2)  # Tiempo para que la cámara se caliente
    
    image_stream = BytesIO()
    picam2.capture_file(image_stream, format='png')
    
    #picam2.capture_file("foo.jpg")
    picam2.stop()
    
    return image_stream

def enviar_correo(imagen):
    msg = EmailMessage()
    
    # Set email body
    body = "Adjunto primera imagen de una bandera costarricense en el espacio exterior."
    msg.set_content(body)
    
    # Set sender and recipient
    msg['From'] = from_email_addr
    msg['To'] = ', '.join(to_email_addr)  # Aquí se agregan múltiples destinatarios
    #msg['To'] = to_email_addr
    
    # Set your email subject
    msg['Subject'] = 'Imagen Lunar'
    
    # Adjuntar la imagen desde el buffer en memoria
    imagen.seek(0)  # Asegurarse de que el puntero del buffer esté al inicio
    msg.add_attachment(imagen.read(), maintype='image', subtype='png', filename="bandera.png")
    
    # Connecting to server and sending email
    # Edit the following line with your provider's SMTP server details
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    # Comment out the next line if your email provider doesn't use TLS
    server.starttls()
    # Login to the SMTP server
    server.login(from_email_addr, from_email_pass)
    
    # Send the message
    server.send_message(msg)
    
    print('Email sent')
    
    #Disconnect from the Server
    server.quit()

