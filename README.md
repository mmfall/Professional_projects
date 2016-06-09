# Work projects involving data science
--------------------------------------
Work related project involving large data analysis

### 1.Air France Organization analysis in the frame of an organization redesign

Micro-management and silos have been identified as obstacle against efficiency within organizations. Too many managers with too little responsility create control burden and rigidities. The aim of this project is to analyse Air France Group organization and identify opportunities to reduce the number of managers by increasing average span of control and mutualize teams when it makes sense.

First let's import the data which include every agent Name, Id, Line of Work, his level (executive, technician etc.), his status (ground, flight crew, local staff in foreign countries etc.), his service and so on

```
LOAD CSV WITH HEADERS FROM "file:///ETUDENIVHIERARCHIQUENEO4J.csv" AS csvLine CREATE (person:Person {Matricule: csvLine.Matricule, Nom: csvLine.Nom, Macro_activite: csvLine.Macro_activite, Activite: csvLine.Activite, Niveau_emploi: csvLine.Niveau_emploi, Categorie_salariale: csvLine.Categorie_salariale, Sigle_Service: csvLine.Sigle_Service, Libelle_Service: csvLine.Libelle_Service, Matricule_N1: csvLine.Matricule_N1, Nom_N1: csvLine.Nom_N1})
```

I have used py2neo librairy to build queries with Python instead of pure Cypher to be able to run complex queries faster. Hereunder is a snippet of the code I've used to create managerial relationship

```python
from py2neo import authenticate, Graph, Path, Relationship
authenticate("localhost:7474","neo4j","")
graph=Graph()
cursor=graph.find('Person')
for record in cursor :
 try:
  team=record
  manager=graph.find_one('Person','Matricule',team["Matricule_N1"])
  print manager["Nom"],"est le manager de", team["Nom"]
  graph.create(Relationship(manager, "MANAGER_OF", team))
 except TypeError :
  continue
 ```
The result can be seen in the following graph :
![alt text](/topgraph.png)

