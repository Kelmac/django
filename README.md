
Portal FotoWorld
Projekt zaliczeniowy na studia na przedmiot "Systemy Zarządzania Treścią"
Projekt serwisu internetowego do dzielenia się zdjęciami .
Projekt napisany w Django 1.8 i Python 3.6

Konta użytkowników
Superuser:
  USER:  admin
  PASSOWRD: admindjango
  
  Superuser - administrator SZT ma dostęp do panelu administratorskiego (może dodawać news'y)
Bloger:
  USER: bloger
  PASSWORD: django
  
  Bloger - użytkownik bez dostępu do panelu administracyjnego, po zalogowaniu może publikowac zdjęcia wraz z opisem
  


Aplikacje Django: 

News:
	Aplikacja do wyświetlania listy postów i ich szczegółów po naciśnięciu na przycisk na stronie. Posty dodaje się przez panel Administratorski
Account:
	Aplikacja odpowiadająca za autoryzacje i logowanie użytkowników do strony. Zarządzanie użytkownikami (dodawanie,usuwanie) odbywa się przez panel administratorski
Images
	Aplikacja do zarządzania plikami graficznymi. Każdy zalogowany na stronie użytkownik może dodawać zdjęcia za pomocą przygotowanego odpowiednio formularza przez wklejeniu linku do tego zdjęcia. Aplikacja sama pobiera zdjęcia z podanego linku i zapisuję na serwerze. Aplikacja także wyświetla wszystkie zdjęcia w serwisie.


