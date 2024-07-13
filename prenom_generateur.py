import streamlit as st
import random

# Fonction pour segmenter un prénom en syllabes (approximatif)
def segment_syllables(name):
    vowels = "aeiouyAEIOUY"
    syllables = []
    syllable = ""

    for i, char in enumerate(name):
        syllable += char
        if char in vowels:
            if i + 1 < len(name) and name[i + 1] in vowels:
                continue
            syllables.append(syllable)
            syllable = ""

    if syllable:
        syllables.append(syllable)
    
    return syllables

# Page principale de l'application
st.title("Générateur de Prénoms")

name = st.text_input("Entrez un prénom:")

part = st.selectbox("Changer la syllabe :", ["initiale", "médiane", "finale"])

name_list_text = st.text_area("Collez votre liste de prénoms (un par ligne) :")

if st.button("Générer"):
    syllables = segment_syllables(name)

    if len(syllables) < 2:
        st.error("Le prénom doit avoir au moins deux syllabes.")
    else:
        initial_syllable = syllables[0]
        middle_syllable = syllables[1] if len(syllables) > 2 else ""
        final_syllable = syllables[-1]

        raw_names = name_list_text.strip().split("\n")
        name_list = [segment_syllables(n.strip()) for n in raw_names]

        new_names = set()  # Utiliser un set pour éviter les doublons
        while len(new_names) < 20:  # Générer 20 prénoms uniques
            random_name_syllables = random.choice(name_list)
            if len(random_name_syllables) < 2:
                continue

            if part == "initiale":
                new_initial = random_name_syllables[0]
                new_name = new_initial + ''.join(syllables[1:])
            elif part == "médiane" and len(syllables) > 2:
                new_middle = random.choice(random_name_syllables[1:-1] if len(random_name_syllables) > 2 else random_name_syllables)
                new_name = syllables[0] + new_middle + syllables[-1]
            elif part == "finale":
                new_final = random_name_syllables[-1]
                new_name = ''.join(syllables[:-1]) + new_final

            new_names.add(new_name)

        st.write("Prénoms générés :")
        for name in new_names:
            st.write(name)
