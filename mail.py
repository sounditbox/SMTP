import base64
import os


class Mail:

    def __init__(self, boundary, mail_from, mail_to, cc, bcc, subj, mes, text_type, attachments=None):

        self.boundary = boundary #'--boundary42'
        self.email = 'Content-Type: multipart/mixed; '\
                     'boundary="{}"\r\n'\
            .format(self.boundary[2:])
        self.email += 'MIME-Version: 1.0\r\n'
        self.email += 'From: {}\r\n'.format(mail_from)
        self.email += 'Subject: {}\r\n'.format(subj)
        self.email += 'To: {}\r\n'.format(','.join(mail_to)
                              if isinstance(mail_to, list)
                              else mail_to)
        self.email += 'CC: {}\r\n'.format(','.join(cc)
                              if isinstance(cc, list)
                              else cc)
        self.email += 'BCC: {}\r\n'.format(','.join(bcc)
                              if isinstance(bcc, list)
                              else bcc)

        self.email += self.boundary + '\r\n'
        self.email += 'Content-Type: text/{}; charset="us-ascii"\r\n' \
                      'MIME-Version: 1.0\r\n' \
                      'Content-Transfer-Encoding: 7bit\r\n\r\n'.format(text_type)

        self.email += "{}\r\n".format(mes)

        if attachments is not None:
            for file in attachments:
                name = file.rsplit('/', 1)[1]
                attach = self.boundary
                attach += '\r\nContent-Type: application/octet-stream; ' \
                          'Name="{0}"\r\n' \
                          'MIME-Version: 1.0\r\n' \
                          'Content-Transfer-Encoding: base64' \
                          '\r\nContent-Disposition: attachment; ' \
                          'filename="{0}"\r\n\r\n'.format(name)

                with open(name, 'rb') as f:
                    a = f.read()
                    a = base64.b64encode(a)

                    attach += a.decode('ascii')
                    self.email += attach + '\r\n\r\n'

        self.email += self.boundary + "--"

