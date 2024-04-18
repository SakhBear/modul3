def register(login, password):

    with open('register.json', 'a') as f:
        f.write(f"{login, password}\n")

login = input("введите логин: ")
password = input("введите пароль: ")
register(login, password)
print("вы успешно прошли регистрацию.")