elso_szo = input("Kérem az első szót: ")
masodik_szo = input("Kérem a második szót: ")

if len(elso_szo) > len(masodik_szo): 
    print("Az első szó hosszabb.")
elif len(elso_szo) < len(masodik_szo):
    print("A második szó hosszabb.")
else:
    print("A két szó egyforma hosszú.")
