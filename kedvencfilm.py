film_cime = input("Add meg egy film címét: ")
film_hossza = int(input("Hány perces a film: "))

ora = film_hossza // 60
perc = film_hossza % 60
print(f"A(z) {film_cime} {ora} óra {perc} perc hosszú.")
