class Account:

    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

accounts = []

github = Account("GitHub", "TimIlTom", "password")
moodle = Account("Moodle", "to.lupu", "password1")
gmail = Account("Gmail", "ittomalupu@gmail.com", "password2")

accounts.append(github)
accounts.append(moodle)
accounts.append(gmail)

assert github.password == "password"

