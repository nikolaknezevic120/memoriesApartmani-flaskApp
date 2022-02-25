# memoriesApartmani-flaskApp

# PROJEKT2-FLASK APLIKACIJA
Za aplikaciju zavrsnog projekta iz kolegija "Programiranje za Web" tema su bili Memories apartmani u Svetom Petru na moru kraj Zadra.
Aplikacija se sastoji od više web stranica 

Na pocetnoj stranici glavne opcije su sign up(kreiraj racun), log in(Prijavi se) i nastavi kao gost(continue as a guest).
Uz navedene opcije nalazi slideshow sa nekoliko slika i tablica sa trenutnim vremenskim prilikama u gradu Zadru.
Ispunjavajuci polja potrebna za kreiranje racuna, korisnik kreira novi korisnicki racun i otvara si mogucnost pristupa aplikaciji preko opcije log in.
Razlika u odabira opcija log in i nastavi kao gost ogleda se u tome da ako se logira, na stranici pise 
hello i username a ako se odabere opcija nastavi kao gost stranice su bez pozrdava.

Na savim stranicama osim pocetne nalazi se i opcija za direktni poziv na sluzbeni broj apartmana.
Takoder se na vecini stranica nalazi i tablica sa trenutnim vremenskim podatcima koji se preuzimaju sa https://openweathermap.org/
U mobilnoj verziji, traka za navigaciju unutar aplikacije se pretvara u padajuci "hamburger" izbornik.

Klikom na polje "Mail" u navigacijskoj traci, otvara se stranica na kojoj se od korisnika trazi unos emaila i subject (naslov email poruke). Ispunjavanjem navedenih polja i klikom na gumb "Zapocni rezervaciju", korisniku automatski stize email poruka sa zahvalom zbog zainteresiranosti i upitom koji ga datumi za rezevaciju zanimaju. Ako je korisnik ulogiran u aplikaciju, iznad polja za unos email-a korisniku kao podsjetnik stoji mail kojeg je naveo prilikom registracije. Nakon klika na gumb "Zapocni rezervaciju", korisniku se otvara nova stranica sa navvigacijskom trakom, slikama apartmana i porukom da je rezervacija zapocela te da provjeri svoju email adresu.

Ukoliko korisnik aplikaciju koristi kao gost u svakom trenutku i sa svake stranice unutar aplikacije moze jednostavno pristupici obrascima za kreiranje racuna i prijavu klikom na gumb "Prijava" na lijevoj strani navigacijske trake, ukoliko je korisnik prijavvljen i zeli se odlogirati, na mjestu opcije gdje se nalazi opcija "Prijava" kada korisnik nije prijavljen nalazi se opcija "Odjava".

## Pokretanje aplikacije
1.Instaliramo virtualno okruženje u CMD ili Poweshell-u ( py -m venv venv ili python -m venv venv)
2.Ulazimo u direktorij Scripts unutar venv foldera kako bi ga aktivirali (venv\Scripts\activate)
3.Instalacija sa requirements (pip install -r requirements.txt)
4.set FLASK_APP=app.py
5.set FLASK_DEBUG=1
6.flask run
7.Otvoriti browser te upisati(http://127.0.0.1:5000/)
