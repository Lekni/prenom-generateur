import streamlit as st
import random
import re

# Listes de prénoms fictives
prenoms = {
    "Français": {
        "Masculin": ["Alexandre", "Benjamin", "Charles", "David", "Émile", "François", "Gabriel", "Henri", "Isaac", "Jacques", "Laurent", "Martin", "Nicolas", "Olivier", "Paul", "Quentin", "Romain", "Simon", "Thomas", "Ulysse", "Vincent", "William", "Xavier", "Yves", "Zacharie"]
,
        "Féminin": ["Amandine", "Bérénice", "Charlotte", "Delphine", "Émilie", "Florence", "Gabrielle", "Hélène", "Isabelle", "Julie", "Karine", "Laure", "Marie", "Nathalie", "Olivia", "Pauline", "Quitterie", "Rachel", "Sophie", "Thérèse", "Ursule", "Valérie", "Wendy", "Xénia", "Yvette", "Zoé"]
    },
    "Allemand": {
        "Masculin": ["Alexander", "Benjamin", "Carl", "David", "Emil", "Friedrich", "Georg", "Heinrich", "Isaak", "Jakob", "Ludwig", "Martin", "Niklas", "Otto", "Paul", "Quirin", "Rudolf", "Stefan", "Thomas", "Ulrich", "Viktor", "Werner", "Xaver", "Yannick", "Zacharias"],
        "Féminin": ["Amanda", "Bettina", "Charlotte", "Doris", "Emma", "Franziska", "Greta", "Hanna", "Isabel", "Julia", "Katharina", "Luise", "Marie", "Nina", "Olga", "Paula", "Quirin", "Rebecca", "Sophie", "Theresa", "Ulrike", "Verena", "Wiebke", "Xenia", "Yvonne", "Zoe"]
    },
    "Anglais": {
        "Masculin": ["Alexander", "Benjamin", "Charles", "David", "Emil", "Frank", "George", "Henry", "Isaac", "Jack", "Louis", "Martin", "Nicholas", "Oliver", "Paul", "Quentin", "Robert", "Steven", "Thomas", "Ulysses", "Victor", "William", "Xander", "Yves", "Zachary"],
        "Féminin": ["Amanda", "Betty", "Charlotte", "Diana", "Emily", "Fiona", "Grace", "Hannah", "Isabelle", "Jessica", "Katherine", "Laura", "Mary", "Nina", "Olivia", "Patricia", "Quinn", "Rachel", "Sophia", "Tina", "Ursula", "Victoria", "Wendy", "Xena", "Yvonne", "Zara"]
    },
    "Espagnol": {
        "Masculin": ["Alejandro", "Benjamin", "Carlos", "David", "Emilio", "Francisco", "Gonzalo", "Hugo", "Ignacio", "Javier", "Luis", "Manuel", "Nicolas", "Oscar", "Pablo", "Quentin", "Rafael", "Sergio", "Tomas", "Ulises", "Vicente", "William", "Xavier", "Yago", "Zacarias"],
        "Féminin":  ["Amanda", "Beatriz", "Carlota", "Diana", "Emilia", "Fernanda", "Gabriela", "Helena", "Isabel", "Juana", "Lucia", "Maria", "Nina", "Olga", "Paula", "Quintina", "Raquel", "Sofia", "Teresa", "Ursula", "Valeria", "Wendy", "Ximena", "Yolanda", "Zoe"]
    },
    "Islandais": {
        "Masculin": ["Alexander", "Bjorn", "Carl", "David", "Emil", "Finnur", "Gunnar", "Halldor", "Ingvar", "Jon", "Kristjan", "Leifur", "Magnus", "Njall", "Olafur", "Petur", "Quinn", "Ragnar", "Stefan", "Thor", "Ulfr", "Valdimar", "William", "Xavier", "Ymir", "Zacharias"],
        "Féminin": ["Amanda", "Björk", "Carla", "Dóra", "Elísa", "Freya", "Gudrun", "Hildur", "Ingibjörg", "Jóna", "Katrin", "Lilja", "Margret", "Nína", "Olga", "Pálína", "Quinn", "Rakel", "Sara", "Tinna", "Urður", "Vigdís", "Wendy", "Xena", "Ylfa", "Zoe"]
    }
}

# Fonction de segmentation syllabique
def segmenter_syllabes(prenom):
    return re.findall(r'[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]))?', prenom, re.IGNORECASE)

# Fonction pour générer des prénoms par permutation des syllabes
def generer_prenom_par_permutation(liste_prenoms, nb_syllabes, nb_lettres):
    generated_prenoms = []
    
    while len(generated_prenoms) < 5:
        prenom_base = random.choice(liste_prenoms)
        syllabes = segmenter_syllabes(prenom_base)
        
        if len(syllabes) >= nb_syllabes:
            random.shuffle(syllabes)
            prenom = ''.join(syllabes[:nb_syllabes])
            if len(prenom) <= nb_lettres:
                generated_prenoms.append(prenom.capitalize())
    
    return generated_prenoms

# Interface Streamlit
st.title("Générateur de Prénoms")

# Sélection de la langue et du genre
langue = st.selectbox("Choisissez une langue", list(prenoms.keys()))
genre = st.selectbox("Choisissez un genre", ["Masculin", "Féminin"])

# Sélection du nombre de syllabes et de lettres
nb_syllabes = st.slider("Nombre de syllabes", min_value=1, max_value=5, value=2)
nb_lettres = st.slider("Nombre de lettres", min_value=3, max_value=10, value=6)

# Bouton pour générer des prénoms
if st.button("Générer des prénoms"):
    liste_prenoms = prenoms[langue][genre]
    generated_prenoms = generer_prenom_par_permutation(liste_prenoms, nb_syllabes, nb_lettres)
    
    for i in range(0, len(generated_prenoms), 5):
        cols = st.columns(5)
        for j, col in enumerate(cols):
            if i + j < len(generated_prenoms):
                col.write(generated_prenoms[i + j])