```
# Rechercher le CEO
$MATCH (n) WHERE n.Nom_N1="GAGEY FREDERIC" RETURN n
# Rechercher les agents directement reliés à CEO
$MATCH (Person),(CEO {Nom:"GAGEY FREDERIC"}) WHERE (Person)<--(CEO) RETURN Person
# Rechercher les agents et liens reliés de 1 à 2 niveaux au CEO (renvoi tout, le CEO compris avec *)
MATCH (Person),(CEO {Nom:"GAGEY FREDERIC"}) WHERE (Person)<-[:MANAGER_OF*0..2]-(CEO) RETURN *
# Anomalies : Ruptures de chaîne hierarchiques
MATCH (Person),(CEO {Nom:"BEGOUGNE DE JUNIAC ALEXANDRE"}) WHERE NOT (Person)<-[:MANAGER_OF*0..10]-(CEO) RETURN Person.Nom
# Nombre de personnes reliées directement au CEO
MATCH (Person),(CEO {Nom:"GAGEY FREDERIC"}) WHERE (Person)<-[:MANAGER_OF]-(CEO) RETURN count(*)
# Nombre de personnes reliées avec 6 intermédiaires au CEO n'étant pas Personnel Navigant
MATCH (CEO {Nom:"GAGEY FREDERIC"})-[r:MANAGER_OF*6..6]->(Team) WHERE NOT (Team.Macro_activite="PN") RETURN COUNT(Team)
# Nombre de personnes reliées avec 1 intermédiaire au CEO
MATCH (Person),(CEO {Nom:"GAGEY FREDERIC"}) WHERE (Person)<-[:MANAGER_OF*2..2]-(CEO) RETURN count(*)
# Nombre de managers rattachés avec X intermediaire au CEO
MATCH (Person),(CEO {Nom:"GAGEY FREDERIC"}) WHERE (Person)<-[:MANAGER_OF*1..1]-(CEO) AND (Person)-->() RETURN count(*)
# Nombre de managers rattachés avec X intermediaires au CEO n'étant pas Personnel Navigant
MATCH (Person),(CEO {Nom:"GAGEY FREDERIC"}) WHERE (Person)<-[:MANAGER_OF*2..2]-(CEO) AND (Person)-->() AND NOT (Person.Macro_activite="PN") RETURN count(*)
# Managers avec le plus grand et plus petit nombre de rattachements, directement rattachés au CEO
MATCH (CEO {Nom:"GAGEY FREDERIC"})-[:MANAGER_OF*1..1]->(Person)-[r:MANAGER_OF]->(Team) RETURN Person, COUNT(r) as rel_count ORDER BY rel_count DESC
# Nombre de personnes appartenant aux fonctions support rattachées au CEO
MATCH (CEO {Nom:"GAGEY FREDERIC"})-[r:MANAGER_OF*2..2]->(Team) WHERE (Team.Macro_activite="ACHATS")OR(Team.Macro_activite="AMO")OR(Team.Macro_activite="AUTRES SUPPORTS TRANSVERSES")OR(Team.Macro_activite="COMMUNICATION")OR(Team.Macro_activite="DIGITAL")OR(Team.Macro_activite="FORMATION")OR(Team.Macro_activite="GESTION ET FINANCES")OR(Team.Macro_activite="MEDICAL / SOCIAL")OR(Team.Macro_activite="PAIE & ADMIN. DU PERSONNEL")OR(Team.Macro_activite="RESSOURCES HUMAINES")OR(Team.Macro_activite="SMI")OR(Team.Macro_activite="SUPPORT METIER") RETURN COUNT(Team)
#  Managers opérationnels avec le plus grand et plus petit nombre de rattachements, directement rattachés au CEO
MATCH (CEO {Nom:"GAGEY FREDERIC"})-[:MANAGER_OF*2..2]->(Team)-[r:MANAGER_OF]->(Person) WHERE NOT ( (Team.Macro_activite="ACHATS")OR(Team.Macro_activite="AMO")OR(Team.Macro_activite="AUTRES SUPPORTS TRANSVERSES")OR(Team.Macro_activite="COMMUNICATION")OR(Team.Macro_activite="DIGITAL")OR(Team.Macro_activite="FORMATION")OR(Team.Macro_activite="GESTION ET FINANCES")OR(Team.Macro_activite="MEDICAL / SOCIAL")OR(Team.Macro_activite="PAIE & ADMIN. DU PERSONNEL")OR(Team.Macro_activite="RESSOURCES HUMAINES")OR(Team.Macro_activite="SMI")OR(Team.Macro_activite="SUPPORT METIER")) RETURN Team, COUNT(r) as rel_count ORDER BY rel_count DESC
# Organisation RH du Cargo
MATCH (CCO {Nom:"MALKA ALAIN"})-[r:MANAGER_OF*0..10]->(Person {Macro_activite:"RESSOURCES HUMAINES"})-->(Team) RETURN *
```
### 2.NLP on staff bottom-up ideas within an internal contribution campaign

### 3.Modeling Large Organization complexity using a Model-Based Design approach (w Scilab software)

### 4.Bot answering flight safety related comments on company social network
Air France and KLM share a company social network. It has been launched in 2014 and at the date of June 2016 the social network counts more than 30 000 members from both companies. More than a hundred discussions groups have been created by employees and a few ones by the corporate communication services. in June 16 very few of these groups talk about Flight Safety and related issues. This project consists of creating a chatbot using python aiml and yampy libraries to answer flight safety related questions. The objectives was mainly communication purposes to create a buzz on the topic but also to give valuable information within the company on where to report concerns and events related to flight safety. The bot is named R2D2 in relation with the robot in the Star Wars movie sagas (R2D2 is Luke Skywalker copilot during flight combats).    
![alt text](/afr2d2post.png)

### 5.Ops Data science project?

### 6.Improve corporate communication by clustering analysis

### 7.Process mining using event logs
