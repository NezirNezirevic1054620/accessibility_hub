# wp3-2024-starter

Template voor WP3 opdracht "Accessibility Hub". Vul dit document aan zoals beschreven in eisen rondom opleveren (zie ook
de [opdracht](CASUS.md)) 

# ❗❗❗ LEES DE README GOED DOOR ❗❗❗

## Introductie

Voor WP3 moesten wij een applicatie maken waar ervaringsdeskundigen zich in konden registreren en opgeven voor een onderzoek waaraan ze mee konden doen, de onderzoek en de inschrijving wordt uitgevoerd door de beheerder

## Setup met Docker

#### Waarom Docker?

Om het nakijkwerk voor docenten makkelijker te maken hebben we de project verdockerd

#### Requirements

Voor dit setup heb je Docker nodig, de instructies om docker the installeren vind je [hier](https://docs.docker.com/get-docker/).

Als je docker geinstalleerd heb moet je de volgende command runnen in de root van de project:

```bash
docker compose up
```

Als alles goed is, is de applicatie te zien op je http://localhost:8000 of op http://0.0.0.0:8000

Voor het verdockeren hebben we gebruik gemaakt van Docker file en docker compose

Dockerfile:
```Dockerfile
FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /accessibility_hub

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY accessibility_hub .

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

docker-compose:
```Dockerfile
version: '3.9'

services:
  django:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/accessibility_hub .
      - database:/accessibility_hub/database
    ports:
      - "8000:8000"

volumes:
  database:
```

## Setup met VENV

#### Clone de repository
```git
git clone https://github.com/Rac-Software-Development/wp3-2024-rest-1e1-overtime.git
```

#### Maak een Virtual Environment
```python
python -m venv .venv
```


#### Activeer de Virtual Environment


MacOS:

```zsh
source <venv>/bin/activate
```

Windows:

```bash
<venv>\Scripts\activate.bat
```


#### Installeer alle modules
```python
pip install -r requirements.txt
```

#### Run de Django applicatie

```bash
cd accessibility_hub 
```

```python
python manage.py runserver
```

## Login

Admin login:

username: admin
password: admin

Ervaringsdeskundige login:

username: Hxxs164
password: PcBERVNT4mXjFqL

***ALS JE NIET KAN INLOGGEN MAAK EEN ACCOUNT AAN IN http://localhost:8000/admin (je logt in met admin gegevens) daarna druk je op user en je maakt een user aan met een knop die rechtsboven is.

## Zaken met aandacht

Voor dit project hebben we gebruik gemaakt van mailtrap, dit houdt in dat er bevestigingsemails worden gestuurd

![mail1](https://github.com/Rac-Software-Development/wp3-2024-rest-1e1-overtime/blob/main/docs/images/mail4.png?raw=true)
![mail2](https://github.com/Rac-Software-Development/wp3-2024-rest-1e1-overtime/blob/main/docs/images/mail3.png?raw=true)
![mail3](https://github.com/Rac-Software-Development/wp3-2024-rest-1e1-overtime/blob/main/docs/images/mail2.png?raw=true)
![mail4](https://github.com/Rac-Software-Development/wp3-2024-rest-1e1-overtime/blob/main/docs/images/mail1.png?raw=true)

Daarnaast hebben we ook gebruik gemaakt van github actions

```yaml
name: Format code with black

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Format code with black
        run: |
          pip install black
          black --line-length 100 .
      - name: Commit changes
        uses: EndBug/add-and-commit@v4
        with:
          author_name: ${{ github.actor }}
          author_email: ${{ github.actor }}@users.noreply.github.com
          message: "Format code with black"
          add: "."
          branch: ${{ github.ref }}
```


## Documentatie API routes

API documentatie is te vinden op http://127.0.0.1:8000/api_docs/ of in de Postman collection

## ERD

![database_erd](https://github.com/Rac-Software-Development/wp3-2024-rest-1e1-overtime/blob/main/docs/images/database_erd.png?raw=true)

## Postman

```json
{
    "info": {
        "_postman_id": "aabbabe4-6115-40d7-b15c-42d918445f82",
        "name": "AccessibilityHub API",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
        "_exporter_id": "15230291"
    },
    "item": [
        {
            "name": "Ervaringsdeskundige",
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "exec": [
                            "",
                            "pm.test(\"Response status code is 200\", function () {",
                            "  pm.expect(pm.response.code).to.equal(200);",
                            "});",
                            "",
                            "",
                            "pm.test(\"Response has the Content-Type header set to application/json\", function () {",
                            "    pm.expect(pm.response.headers.get(\"Content-Type\")).to.include(\"application/json\");",
                            "});",
                            "",
                            "",
                            "pm.test(\"Email is in a valid format\", function () {",
                            "    const responseData = pm.response.json();",
                            "    ",
                            "    responseData.forEach(function(item) {",
                            "        pm.expect(item.email).to.be.a('string').and.to.match(/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/);",
                            "    });",
                            "});",
                            "",
                            "",
                            "pm.test(\"Toezichthouder field is a boolean value\", function () {",
                            "    const responseData = pm.response.json();",
                            "    ",
                            "    pm.expect(responseData).to.be.an('array');",
                            "    responseData.forEach(function(item) {",
                            "        pm.expect(item.toezichthouder).to.be.a('boolean');",
                            "    });",
                            "});",
                            "",
                            "var template = `",
                            "<style type=\"text/css\">",
                            "    .tftable {font-size:14px;color:#333333;width:100%;border-width: 1px;border-color: #87ceeb;border-collapse: collapse;}",
                            "    .tftable th {font-size:18px;background-color:#87ceeb;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;text-align:left;}",
                            "    .tftable tr {background-color:#ffffff;}",
                            "    .tftable td {font-size:14px;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;}",
                            "    .tftable tr:hover {background-color:#e0ffff;}",
                            "</style>",
                            "",
                            "<table class=\"tftable\" border=\"1\">",
                            "    <tr>",
                            "        <th>ID</th>",
                            "        <th>Voornaam</th>",
                            "        <th>Achternaam</th>",
                            "        <th>Email</th>",
                            "        <th>Postcode</th>",
                            "        <th>Geslacht</th>",
                            "        <th>Tel Nummer</th>",
                            "        <th>Geboortedatum</th>",
                            "        <th>Type Beperking</th>",
                            "        <th>Gebruikte Hulpmiddelen</th>",
                            "        <th>Bijzonderheden</th>",
                            "        <th>Toezichthouder</th>",
                            "        <th>Naam Voogd Toezichthouder</th>",
                            "        <th>Email Voogd Toezichthouder</th>",
                            "        <th>Tel Voogd Toezichthouder</th>",
                            "        <th>Voorkeur Benadering</th>",
                            "        <th>Type Onderzoek</th>",
                            "        <th>Bijzonderheden Beschikbaarheid</th>",
                            "        <th>Status</th>",
                            "    </tr>",
                            "    ",
                            "    {{#each response}}",
                            "        <tr id=row_{{@key}}>",
                            "            <td>{{id}}</td>",
                            "            <td>{{voornaam}}</td>",
                            "            <td>{{achternaam}}</td>",
                            "            <td>{{email}}</td>",
                            "            <td>{{postcode}}</td>",
                            "            <td>{{geslacht}}</td>",
                            "            <td>{{tel_nummer}}</td>",
                            "            <td>{{geboortedatum}}</td>",
                            "            <td>{{type_beperking}}</td>",
                            "            <td>{{gebruikte_hulpmiddelen}}</td>",
                            "            <td>{{bijzonderheden}}</td>",
                            "            <td>{{toezichthouder}}</td>",
                            "            <td>{{naam_voogd_toezichthouder}}</td>",
                            "            <td>{{email_voogd_toezichthouder}}</td>",
                            "            <td>{{tel_voogd_toezichthouder}}</td>",
                            "            <td>{{voorkeur_benadering}}</td>",
                            "            <td>{{type_onderzoek}}</td>",
                            "            <td>{{bijzonderheden_beschikbaarheid}}</td>",
                            "            <td>{{status}}</td>",
                            "        </tr>",
                            "    {{/each}}",
                            "</table>",
                            "`;",
                            "",
                            "function constructVisualizerPayload() {",
                            "    return {response: pm.response.json()}",
                            "}",
                            "",
                            "pm.visualizer.set(template, constructVisualizerPayload());"
                        ],
                        "type": "text/javascript",
                        "packages": {}
                    }
                }
            ],
            "request": {
                "method": "GET",
                "header": [],
                "url": {
                    "raw": "http://localhost:8000/api/experience_experts",
                    "protocol": "http",
                    "host": [
                        "localhost"
                    ],
                    "port": "8000",
                    "path": [
                        "api",
                        "experience_experts"
                    ]
                },
                "description": "This endpoint makes an HTTP GET request to retrieve a list of experience experts. The response will be in JSON format and will contain an array of objects, each representing an experience expert. The objects will include various attributes such as id, voornaam, achternaam, email, postcode, geslacht, tel_nummer, geboortedatum, type_beperking, gebruikte_hulpmiddelen, bijzonderheden, toezichthouder, naam_voogd_toezichthouder, email_voogd_toezichthouder, tel_voogd_toezichthouder, voorkeur_benadering, type_onderzoek, bijzonderheden_beschikbaarheid, and status."
            },
            "response": []
        },
        {
            "name": "Onderzoek aanmaken",
            "request": {
                "method": "POST",
                "header": [],
                "body": {
                    "mode": "raw",
                    "raw": "{\n    \"titel\": \"test\",\n    \"beschikbaar\": 0,\n    \"beschrijving\": \"testonderzoek\",\n    \"datum_vanaf\": \"2024-03-08 08:00:00\",\n    \"datum_tot\": \"2024-03-12 08:00:00\",\n    \"type_onderzoek\": \"online\",\n    \"locatie\": \"Rotterdam\",\n    \"met_beloning\": 1,\n    \"beloning\": \"Prijs\",\n    \"doelgroep_leeftijd_van\": 30,\n    \"doelgroep_leeftijd_tot\": 40,\n    \"doelgroep_beperking\": \"Blind\"\n}",
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": {
                    "raw": "http://localhost:8000/api/create_research/",
                    "protocol": "http",
                    "host": [
                        "localhost"
                    ],
                    "port": "8000",
                    "path": [
                        "api",
                        "create_research",
                        ""
                    ]
                },
                "description": "### Create Research\n\nThis endpoint allows you to create a new research entry.\n\n**HTTP Request**  \n`POST http://localhost:8000/api/create_research/`\n\n**Request Body**\n\n- `titel` (string): The title of the research.\n- `beschikbaar` (number): The availability status of the research.\n- `beschrijving` (string): The description of the research.\n- `datum_vanaf` (string): The start date of the research.\n- `datum_tot` (string): The end date of the research.\n- `type_onderzoek` (string): The type of research.\n- `locatie` (string): The location of the research.\n- `met_beloning` (number): The reward availability status.\n- `beloning` (string): The reward offered for the research.\n- `doelgroep_leeftijd_van` (number): The minimum age of the target audience.\n- `doelgroep_leeftijd_tot` (number): The maximum age of the target audience.\n- `doelgroep_beperking` (string): The restriction or limitation of the target audience.\n    \n\n**Response**\n\n- Status: 201\n- Content-Type: application/json\n- `titel` (string): The title of the research.\n- `beschikbaar` (boolean): The availability status of the research.\n- `beschrijving` (string): The description of the research.\n- `datum_vanaf` (string): The start date of the research.\n- `datum_tot` (string): The end date of the research.\n- `type_onderzoek` (string): The type of research.\n- `locatie` (string): The location of the research.\n- `met_beloning` (boolean): The reward availability status.\n- `beloning` (string): The reward offered for the research.\n- `doelgroep_leeftijd_van` (number): The minimum age of the target audience.\n- `doelgroep_leeftijd_tot` (number): The maximum age of the target audience.\n- `doelgroep_beperking` (string): The restriction or limitation of the target audience."
            },
            "response": []
        },
        {
            "name": "Organisaties",
            "request": {
                "method": "GET",
                "header": [],
                "url": {
                    "raw": "http://localhost:8000/api/organisations/",
                    "protocol": "http",
                    "host": [
                        "localhost"
                    ],
                    "port": "8000",
                    "path": [
                        "api",
                        "organisations",
                        ""
                    ]
                },
                "description": "This API endpoint makes an HTTP GET request to retrieve a list of organisations. The response will be in JSON format and will include an array of objects, each representing an organisation with its respective details such as ID, company name, type, website, description, contact person, email, phone number, and other details."
            },
            "response": []
        }
    ]
}
```

## Azure Board

![azure_board](https://github.com/Rac-Software-Development/wp3-2024-rest-1e1-overtime/blob/main/accessibility_hub/accessibility_hub/static/azure_board.png?raw=true)

## Verslag van standup

Standup 17 maart:
Vandaag hadden we een bespreking om 12 uur net zoals elke week. vandaag was deze op zondag inplaats van zaterdag omdat Airto een verjaardag had op zaterdag. we vroegen eerst of alles gelukt was bij iedereen en bij Ruben en Merissa waren er wat probleempjes. daardoor hebben we gevraagd voor schermdelen om te kijken wat het probleem was. Dit probleem hebben we met ze alle snel en eenvoudig opgelost want merrissa had een klein Javascript probleem en Ruben had een function verkeerd gelinkt aan een URL. Daarna kwam de rondvraag voor de mensen die klaar waren welke opdracht ze wilde gaan oppakken.
Nezir ging verder met:
Als beheerder wil ik door de ervaringsdeskundigen kunnen bladeren met pagination
Airto ging verder met: 
Als beheerder wil ik door ervaringsdeskundige kunnen filteren
Merrissa en Ruben gingen nog verder met hun eigen opdrachten want deze waren nog niet klaar. Verder wisten we allemaal wat we moesten doen en gingen we uit de call en dat was onze standup.

## Bronvermelding

AJAX. (n.d.). MDN Web Docs. https://developer.mozilla.org/en-US/docs/Glossary/AJAX

Christie, T. (n.d.). Django Rest Framework Docs. Home - Django REST framework. https://www.django-rest-framework.org/

Django ORM Tutorial. (n.d.). YouTube. https://www.youtube.com/watch?v=eio1wDUHFJE

Django. (n.d.). Django Project. https://docs.djangoproject.com/en/5.0/

MerakUi Docs. (n.d.). Meraki UI Tailwind CSS Components. https://merakiui.com/

(n.d.). Stack Overflow. https://stackoverflow.com/

Tailwind Docs. (n.d.). Rapidly build modern websites without ever leaving your HTML. https://tailwindcss.com/
