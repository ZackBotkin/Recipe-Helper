import smtplib

class EmailerCreds(object):

    def __init__(self, creds_file):
        f = open(creds_file, 'r')
        self.server = 'smtp.gmail.com'
        self.user_name = f.readline()
        self.password = f.readline()

class Emailer(object):
    def __init__(self, creds):
        self.server = smtplib.SMTP_SSL(creds.server, 465)
        self.server.login(creds.user_name, creds.password)
    def email_ingredients(self, ingredients_to_buy, email_address):
        email_text = ''
        for ingredient in ingredients_to_buy:
            email_text += '%s\n' % ingredient.name
        print('Emailing infgredients to %s' % email_address)
        print('Grocery list...\n\n %s' % email_text)
        self.server.sendmail(email_address, email_address, email_text)
