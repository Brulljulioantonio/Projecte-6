# Què fa el programa:
# Autor: Biel Rull Simon

import validacions

print(validacions.es_email_valid("usuari@example.com"))
print(validacions.es_email_valid("malcorreu"))

print(validacions.es_telefon_valid("123456789"))
print(validacions.es_telefon_valid("abc123"))