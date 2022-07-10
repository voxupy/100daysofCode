year = int(input("Podaj rok: "))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} przestępny.")
elif year % 400 == 0 and year % 100 == 0:
    print(f"{year} przestepny.")
else:
    print(f"{year} rok nieprzestepny.")
