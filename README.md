# Work projects involving data science
--------------------------------------
Work related project involving large data analysis


### 1.NLP on staff bottom-up ideas within an internal contribution campaign

### 2.Air France Organization analysis in the frame of an organization redesign

First let's import the data which include every agent Name, Id, Line of Work, his level (executive, technician etc.), his status (ground, flight crew, local staff in foreign countries etc.), his service and so on

```
LOAD CSV WITH HEADERS FROM "file:///ETUDENIVHIERARCHIQUENEO4J.csv" AS csvLine CREATE (person:Person {Matricule: csvLine.Matricule, Nom: csvLine.Nom, Macro_activite: csvLine.Macro_activite, Activite: csvLine.Activite, Niveau_emploi: csvLine.Niveau_emploi, Categorie_salariale: csvLine.Categorie_salariale, Sigle_Service: csvLine.Sigle_Service, Libelle_Service: csvLine.Libelle_Service, Nom_N1: csvLine.Nom_N1})
```

I have used py2neo librairy to build queries with Python instead of pure Cypher to be able to run complex queries faster. Hereunder is a snippet of the code I've used to create managerial relationship

```python
from py2neo import authenticate, Graph, Path, Relationship
authenticate("localhost:7474","neo4j","")
graph=Grahp()
cursor=graph.find('Person')
for record in cursor :
 try:
  team=record
  manager=graph.find_one('Person','Nom',team["Nom_N1"])
  print manager["Nom"],"est le manager de", team["Nom"]
  graph.create(Relationship(manager, "MANAGER_OF", team))
 except TypeError :
  continue
 ```
The result can be seen in the following graph :
![alt text](/topgraph.png)

```
$MATCH (n) WHERE n.Nom_N1="GAGEY FREDERIC" RETURN n
$MATCH (Person),(CEO {Nom:"GAGEY FREDERIC"}) WHERE (Person)<--(CEO) RETURN Person

MATCH (Person),(CEO {Nom:"GAGEY FREDERIC"}) WHERE (Person)<-[:MANAGER_OF*0..2]-(CEO) RETURN Person
```

### 3.Ops Data science project?
