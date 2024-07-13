import streamlit as st
import random

# Prénoms en différentes langues (exemple simplifié)
prenoms_fr_masc = ["Alexandre", "Benjamin", "Charles", "David", "Émile"]
prenoms_fr_fem = ["Amandine", "Bérénice", "Charlotte", "Delphine", "Émilie"]
prenoms_de_masc = ["Alexander", "Benjamin", "Carl", "David", "Emil"]
prenoms_de_fem = ["Amanda", "Bettina", "Charlotte", "Doris", "Emma"]
prenoms_en_masc = ["Alexander", "Benjamin", "Charles", "David", "Emil"]
prenoms_en_fem = ["Amanda", "Betty", "Charlotte", "Diana", "Emily"]
prenoms_es_masc = ["Alejandro", "Benjamin", "Carlos", "David", "Emilio"]
prenoms_es_fem = ["Amanda", "Beatriz", "Carlota", "Diana", "Emilia"]
prenoms_is_masc = ["Alexander", "Bjorn", "Carl", "David", "Emil"]
prenoms_is_fem = ["Amanda", "Björk", "Carla", "Dóra", "Elísa"]

# Fonction pour segmenter les prénoms par syllabes (simplifiée)
def segmenter_syllabes(prenom):
    # Exemple très basique pour la segmentation, à améliorer selon besoin
    syllabes = []
    voyelles = "aeiouyAEIOUY"
    syllabe = ""
    for lettre in prenom:
        syllabe += lettre
        if lettre in voyelles:
            syllabes.append(syllabe)
            syllabe = ""
    if syllabe:
        syllabes.append(syllabe)
    return syllabes

# Regroupement des prénoms par langue et genre
prenoms = {
    "Français Masculin": prenoms_fr_masc,
    "Français Féminin": prenoms_fr_fem,
    "Allemand Masculin": prenoms_de_masc,
    "Allemand Féminin": prenoms_de_fem,
    "Anglais Masculin": prenoms_en_masc,
    "Anglais Féminin": prenoms_en_fem,
    "Espagnol Masculin": prenoms_es_masc,
    "Espagnol Féminin": prenoms_es_fem,
    "Islandais Masculin": prenoms_is_masc,
    "Islandais Féminin": prenoms_is_fem,
}

# Interface Streamlit
st.title("Générateur de Prénoms")
langue_genre = st.selectbox("Choisissez la langue et le genre", list(prenoms.keys()))
nb_syllabes = st.slider("Nombre de syllabes", 1, 5, 2)
nb_lettres = st.slider("Nombre de lettres", 3, 10, 6)
nb_prenoms = st.slider("Nombre de prénoms à générer", 5, 50, 10)

# Segmenter les prénoms de la liste choisie
prenoms_segmentes = [segmenter_syllabes(p) for p in prenoms[langue_genre]]

# Générer des prénoms selon les critères
prenoms_generes = []
while len(prenoms_generes) < nb_prenoms:
    prenom = random.choice(prenoms[langue_genre])
    syllabes = segmenter_syllabes(prenom)
    if len(syllabes) == nb_syllabes and len(prenom) == nb_lettres:
        prenoms_generes.append(prenom)

# Afficher les prénoms générés en colonnes de 5
st.subheader("Prénoms générés")
cols = st.columns(5)
for i, prenom in enumerate(prenoms_generes):
    cols[i % 5].write(prenom)
