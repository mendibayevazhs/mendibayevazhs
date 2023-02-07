# Write your code here :-)
def check_passwd(username,password):
    if type(username) != str or type(password) != str:
        raise ValueError("You need to write only strings")
    if len(password) < 8:
        print("Password is so short, please create something difficult")
        return False
    elif username.lower() in password.lower():
        print("Username contains in password, it is not secure")
        return False
    else:
        print(f"Password for {username} has been created")
        return True


def check_user_list(user_password_data):
    correct_users = []
    wrong_users = []
    for user, password in user_password_data:
        print(user, password)
        try:
            check = check_passwd(user, password)
        except ValueError as error:
            print(error)
        else:
            if check:
                correct_users.append(user)
            else:
                wrong_users.append(user)
    return correct_users, wrong_users

def main():
    data = [
        ["user1", "jhdxhjgjdhgj"],
        ["user2", "jdh"],
        ["user3", "gkdjgfguser3"],
        [10,20]
    ]
    ok, not_ok = check_user_list(data)
    print(ok)
    print(not_ok)


main()
