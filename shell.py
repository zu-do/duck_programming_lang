import duck

#infinitive loop - reads input from the terminal windo, kvieciam python shell.py => ir vedam
while True:
    text = input('duck > ')
    result, error = duck.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: print (result)