
class Mail:
    def concat(self,name, mail_from, subj, data):
        self.mail = 'FROM: {} <{}>\r\n'.format(name, mail_from)
        self.mail+= 'SUBJECT: {}\r\n\r\n'.format(subj)
        self.mail+= '{}\r\n.\r\n'.format(data)

    def write_mail(self, name):
        mail_from = input('input your email: ')
        mail_to = input('input recipient email: ')

        #print('Ok, {}, let\'s write a message!'.format(name))
        subj = input('input a subject: ')
        data = ''
        print('input data')#'write a message and end it with ctrl+d:')
        while True:
            try:
                data += input() + '\r\n'
            except EOFError:
                break
        self.concat(name, mail_from, subj, data)
        return mail_from, mail_to
