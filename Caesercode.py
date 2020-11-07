# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:12:12 2019

@author: Andrea
"""
posa = ord('a')#ord wandelt einen Buchstaben in eine Zahl um
posz = ord('z')

def caesar(wort, verschiebung):
    wortneu = ""#um die Variable vor zu deffinieren
    wortlaenge= len(wort)
    for x in range(wortlaenge):#zum iterieren für alle elemente des Wortes
        pos = ord(wort[x].lower())#die Position der Buchstaben des Wortes konvertiert in Kleinbuchstaben
        if posa <= pos <= posz:#um nur Buchstaben von a bis z umzuwandeln und den rest nicht
            wortneu += chr( ((pos-posa) - int(verschiebung)) % (posz-posa+1) + posa )
            """Der Variable wortneu werden die einzelnen Buchstaben,
            die um die verschiebung erhöht oder erniedricht wurden zugewiesen.
            Dazu wird der Zahl (Position im Alphabet) die für den Buchstaben in der Eingabe für wort steht
            die als Ganzzahl deffinierte verschiebung abgezogen.
            Anschließend wird die erhaltene Zahl mit dem Befehl chr in einen Buchstaben rückumgewandelt. 
            Um zu erreichen, dass nach z wieder a folgt wird der modolo verwendet. 
            Dazu wird die nach der verschiebung erhaltene Position immer 
            durch die Position von z im Alphabet dividiert und der Rest ausgegeben
            #Ist die Position klieiner als z wird die gleiche position als Rest 
            zurückgegeben ist sie größer entspricht der Rest dem um wie viel 
            sie größer ist und zählt somit von z wieder richtung a.
            Diesem Rest wird dann für die Rückumwandlung die Position von a addiert."""
        else:
            wortneu += wort[x] 
            #falls ein anderes Zeichen als a-z vorkommt wird dieses unumgewandelt im neuen Wort ausgegeben
    return wortneu



    
    

