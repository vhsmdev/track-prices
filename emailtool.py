import smtplib
import email.message


def send_email():
    email_content = """
    https://www.brasiltronic.com.br/camera-digital-fujifilm-gfx-50r-medio-formato-somente-corpo
    """
    msg = email.message.Message()
    msg['Subject'] = "Câmera FUJIFILM GFX 50R Médio Formato (Somente Corpo)!!!!"

    msg['From'] = 'teste@startz.space'
    msg['To'] = 'vmoreira021@gmail.com'

    password = "teste324*$#"

    msg.add_header("Content-Type", "text/html")
    msg.set_payload(email_content)

    s = smtplib.SMTP("mail.startz.space", 465)
    s.starttls()
    s.login(msg["From"], password)

    s.sendmail(msg["From"], [msg["To"]], msg.as_string())

    print("Sucesso ao enviar email!")

send_email()
