import streamlit as st
import random
import re

# Listes de prénoms fictives
prenoms = {
    "Français": {
        "Masculin": ["Alexandre", "Benjamin", "Christophe", "David", "Etienne"],
        "Féminin": ["Alice", "Bernadette", "Charlotte", "Diane", "Elise"]
    },
    "Allemand": {
        "Masculin": ["Friedrich", "Heinrich", "Klaus", "Wolfgang", "Hans"],
        "Féminin": ["Greta", "Heidi", "Lotte", "Ursula", "Ingrid"]
    },
    "Anglais": {
        "Masculin": ["John", "William", "James", "Charles", "George"],
        "Féminin": ["Mary", "Elizabeth", "Patricia", "Jennifer", "Linda"]
    },
    "Espagnol": {
        "Masculin": ["Juan", "Carlos", "Pedro", "Luis", "Miguel"],
        "Féminin": ["Maria", "Isabella", "Carmen", "Dolores", "Sofia"]
    },
    "Islandais": {
        "Masculin": ["Bjorn", "Gunnar", "Magnus", "Olafur", "Thor"],
        "Féminin": ["Gudrun", "Ingrid", "Sigrid", "Thorunn", "Vigdis"]
    }
}

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
langue = st.selectbox("Choisissez une langue", list(prenoms.keys()))
genre = st.selectbox("Choisissez un genre", ["Masculin", "Féminin"])

# Sélection du nombre de syllabes et de lettres
nb_syllabes = st.slider("Nombre de syllabes", min_value=1, max_value=5, value=2)
nb_lettres = st.slider("Nombre de lettres", min_value=3, max_value=10, value=6)

# Bouton pour générer des prénoms
if st.button("Générer des prénoms"):
    liste_prenoms = prenoms[langue][genre]
    generated_prenoms = generer_prenom(liste_prenoms, nb_syllabes, nb_lettres)
    
    for i in range(0, len(generated_prenoms), 5):
        cols = st.columns(5)
        for j, col in enumerate(cols):
            if i + j < len(generated_prenoms):
                col.write(generated_prenoms[i + j])
