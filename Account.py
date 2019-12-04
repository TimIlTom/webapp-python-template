class Account:

    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

accounts = []

github = Account("GitHub", "TimIlTom", "password")
moodle = Account("Moodle", "to.lupu", "password1")

accounts.append(github)
accounts.append(moodle)

assert github.password == "password"

