import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(sender_email, receiver_email, password):
    port = 465
    smtp_server = "smtp.viettel.com.vn"
    sender_email = sender_email
    receiver_email = receiver_email
    password = password
    # password = input("Password: ")

    msg = MIMEMultipart()
    msg['Subject'] = "Mời mua homewifi"
    msg['From'] = sender_email
    body = """
    <html>
        <body>
            <p>Hi, tên tôi là <b>Cường</b></p>
            <p>Hãy mua homewifi ngay</p>
            <img src="http://127.0.0.1:5000/pixel.gif" width="1" height="1">
        </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        for i in range(len(receiver_email)):
            del msg['to']
            msg['To'] = receiver_email[i]
            server.send_message(msg, sender_email, receiver_email[i])