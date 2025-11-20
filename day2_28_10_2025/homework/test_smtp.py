import smtplib

SMTP_SERVER = "poczta.interia.pl"
SMTP_PORT = 465
SMTP_USER = "test_python@interia.pl"
SMTP_PASSWORD = "testpython12345!"

with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    print("Zalogowano!")