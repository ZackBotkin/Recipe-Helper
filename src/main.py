
import smtplib


class EmailerCreds(object):

    def __init__(self, creds_file):
        f = open(creds_file, 'r')
        self.server = 'smtp.gmail.com'
        self.user_name = f.readline()
        self.password = f.readline()

class Recipe(object):
    def __init__(self):
        self.ingredients = ['salt', 'pepper']


class Emailer(object):
    def __init__(self, creds):
        self.server = smtplib.SMTP_SSL(creds.server, 465)
        self.server.login(creds.user_name, creds.password)
    def email_ingredients(self, recipe, email_address):
        email_text = ''
        for ingredient in recipe.ingredients:
            email_text += '%s\n' % ingredient
        print('Emailing infgredients to %s' % email_address)
        self.server.sendmail(email_address, email_address, email_text)

def main():
    creds = EmailerCreds("C:\\Users\\zackb\\emailer_creds\\creds.txt")
    emailer = Emailer(creds)
    recipe = Recipe()
    emailer.email_ingredients(recipe, "zackbotkin@gmail.com")

if __name__ == "__main__":
    main()
