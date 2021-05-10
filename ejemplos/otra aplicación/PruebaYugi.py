from rdflib import Graph,Literal,URIRef
from rdflib import Namespace
from rdflib.namespace import RDF, RDFS

#Ingresando las URIs de las instancias de la clase maestra: Objeto
guerreroCelta=URIRef("https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=4047")
guerreroCastor=URIRef("https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=4033")

n = Namespace("https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=1&pid=1202002000&rp=99999")

#Insertando las URIs de la clase: Características
nombre = URIRef('characteristic:nombre')
atributo = URIRef('characteristic:atributo')
nivel = URIRef('characteristic:nivel')
ataque = URIRef('characteristic:ataque')
defensa = URIRef('characteristic:defensa')

g = Graph()

#categorias generales, existen cartas tipo criatura, magica y trampa
g.add((n.criatura, RDFS.subClassOf, n.carta))
g.add((n.magica, RDFS.subClassOf, n.carta))
g.add((n.trampa, RDFS.subClassOf, n.carta))

#subcategorias, las cartas criatura pueden ser tipo guerrero,guerrero bestia..., tambien efecto o normal
g.add((n.efecto, RDFS.subClassOf, n.criatura))
g.add((n.normal, RDFS.subClassOf, n.criatura))
g.add((n.guerrero, RDFS.subClassOf, n.criatura))
g.add((n.guerreroBestia, RDFS.subClassOf, n.criatura))

#agregar triples a guerrero Celta
g.add((guerreroCelta, RDF.type, n.criatura))
g.add((guerreroCelta, RDF.type, n.guerrero))
g.add((guerreroCelta, RDF.type, n.normal))
g.add((guerreroCelta, nombre, Literal('guerrero Celta')))
g.add((guerreroCelta, ataque, Literal('1400')))
g.add((guerreroCelta, defensa, Literal('1200')))
g.add((guerreroCelta, atributo, Literal('Tierra')))
g.add((guerreroCelta, nivel, Literal('4')))

#agregar triples a guerrero Castor
g.add((guerreroCelta, RDF.type, n.criatura))
g.add((guerreroCelta, RDF.type, n.guerreroBestia))
g.add((guerreroCelta, RDF.type, n.normal))
g.add((guerreroCelta, nombre, Literal('guerrero Castor')))
g.add((guerreroCelta, ataque, Literal('1200')))
g.add((guerreroCelta, defensa, Literal('1500')))
g.add((guerreroCelta, atributo, Literal('Tierra')))
g.add((guerreroCelta, nivel, Literal('4')))

#Ingresando las SubPropiedades de la clase: Características y sucesoras
g.add((nombre, RDFS.subPropertyOf, n.characteristic))
g.add((atributo, RDFS.subPropertyOf, n.characteristic))
g.add((nivel, RDFS.subPropertyOf, n.characteristic))
g.add((ataque, RDFS.subPropertyOf, n.characteristic))
g.add((defensa, RDFS.subPropertyOf, n.characteristic))

#Definicion Labels
g.add((nombre, RDFS.subPropertyOf, RDFS.label))
g.add((atributo, RDFS.subPropertyOf, RDFS.label))
g.add((nivel, RDFS.subPropertyOf, RDFS.label))
g.add((ataque, RDFS.subPropertyOf, RDFS.label))
g.add((defensa, RDFS.subPropertyOf, RDFS.label))


#Ingresando los nombres literales de las propiedades y sub-propiedades
g.add((n.carta, nombre, Literal('Carta')))
g.add((n.magica, nombre, Literal('Magica')))
g.add((n.trampa, nombre, Literal('Trampa')))
g.add((n.efecto, nombre, Literal('Efecto')))
g.add((n.normal, nombre, Literal('Normal')))
g.add((n.criatura, nombre, Literal('Criatura')))
g.add((n.guerrero, nombre, Literal('Guerrero')))
g.add((n.guerreroBestia, nombre, Literal('Guerrero Bestia')))

print("Predicado:")
for index,(sub,pred,obj) in enumerate(g):
    print(pred)
    if index==10:
        break

#Encontrar las dependencias (subclases) para la subclase guerrero
print("Subclases de la subclase guerrero:")
for s in g.transitive_objects(n.guerrero, RDFS.subClassOf):
    print(g.value(s, nombre))

def isSubClassOf(subClass, superClass, graph):
    if subClass == superClass: return True
    for parentClass in graph.objects(subClass, RDFS.subClassOf):
        if isSubClassOf(parentClass, superClass, graph): return True
        else:return False

va=isSubClassOf(n.normal, n.criatura, g)
print("Valor: ",va)

#Encontrar los tipos asociados a la instancia guerrero Celta
print("Instancias asociadas a guerrero Celta:")
for s in g.transitive_objects(guerreroCelta, RDF.type):
    print(g.value(s, nombre))

#Dependencias inferiores a criatura
print("Dependencias inferiores a criatura:")
for s in g.transitive_subjects (RDFS.subClassOf,n.criatura):
    print(g.value(s, nombre))

#Nombres de las criaturas
print("Nombres de las criaturas:")
for criatura in g.subjects(RDF.type,n.criatura):
    for nick in g.objects(criatura,nombre):
        print(nick)


# for s,p,o in g:
#     print(s,p,o)
