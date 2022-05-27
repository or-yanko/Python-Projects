import basic

def analize_line():
    text = input('basic > ')
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)


while True:
    analize_line()
