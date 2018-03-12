import base64
import smtplib
import socket as s
import ssl
from time import sleep

import mail

class Smtp:
    def __init__(self,
                 ip, port,
                 username, password,
                 boundary, mail_from, mail_to,
                 cc, bcc, subj, mes,
                 text_type,
                  attachments=None):
        self.sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.sock.settimeout(5)
        self.ip = ip
        self.port = int(port)
        self.username = username
        self.password = password
        self.mail_from = mail_from
        self.mail_to = mail_to
        self.email = mail.Mail(boundary, mail_from,
            mail_to, cc, bcc, subj, mes, text_type, attachments)

    def connect(self):
        self.sock = ssl.wrap_socket(
             self.sock,ssl_version=ssl.PROTOCOL_SSLv23)
        self.sock.connect((self.ip, self.port))
        self.get_answer()

    def ehlo(self):
        self.sock.send('EHLO Neo\r\n'.encode())
        self.get_answer()

    def start_tls(self):
        self.sock.send('STARTTLS\r\n'.encode())
        self.get_answer()

    def auth(self):
        str = base64.b64encode(("\x00" + self.username + "\x00" + self.password).encode())
        auth = "AUTH PLAIN ".encode() + str + "\r\n".encode()
        self.sock.send(auth)
        self.get_answer()

    def mail(self):
        self.sock.sendall("MAIL FROM:<{}>\r\n".format(self.username).encode())
        self.get_answer()

        self.sock.sendall("RCPT TO:<{}>\r\n".format(self.mail_to).encode())
        self.get_answer()

        self.sock.sendall("DATA\r\n".encode())
        self.sock.sendall(self.email.email.encode())
        self.get_answer()

        self.sock.sendall('\r\n.\r\n'.encode())
        self.get_answer()


    def disconnect(self):
        self.sock.sendall('QUIT'.encode())
        self.sock.close()


    def get_answer(self):
        print(self.sock.recv().decode())

    def send_mail(self):
        self.connect()
        self.ehlo()
        self.auth()
        self.auth()
        self.mail()
        self.disconnect()

if __name__ == '__main__':
    smtplib
    smtp = Smtp('smtp.gmail.com', 465,
                'python.smtp.test.mail@gmail.com','pythonpython',
                '--boundary42',
                'python.smtp.test.mail@gmail.com',
                'python.smtp.test.mail1@gmail.com',
                None,
                None,
                'Subj',
                'Hi\r\nIts a test message',
                'plain')#, 'html_example.txt')
    smtp.send_mail()
    print('Done!')
