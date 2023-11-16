# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tGNjMFwpwxw7BhESg4INsOgZGgic6lE4

**Task 06: Modifying RDF(s)**
"""

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"

"""Read the RDF file as shown in class"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
Researcher = ns.Researcher
g.add((Researcher, RDF.type, RDFS.Class))
g.add((Researcher, RDFS.label, Literal("Researcher")))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**"""

University = ns.University
g.add((University, RDF.type, RDFS.Class))
g.add((University, RDFS.label, Literal("University")))

for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
g.add((ns.Person, RDF.type, RDFS.Class))
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

janeURI = ns.JaneSmith
g.add((janeURI, RDFS.Class, ns.Researcher))
fullName = Literal("Jane Smith")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
resource = (janeURI, vcard.FN, fullName)
g.add(resource)

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the email address, fullName, given and family names**"""

jane_smith = ns.JaneSmith
g.add((jane_smith, vcard.EMAIL, Literal("jane.smith@example.com")))
g.add((jane_smith, vcard.Given, Literal("Jane")))
g.add((jane_smith, vcard.Family, Literal("Smith")))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

john_smith = ns.JohnSmith
upm = ns.UPM
g.add((upm, RDF.type, ns.University))
g.add((john_smith, vcard.ORG, upm))
g.add((upm, RDFS.label, Literal("Universidad Politécnica de Madrid")))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**Task 6.6: Add that Jown knows Jane using the FOAF vocabulary**"""

from rdflib.namespace import FOAF
john_smith = ns.JohnSmith
jane_smith = ns.JaneSmith
g.namespace_manager.bind('foaf', FOAF, override=False)
g.add((john_smith, FOAF.knows, jane_smith))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

