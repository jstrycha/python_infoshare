# Algorytm
################################################
# 1. importuje biblioteki
# 2. przygotowuję maila z tematem treścią i odbiorcą
# 3. tworze obiekt mailera
#   a. witam się z serwerem smtp – tworzę połączenie
#   b. loguję się (podając login i hasło)
#   c. wysyłam maila
# kończę połączenie z serwerem
################################################
# login: pythonintel@int.pl
# hasło: isapython;2025
# smtp: poczta.int.pl
# port: 465
# zabezpieczenie: SSL


# 1. importuje biblioteki
import smtplib
from email.mime.text import MIMEText

# dane logowania i dane serwera
login = "pythonintel@int.pl"
haslo = "isapython;2025"
smtp_server = "poczta.int.pl"
port = 465 #zabezpieczenie: SSL

# 2. przygotowuję maila z tematem treścią i odbiorcą
mail = MIMEText('Testowy mail')
mail['Subject'] = 'Test'
mail['To'] = 'pythonintel@int.pl'
mail['From'] = 'pythonintel@int.pl'

# 3. tworze obiekt mailera
#   a. witam się z serwerem smtp – tworzę połączenie
with smtplib.SMTP_SSL(smtp_server, port) as server: ## kończę połączenie z serwerem - dzięki with
    #   b. loguję się (podając login i hasło)
    server.login(login, haslo)
    #   c. wysyłam maila
    server.send_message(mail)
    server.sendmail(mail['From'],mail['To'],mail.as_string())

print("Mail wysłany!")


#####################################################################################################
# wersja Bartka
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# def send_email(smtp_server: str= "poczta.int.pl", smtp_port: int=465, login: str= "pythonintel@int.pl",
#                pwd:str= "isapython;2025", recipient:str= "pythonintel@int.pl"):
#
#     # przygotowuję maila z tematem treścią i odbiorcą
#     msg = MIMEMultipart()
#     msg["From"] = login
#     msg["To"] = recipient
#     msg["Subject"] = "Python SMTP"
#
#     body = "Jeśli to czytasz, to znaczy, że mój program działa!"
#     msg.attach(MIMEText(body, "plain"))
#
#     print(msg.as_string())
#
#     # tworze obiekt mailera
#     # witam się z serwerem smtp – tworzę połączenie
#     server = smtplib.SMTP_SSL(smtp_server, smtp_port)
#     try:
#         # loguję się (podając login i hasło)
#         server.login(login, pwd)
#         # wysyłam maila
#         server.send_message(msg)
#         # kończę połączenie z serwerem
#         server.quit()
#         print(f"Wysłano wiadomość do {msg["To"]}")
#     except Exception as e:
#         print(e)