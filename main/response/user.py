class UserInfo(object):
    first_name: str
    midle_name: str
    last_name: str
    facebook_account: str
    email: str
    normal_account: str
    avatar: str

    def __init__(self, first_name: str,
                 midle_name: str,
                 last_name: str,
                 facebook_account: str,
                 email: str,
                 normal_account: str,
                 avatar: str):
        self.first_name = first_name
        self.midle_name = midle_name
        self.last_name = last_name
        self.facebook_account = facebook_account
        self.email = email
        self.normal_account = normal_account
        self.avatar = avatar
