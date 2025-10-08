# Kom i gang med FastAPI - del 2
Denne guide bygger ovenpå vores tidligere guide om, hvordan du kommer i gang med selv at kode dit eget API med [FastAPI](https://fastapi.tiangolo.com/) til Python.

Har du ikke været den tidligere guide før, så er her et link til den, da det er nødvendigt at følge den først, før du gennemgår denne guide. 

Link til den tidligere guide er: https://github.com/coding-pirates-hillerod/python-fastapi-get-started

## Om denne guide
I denne vil du skulle bygge videre på det meget, meget simple API du tidligere har lavet (via den ovennævnte guide) - dvs. vi vil i denne guide udvide den kode du allerede har skrevet med et eksempel på et API, hvorfra man kan få data om nogle enkelte film.

For at kode dette vil vi derfor følge disse steps:
- Importere en <code>BaseModel</code> fra <code>pydantic</code>
- Slette vores tidligere ene route
- Lave en <code>list</code> med flere film
- Lave en <code>Movie</code> klasse for film
- Lave en route til at hente alle film gemt i vores liste
- Lave en route til at hente en enkelt film per dets id
- Starte en udviklingsserver og se vores API i en browser

Alle disse steps vil én efter én blive gennemgået i nedenstående.

### Step 1: Importere en <code>BaseModel</code> fra <code>pydantic</code>
I den tidligere guide fik vi lavet denne kode til vores meget simple API:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Til denne kode skal vi først og fremmest tilføje endnu en <code>import</code> - denne gang en <code>BaseModel</code> fra et bibliotek som kommer med din installation af FastAPI, der hedder <code>pydantic</code> (tænk i øvrigt ikke så meget over hvad denne import betyder - det kan du sikkert lære mere om, jo mere du sætter dig i Python).

Under din import af <code>fastapi</code> skal du derfor importere dette på følgende måde (det er linje 2 i din kode som er "det nye" her):

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```


### Step 2: Slette vores tidligere ene route
I denne nuværende kode - inkl. den nye import af <code>pydantic</code> - skal vi dog ikke længere bruge den <code>route ("/")</code> vi har, hvorfor denne bare kan slettes.

Koden du skal stå tilbage med for at lave dette nye API med data om film er derfor til en start kun dette:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
```

### Step 3: Lave en <code>list</code> med flere film
For at kunne lave vores API sådan, at man kan hente data om film derfra, så vil vi bruge en Python <code>list</code> (en datastruktur der kan gemme flere data på én gang) til dette.

Skriv derfor under din nuværende kode følgende, hvilket give dig en liste med 3 forskellige film indeholdende data med id, titel, produceren og årstal for release af filmen:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

movies = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "director": "Chris Columbus", "release_year": 2001},
    {"id": 2, "title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "release_year": 2001},
    {"id": 3, "title": "Toy Story", "director": "John Lasseter", "release_year": 1995}
]
```

### Step 4: Lave en <code>Movie</code> klasse for film
Som det næste skal vi lave en Python <code>klasse</code> for en film. Koden til det ser måske nok lidt "mærkelig" ud lige nu, men tænk ikke så meget over det. Lige nu og her laver vi bare noget simpelt, så kan/vil du forhåbentlig med tiden blive bedre i stand til at forstå, hvad koden egentlig gør, når/hvis du sætter dig mere og mere ind i Python.

Under din nuværende kode skal du derfor skrive følgende, således at hele din kode indtil videre er:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

movies = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "director": "Chris Columbus", "release_year": 2001},
    {"id": 2, "title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "release_year": 2001},
    {"id": 3, "title": "Toy Story", "director": "John Lasseter", "release_year": 1995}
]

class Book(BaseModel):
    title: str
    director: str
    release_year: int
```

### Step 5: Lave en route til at hente alle film gemt i vores liste
For at lave en route til vores API, hvor vi kan hente alle de data om de film vi har i vores <code>list</code>, så skal du under din nuværende kode tilføje følgende:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

movies = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "director": "Chris Columbus", "release_year": 2001},
    {"id": 2, "title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "release_year": 2001},
    {"id": 3, "title": "Toy Story", "director": "John Lasseter", "release_year": 1995}
]

class Movies(BaseModel):
    title: str
    director: str
    release_year: int

@app.get("/movies")
def get_movies():
    """Get all movies"""
    return {"movies": movies}
```

Med denne kode vil vi - når vi senere starter den udviklingsserver som kommer med FastAPI - kunne gå til url'en <code>http://127.0.0.1:8000/movies</code> i vores browser og se, at vi med denne url får et svar med al data om de film vi har gemt i vores <code>list</code>.

### Step 6: Lave en route til at hente en enkelt film per dets id
Det sidste vi faktisk kun mangler at kode er en route hvor kan hente data om én film ud fra det id vi har givet hver bog i vores <code>list</code>.

Og dette gøres bare ved at tilføje følgende under al din nuværende kode:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

movies = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "director": "Chris Columbus", "release_year": 2001},
    {"id": 2, "title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "release_year": 2001},
    {"id": 3, "title": "Toy Story", "director": "John Lasseter", "release_year": 1995}
]

class Movies(BaseModel):
    title: str
    director: str
    release_year: int

@app.get("/movies")
def get_movies():
    """Get all movies"""
    return {"movies": movies}

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    """Get a specific movie by ID."""
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return {"error": "Movie not found"}
```

> _Igen ser koden sikkert lidt "mærkelig" ud for dig - og det er også **helt** okay! Men det, som koden vi lige har tilføjet egentlig bare gør, er at løbe den liste af film vi har igennem for at se, om det <code>id</code> du i din browser vil give for at hente data for én film findes. Og hvis dette id findes, ja, så får du data om denne film tilbage. Findes id'et ikke, så får du blot fejlmedelelse <code>{"error": "Movie not found"}</code> (som er den sidste linje kode i det netop tilføjede)_

### Step 7: Starte en udviklingsserver og se vores API i en browser
Med alt dette er vi nu færdige med at kode vores API om film, og vi kan derfor i en terminal starte en udviklingsserver, så vi bagefter kan se vores API - og dets 2 routes - i vores browser.

Kør derfor denne kommando i din terminal for at starte udviklingsserveren:

```bash
fastapi dev main.py
```

Med outputtet i din terminal skulle du gerne blive givet et link til dit API som du kan se i din browser, og du kan derfor gå til følgende 2 url'er:

1. http://127.0.0.1:8000/movies
2. http://127.0.0.1:8000/movies/1

Går du i din browser til <code>http://127.0.0.1:8000/movies</code>, så vil du få data fra dit API om **alle film**.

Går du i stedet til fx <code>http://127.0.0.1:8000/movies/1</code>, så du kun få data om filmen med id'et nummer 1 (_her Harry Potter filmen i vores tilfælde_). Hvis du se data for en anden film - fx filmen med id 2 - så udskift blot url'ens sidste del med filmens id (for filmen med id'et 2 ville url'en vøre <code>http://127.0.0.1:8000/movies/2</code>).

## Bidrag til dette materiale
Dette materiale er lavet med bidrag af:

- [Jonas Bak Phillispn](https://github.com/jbakchr) (_Formand og Kaptajn for Coding Pirates Hillerød_)

## Tak
Meget af idéen - praktisk talt "mega, mega meget" af idéen - til denne guide stammer fra [RealPython](https://realpython.com/) artiklen "[Get Started With FastAPI](https://realpython.com/get-started-with-fastapi/)", hvorfor der skal lyde et kæmpe tak til dem og alt det gode materiale om Python de laver ❤️
