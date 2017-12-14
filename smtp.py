import base64
import socket
import sys

import time

from mail import Mail

debug_host = 'smtp.gmail.com'  #"alt4.gmail-smtp-in.l.google.com"
debug_port = 587
debug_hostname = '212.193.78.231'


class Smtp:

    def __init__(self, dbg=False, host=None, port=None, login=None, passwd=None):
        self.sock = socket.socket()
        self.sock.settimeout(3)

        self.host = host
        self.port = port

        # self.login = login
        # self.passwd = passwd
        # self.CC = []
        # self.BCC = []
        # self.is_connected = False

        if host and port:
            self.connect(host,port)
        #if login and passwd:
        #    self.auth(login,passwd)

    def connect(self, host, port):
        print('-Connecting...')

        self.sock.connect((host, int(port)))

        resp = self.get_response()
        print(resp)
        if resp[:3] in ['220', '221', '235', '250']:
            print('-Successful connection!')
        else:
            print('-Connection failed')

    def socket_send(self, message):
        message = (message+'\r\n')
        self.sock.send(message.encode())
        return self.get_response()

    def get_response(self):
        attemptCount = 0
        try:
            resp = self.sock.recv(1024).decode()
        except socket.timeout:
            attemptCount+=1
            if attemptCount < 5:
                self.get_response()
            else:
                print('--No answer from server')
                self.disconnect()
                sys.exit()

        return resp

    def ehlo(self, hostname):
        print('-Sending EHLO...')

        self.socket_send('EHLO {}'.format(hostname))

        resp = self.get_response()
        print(resp)
        if resp[:3] in ['220', '221', '235', '250']:
            print('-EHLO Successful!')
        else:
            print('-EHLO failed')

    def start_tls(self):
        if self.debug:
            print('Starting TLS')
        print(self.socket_send('STARTTLS'))

    def auth(self, username, password):
        print('logging in...')
        self.username = username
        base64_str = ("\x00" + username + "\x00" + password).encode()
        base64_str = base64.b64encode(base64_str)
        auth_msg = "AUTH PLAIN ".encode() + base64_str
        print(self.socket_send(auth_msg))

    def disconnect(self):
        self.sock.close()
        print('-Connection has been ended')



def main1():
    print('Hello! SMTP v0.3.5 is for your service!\r\n')

    smtp = Smtp(True,debug_host,debug_port,'sounditbox@gmail.com')
    mail = Mail()

    if not(smtp.host and smtp.port):
        host = input('input a host to use: ')
        port = input('input a port to use: ')
        smtp.connect(host, port)

    hostname = input('input your hostname: ')

    smtp.ehlo(hostname)

    smtp.start_tls()

    if not(smtp.login and smtp.passwd):
        smtp.login = input('login: ')
        smtp.passwd = input('passwd: ')
    smtp.auth(smtp.login, smtp.passwd)

    mail_from, mail_to = mail.write_mail(hostname)
    print(smtp.socket_send('MAIL FROM:<{}>'.format(mail_from)))

    print(smtp.socket_send('RCPT TO: <{}>'.format(mail_to)))

    print(smtp.sock.send('DATA'.encode()))

    smtp.sock.send(mail.mail.encode())
    print(smtp.get_response())


    smtp.disconnect()


def main():
    smtp = Smtp(True, debug_host, debug_port, debug_hostname)
    while 1:
        try:
            print('Server: ' + smtp.socket_send(input('You: ')))
        except socket.timeout:
            print('TIMEOUT')
            continue
        except IOError:
            smtp.disconnect()




if __name__=='__main__':
    main1()