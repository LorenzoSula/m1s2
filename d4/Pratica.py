fine = False

while not fine:
    fine = True
    figura = input("Inserisci la figura di cui calcolare il perimetro: ")

    match figura.lower():
        case "cerchio":
            r = input("Inserisci il raggio del cerchio: ")
            cir = 2 * 3.14 * float(r)
            print("Circonferenza = ", cir)
        case "quadrato":
            l = input("Inserisci la misura del lato della figura: ")
            l *= 4
            print("Perimetro = ", l)
        case "rettangolo":
            b = input("Inserisci la misura della base della figura: ")
            h = input("Inserisci la misura dell'altezza della figura: ")
            perimetro = b * 2 + h * 2
            print("Perimetro = ", perimetro)
        case _:
            print("Figura non riconosciuta. Le opzioni conosciute sono:\n" \
            "- Quadrato\n" \
            "- Cerchio\n" \
            "- Rettangolo")
            fine = False