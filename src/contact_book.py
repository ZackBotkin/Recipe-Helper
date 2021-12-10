
class ContactBook(object):

    def __init__(self, contact_book_file):
        self.email_addresses = {}
        f = open(contact_book_file, 'r')
        row = f.readline()
        while row:
            parts = row.split(',')
            self.email_addresses[parts[0]] = parts[1]
            row = f.readline()

    def lookup_recipient(self, search_term):
        if search_term in self.email_addresses:
            return self.email_addresses[search_term]
        else:
            return search_term

