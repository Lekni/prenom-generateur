import streamlit as st
import random

# Listes de prénoms (exemples étendus)
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

# Fonction pour segmenter les prénoms par syllabes (simplifiée)
def segmenter_syllabes(prenom):
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

# Bouton pour générer les prénoms
if st.button("Générer les prénoms"):
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
