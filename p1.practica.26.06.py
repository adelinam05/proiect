
import re

def validare_nume(nume):
   if re.match(r'^[a-zA-Z\-\s]+$',nume) and not re.match(r'^[+\\@!?/]+$',nume):
       return True
   else:
       return False

def validare_cnp(cnp):
    if re.match(r'^[\d]+$',cnp) and len(cnp)==13 and not re.match(r'^[+\\@!?/]+$',cnp):
        c_coef = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
        suma = sum(int(cnp[i]) * c_coef[i] for i in range(12))
        control_digit = suma % 11
        if control_digit == 10:
            control_digit = 1
        if control_digit  == int(cnp[12]):
            return True
    else:
        return False

def input_date_client():
    nume_client = input("Introduceti numele clientului: ")
    if nume_client.lower() == 'stop':
        return None
    while not validare_nume(nume_client):
        print("Numele clientului invalid.")
        nume_client = input("Reintroduceti numele clientului: ")
        if nume_client.lower() == 'stop':
            return None

    prenume_client = input("Introduceti prenumele clientului: ")
    if prenume_client.lower() == 'stop':
        return None
    while not validare_nume(prenume_client):
        print("Prenumele clientului invalid.")
        prenume_client = input("Reintroduceti prenumele clientului: ")
        if prenume_client.lower() == 'stop':
            return None

    if ' ' in prenume_client.strip() or '-' in prenume_client.strip():
        prenume1, prenume2 = re.split(r'\s|-', prenume_client, 1)
    else:
        prenume1 = prenume_client
        prenume2 = ''

    cnp = input("Introduceti CNP-ul clientului: ")
    if cnp.lower() == 'stop':
        return None
    while not validare_cnp(cnp):
        print("CNP-ul clientului invalid.")
        cnp = input("Reintroduceti CNP-ul clientului: ")
        if cnp.lower() == 'stop':
            return None

    return {
        "nume": nume_client,
        "prenume": prenume1,
        "prenume2": prenume2,
        "cnp": cnp
    }
cursanti = []

while True:
    cursant = input_date_client()
    if cursant is None:
        break
    cursanti.append(cursant)
    print(cursant)

print("Procesul de introducere a datelor a fost încheiat.")
while True:
    comanda = input("Introduceti comanda (salveaza / stop): ")
    if comanda.lower() == 'stop':
        break
    elif comanda.lower() == 'salveaza':
        with open("cursanti.txt", "w") as file:
            for cursant in cursanti:
                file.write(f"Nume: {cursant['nume']}, Prenume1: {cursant['prenume']}, Prenume2: {cursant['prenume2']}, CNP: {cursant['cnp']}\n")
        print("Datele au fost salvate în fișier.")

print("Procesul de introducere a datelor a fost încheiat.")