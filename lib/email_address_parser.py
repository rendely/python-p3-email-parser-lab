import re 

class EmailAddressParser():

    email_match_pattern = r"[A-z]+[A-z|0-9|.]+\@[A-z|0-9|.]+"
    email_regex = re.compile(email_match_pattern)

    def __init__(self, emails_string):
        self.emails_string = emails_string

    def parse(self):
        email_list = EmailAddressParser.email_regex.findall(self.emails_string)
        return sorted(email_list)