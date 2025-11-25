# interactive_list_demo.py
# Interaktywny przykład operacji na listach w Pythonie
# Dodano przykłady operacji jak slicing: lista[2:], lista[:3], lista[1:4] itd.

"""

https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

"""


def show_menu():
    print("""
Wybierz operację:
1. Dodaj element (append)
2. Dodaj wiele elementów (extend)
3. Wstaw element na pozycję (insert)
4. Usuń element (remove)
5. Usuń element z pozycji (pop)
6. Pokaż listę
7. Posortuj listę
8. Odwróć listę
9. Policz wystąpienia elementu
10. Pokaż przykłady operacji slice
11. Zakończ
""")

def show_slicing_examples(lista):
    print("""
PRZYKŁADY SLICINGU W PYTHONIE:
lista[2:]    -> elementy od indeksu 2 dalej
lista[:3]    -> pierwsze trzy elementy
lista[1:4]   -> elementy od indeksu 1 do 3
lista[::2]   -> co drugi element
lista[::-1]  -> lista odwrócona (alternatywa dla reverse)
""")
    print("Twoja lista:", lista)
    print("lista[2:]:", lista[2:])
    print("lista[:3]:", lista[:3])
    print("lista[1:4]:", lista[1:4])
    print("lista[::2]:", lista[::2])
    print("lista[::-1]:", lista[::-1])

def main():
    lista = []

    while True:
        show_menu()
        choice = input("Twój wybór: ")

        if choice == "1":
            val = input("Podaj element: ")
            lista.append(val)

        elif choice == "2":
            vals = input("Podaj elementy oddzielone spacjami: ").split()
            lista.extend(vals)

        elif choice == "3":
            pos = int(input("Pozycja: "))
            val = input("Element: ")
            lista.insert(pos, val)

        elif choice == "4":
            val = input("Element do usunięcia: ")
            try:
                lista.remove(val)
            except ValueError:
                print("Nie ma takiego elementu.")

        elif choice == "5":
            pos = int(input("Pozycja: "))
            try:
                removed = lista.pop(pos)
                print("Usunięto:", removed)
            except IndexError:
                print("Błędna pozycja.")

        elif choice == "6":
            print("Aktualna lista:", lista)

        elif choice == "7":
            try:
                lista.sort()
                print("Posortowano.")
            except Exception:
                print("Nie można sortować elementów o różnych typach.")

        elif choice == "8":
            lista.reverse()
            print("Odwrócono listę.")

        elif choice == "9":
            val = input("Element: ")
            print("Liczba wystąpień:", lista.count(val))

        elif choice == "10":
            show_slicing_examples(lista)

        elif choice == "11":
            print("Koniec.")
            break

        else:
            print("Nieznana opcja.")

if __name__ == "__main__":
    main()
