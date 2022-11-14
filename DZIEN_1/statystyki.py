liczby = [900, 1001, -767, 0, 57, 8, 4, -3, 15, 67, 99, 222, -333, 567, 789, 32, 1, -2]


def pokaz_stat(dane):
    minimum = min(dane)
    maksimum = max(dane)
    liczba_el = len(dane)
    rozstep = maksimum - minimum
    sr_arytm = sum(dane) / liczba_el
    return minimum, maksimum, liczba_el, rozstep, sr_arytm


wynik = pokaz_stat(liczby)
print(wynik)
mini, maxi, lb, roz, sa = pokaz_stat(liczby)
print(f"maksimum: {maxi}, miminum: {mini}, rozstęp: {roz}, liczba elementów: {lb}, "
      f"średnia arytmetyczna: {sa:.2f}")


