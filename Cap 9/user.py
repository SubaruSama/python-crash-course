class User:

    def __init__(self, first_name: str, last_name: str, nickname: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.email = email
        self.login_attempts = 0

    def describe_user(self) -> None:
        print(f'First Name: {self.first_name}\nLast Name: {self.last_name}\nNickname: {self.nickname}\nEmail: {self.email}')

    def greet_user(self) -> None:
        print(f'Hello {self.nickname}!')

    def increment_login_attempts(self) -> None:
        self.login_attempts += 1

    def flush_login_attempts(self) -> None:
        self.login_attempts = 0

    def get_quantity_login_attempts(self) -> int:
        return self.login_attempts