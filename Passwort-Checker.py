def password_abfrage():
    """Prüft, ob das Passwort folgende Kriterien erfüllt:
    - mindestens 10 Zeichen lang
    - beginnt nicht auf einem Buchstaben
    - endet nicht auf einer Zahl
    - enthält Klein- und Großbuchstaben, sowie Zahlen und Sonderzeichen
    """

    try:
        sonderzeichen = list(range(33, 48)) + list(range(58, 65))
        zahlen = list(range(48, 58))
        klein = list(range(97, 123))
        gross = list(range(65, 91))

        my_password = str(input("Password:"))
        length = len(my_password)
        if length <= 10:
            return "Das Passwort muss länger als 10 Zeichen lang sein"
        if ord(my_password[0]) in klein or ord(my_password[0]) in gross:
            return "Das Passwort darf nicht mit einem Buchstaben beginnen"
        if ord(my_password[length - 1]) in zahlen:
            return "Das Passwort darf nicht auf einer Zahl enden"

        klein_drin = False
        gross_drin = False
        zahlen_drin = False
        sonder_drin = False
        for digit in my_password:
            if ord(digit) in klein:
                klein_drin = True
                continue
            elif ord(digit) in gross:
                gross_drin = True
                continue
            elif ord(digit) in zahlen:
                zahlen_drin = True
                continue
            elif ord(digit) in sonderzeichen:
                sonder_drin = True
                continue
            else:
                print(digit, "ist kein gültiges Zeichen")
        if klein_drin and gross_drin and zahlen_drin and sonder_drin:
            return "dies ist eine gültige Eingabe"
        else:
            return "Das Passwort muss Klein- und Großbuchstaben, Zahlen und Sonderzeichen enthalten"
    except ValueError:
        print("Eingabe ungültig")

if __name__ == "__main__":
    print(password_abfrage())