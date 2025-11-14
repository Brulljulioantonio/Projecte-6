# Què fa el programa:
# Autor: Biel Rull Simon

def es_email_valid(email):
    return "@" in email and "." in email

def es_telefon_valid(telefon):
    return telefon.isdigit()