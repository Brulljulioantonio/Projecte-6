from CompteUsuari import CompteUsuari

u = CompteUsuari("usuari@example.com")
print(u.email)

u.email = "nou.email@domini.com"
print(u.email)

u.email = "emailincorrecte"
