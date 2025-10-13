import string
error = []
password = input()
if len(password)!=8:
    error.append('Длина пароля не равна 8')
if password==password.lower():
    error.append('В пароле отсутствуют заглавные буквы')
if password==password.upper():
    error.append('В пароле отсутствуют строчные буквы')
if not any(symbol.isdigit() for symbol in password):
    error.append('В пароле отсутствуют цифры')
if not any(symbol in '*-#' for symbol in password):
    error.append('В пароле отсутствуют специальные символы')
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
if not all(symbol in allowed for symbol in password):
    error.append('В пароле используются непредусмотренные символы')
if error:
    for error in error:
        print(error)
else:
    print('Надежный пароль')