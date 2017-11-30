import socket

mailserver = ("smtp.gmx.com", 25)

class Smtp:
    def __init__(self):
        self.sock = socket.socket()

    def send(self, mail_from, mail_to, msg):
        msg = 'MAIL FROM: ' + mail_from + '\r\n'
        msg += 'RCPT TO: ' + mail_to + '\r\n'
        msg += 'DATA\r\n' + msg
        self.sock.send(msg.encode())

    def connect(self, server, name='defaultname'):
        self.sock.connect(server)
        self.print_answer()

    def print_answer(self):
        mes = self.sock.recv(1024)
        print(mes)

    def disconnect(self):
        self.sock.close()
        print('Connection has been ended')



class Mail:
    def __init__(self):
        pass

    def concat(self,name, mail_from, subj, data):
        self.mail = 'FROM:' + name + ' <'+ mail_from +'>\r\n'
        self.mail+= 'SUBJECT: ' + subj + '\r\n\r\n'
        self.mail+= data + '\r\n.\r\n'



def main():
    smtp = Smtp()
    mail = Mail()

    print('Hello! SMTP v0.1 is for your service!')

    name = input('input your name:\r\n')
    mail_from = input('input your email:\r\n')
    mail_to = input('input recipient email:\r\n')
    print('Ok, {}, let\'s write a message!'.format(name))
    subj = input('input a subject:\r\n')
    data = ''
    print('write a message and end it with ctrl+z:\r\n')
    while True:
        try:
            data += input()
        except EOFError:
            break
    mail.concat(name, mail_from, subj, data)
    smtp.send(mail_from, mail_to, mail)
    smtp.print_answer()
    smtp.disconnect()




if __name__=='__main__':
    main()