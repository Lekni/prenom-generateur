import streamlit as st
import random
import re

# Fonction pour segmenter un prénom en syllabes
def syllabify(name):
    syllables = re.findall(r'[^aeiou]*[aeiou]+(?:[^aeiou]*$|[^aeiou](?=[^aeiou]))?', name, re.IGNORECASE)
    return syllables

# Fonction pour générer des prénoms à partir des syllabes
def generate_names(syllables, num_syllables, num_names):
    generated_names = []
    for _ in range(num_names):
        name = ''.join(random.choices(syllables, k=num_syllables))
        generated_names.append(name.capitalize())
    return generated_names

# Interface utilisateur avec Streamlit
st.title("Générateur de Prénoms à partir de Syllabes")

# Champ pour coller une liste de prénoms
input_names = st.text_area("Collez une liste de prénoms (un par ligne):")

# Sélection du nombre de syllabes par prénom
num_syllables = st.slider("Nombre de syllabes par prénom:", min_value=1, max_value=5, value=3)

# Bouton pour générer les prénoms
if st.button("Générer des prénoms"):
    if input_names:
        # Traitement des prénoms collés
        names_list = input_names.split('\n')
        all_syllables = []
        for name in names_list:
            all_syllables.extend(syllabify(name.strip().lower()))
        
        # Générer les prénoms
        generated_names = generate_names(all_syllables, num_syllables, 20)
        
        # Afficher les prénoms générés
        st.write("Prénoms générés:")
        for generated_name in generated_names:
            st.write(generated_name)
    else:
        st.warning("Veuillez coller une liste de prénoms.")
