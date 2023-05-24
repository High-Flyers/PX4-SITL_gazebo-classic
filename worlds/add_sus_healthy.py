import random
from xml.dom import minidom

def replace_tags_with_phrases(file_path):
    # Wczytanie pliku XML
    doc = minidom.parse(file_path)
    
    # Znalezienie wszystkich elementów <uri>
    uris = doc.getElementsByTagName('uri')
    
    # Wygenerowanie 15 unikalnych indeksów dla zamiany na "model://sus"
    sus_indexes = random.sample(range(len(uris)), 15)
    
    # Wygenerowanie 15 unikalnych indeksów dla zamiany na "model://healthy"
    healthy_indexes = random.sample(set(range(len(uris))) - set(sus_indexes), 15)
    
    # Zamiana tagów <uri> na "model://sus" dla odpowiednich indeksów
    for index in sus_indexes:
        uri = uris[index]
        uri.firstChild.nodeValue = 'model://sus'
    
    # Zamiana tagów <uri> na "model://healthy" dla odpowiednich indeksów
    for index in healthy_indexes:
        uri = uris[index]
        uri.firstChild.nodeValue = 'model://healthy'
    
    
    # Zapisanie zmodyfikowanego pliku
    with open(file_path, 'w') as f:
        f.write(doc.toxml())

# Wywołanie funkcji z podaniem ścieżki do pliku XML
replace_tags_with_phrases('baylands_droniada.world')