import streamlit as st
import random
import re

# Listes de prénoms fictives
prenoms_fr_masc = ["Alexandre", "Benjamin", "Charles", "David", "Émile", "François", "Gabriel", "Henri", "Isaac", "Jacques", "Laurent", "Martin", "Nicolas", "Olivier", "Paul", "Quentin", "Romain", "Simon", "Thomas", "Ulysse", "Vincent", "William", "Xavier", "Yves", "Zacharie"]
prenoms_fr_fem = ["Amandine", "Bérénice", "Charlotte", "Delphine", "Émilie", "Florence", "Gabrielle", "Hélène", "Isabelle", "Julie", "Karine", "Laure", "Marie", "Nathalie", "Olivia", "Pauline", "Quitterie", "Rachel", "Sophie", "Thérèse", "Ursule", "Valérie", "Wendy", "Xénia", "Yvette", "Zoé"]
prenoms_de_masc = ["Alexander", "Benjamin", "Carl", "David", "Emil", "Friedrich", "Georg", "Heinrich", "Isaak", "Jakob", "Ludwig", "Martin", "Niklas", "Otto", "Paul", "Quirin", "Rudolf", "Stefan", "Thomas", "Ulrich", "Viktor", "Werner", "Xaver", "Yannick", "Zacharias"]
prenoms_de_fem = ["Amanda", "Bettina", "Charlotte", "Doris", "Emma", "Franziska", "Greta", "Hanna", "Isabel", "Julia", "Katharina", "Luise", "Marie", "Nina", "Olga", "Paula", "Quirin", "Rebecca", "Sophie", "Theresa", "Ulrike", "Verena", "Wiebke", "Xenia", "Yvonne", "Zoe"]
prenoms_en_masc = ["Alexander", "Benjamin", "Charles", "David", "Emil", "Frank", "George", "Henry", "Isaac", "Jack", "Louis", "Martin", "Nicholas", "Oliver", "Paul", "Quentin", "Robert", "Steven", "Thomas", "Ulysses", "Victor", "William", "Xander", "Yves", "Zachary"]
prenoms_en_fem = ["Amanda", "Betty", "Charlotte", "Diana", "Emily", "Fiona", "Grace", "Hannah", "Isabelle", "Jessica", "Katherine", "Laura", "Mary", "Nina", "Olivia", "Patricia", "Quinn", "Rachel", "Sophia", "Tina", "Ursula", "Victoria", "Wendy", "Xena", "Yvonne", "Zara"]
prenoms_es_masc = ["Alejandro", "Benjamin", "Carlos", "David", "Emilio", "Francisco", "Gonzalo", "Hugo", "Ignacio", "Javier", "Luis", "Manuel", "Nicolas", "Oscar", "Pablo", "Quentin", "Rafael", "Sergio", "Tomas", "Ulises", "Vicente", "William", "Xavier", "Yago", "Zacarias"]
prenoms_es_fem = ["Amanda", "Beatriz", "Carlota", "Diana", "Emilia", "Fernanda", "Gabriela", "Helena", "Isabel", "Juana", "Lucia", "Maria", "Nina", "Olga", "Paula", "Quintina", "Raquel", "Sofia", "Teresa", "Ursula", "Valeria", "Wendy", "Ximena", "Yolanda", "Zoe"]
prenoms_is_masc = ["Alexander", "Bjorn", "Carl", "David", "Emil", "Finnur", "Gunnar", "Halldor", "Ingvar", "Jon", "Kristjan", "Leifur", "Magnus", "Njall", "Olafur", "Petur", "Quinn", "Ragnar", "Stefan", "Thor", "Ulfr", "Valdimar", "William", "Xavier", "Ymir", "Zacharias"]
prenoms_is_fem = ["Amanda", "Björk", "Carla", "Dóra", "Elísa", "Freya", "Gudrun", "Hildur", "Ingibjörg", "Jóna", "Katrin", "Lilja", "Margret", "Nína", "Olga", "Pálína", "Quinn", "Rakel", "Sara", "Tinna", "Urður", "Vigdís", "Wendy", "Xena", "Ylfa", "Zoe"]

# Fonction de segmentation syllabique
def segmenter_syllabes(prenom):
    return re.findall(r'[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]))?', prenom, re.IGNORECASE)

# Fonction pour générer des prénoms
def generer_prenom(liste_prenoms, nb_syllabes, nb_lettres):
    syllabes = []
    for prenom in liste_prenoms:
        syllabes.extend(segmenter_syllabes(prenom))
    
    syllabes = list(set(syllabes))
    
    generated_prenoms = []
    while len(generated_prenoms) < 5:
        prenom = ''.join(random.choices(syllabes, k=nb_syllabes))
        if len(prenom) <= nb_lettres:
            generated_prenoms.append(prenom.capitalize())
    
    return generated_prenoms

# Interface Streamlit
st.title("Générateur de Prénoms")

# Sélection de la langue et du genre
langue = st.selectbox("Choisissez une langue", ["Français", "Allemand", "Anglais", "Espagnol", "Islandais"])
genre = st.selectbox("Choisissez un genre", ["Masculin", "Féminin"])

# Sélection du nombre de syllabes et de lettres
nb_syllabes = st.slider("Nombre de syllabes", min_value=1, max_value=5, value=2)
nb_lettres = st.slider("Nombre de lettres", min_value=3, max_value=10, value=6)

# Bouton pour générer des prénoms
if st.button("Générer des prénoms"):
    if langue == "Français":
        liste_prenoms = prenoms_francais_m if genre == "Masculin" else prenoms_francais_f
    elif langue == "Allemand":
        liste_prenoms = prenoms_allemands_m if genre == "Masculin" else prenoms_allemands_f
    elif langue == "Anglais":
        liste_prenoms = prenoms_anglais_m if genre == "Masculin" else prenoms_anglais_f
    elif langue == "Espagnol":
        liste_prenoms = prenoms_espagnols_m if genre == "Masculin" else prenoms_espagnols_f
    elif langue == "Islandais":
        liste_prenoms = prenoms_islandais_m if genre == "Masculin" else prenoms_islandais_f
    
    generated_prenoms = generer_prenom(liste_prenoms, nb_syllabes, nb_lettres)
    
    for i in range(0, len(generated_prenoms), 5):
        cols = st.columns(5)
        for j, col in enumerate(cols):
            if i + j < len(generated_prenoms):
                col.write(generated_prenoms[i + j])
