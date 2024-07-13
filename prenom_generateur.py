import streamlit as st
import random
import json
import os

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

# Fonction pour charger le portfolio à partir d'un fichier JSON
def load_portfolio():
    if os.path.exists("portfolio.json"):
        with open("portfolio.json", "r") as file:
            return json.load(file)
    return {}

# Fonction pour sauvegarder le portfolio dans un fichier JSON
def save_portfolio(portfolio):
    with open("portfolio.json", "w") as file:
        json.dump(portfolio, file, indent=4)

# Charger le portfolio
portfolio = load_portfolio()

# Page principale de l'application
st.title("Générateur de Prénoms")

name = st.text_input("Entrez un prénom:")

name_list_text = st.text_area("Collez votre liste de prénoms (un par ligne) :")

if name:
    syllables = segment_syllables(name)
    probabilities = []

    st.write("Définissez les probabilités de changement pour chaque syllabe:")
    for i, syllable in enumerate(syllables):
        prob = st.slider(f"Probabilité de changement pour la syllabe '{syllable}'", 0.0, 1.0, 0.5)
        probabilities.append(prob)

    if st.button("Générer"):
        if len(syllables) < 2:
            st.error("Le prénom doit avoir au moins deux syllabes.")
        else:
            raw_names = name_list_text.strip().split("\n")
            name_list = [segment_syllables(n.strip()) for n in raw_names]

            new_names = set()  # Utiliser un set pour éviter les doublons
            while len(new_names) < 20:  # Générer 20 prénoms uniques
                random_name_syllables = random.choice(name_list)
                if len(random_name_syllables) < 2:
                    continue

                new_name_syllables = []
                for i, syllable in enumerate(syllables):
                    if random.random() < probabilities[i]:
                        if i == 0:
                            new_syllable = random_name_syllables[0]
                        elif i == len(syllables) - 1:
                            new_syllable = random_name_syllables[-1]
                        else:
                            new_syllable = random.choice(random_name_syllables[1:-1] if len(random_name_syllables) > 2 else random_name_syllables)
                        new_name_syllables.append(new_syllable)
                    else:
                        new_name_syllables.append(syllable)

                new_name = ''.join(new_name_syllables)
                new_names.add(new_name)

            st.write("Prénoms générés :")
            for new_name in new_names:
                col1, col2 = st.columns([3, 1])
                col1.write(new_name)
                if col2.button("✔️", key=new_name):
                    portfolio.setdefault("Default", []).append(new_name)
                    save_portfolio(portfolio)

# Gestion des dossiers
st.sidebar.title("Gestion des dossiers")

# Afficher les dossiers existants
for folder, names in portfolio.items():
    with st.sidebar.expander(folder):
        for name in names:
            col1, col2 = st.columns([3, 1])
            col1.write(name)
            if col2.button("❌", key=f"remove-{folder}-{name}"):
                portfolio[folder].remove(name)
                save_portfolio(portfolio)

        if st.sidebar.button("Supprimer ce dossier", key=f"remove-{folder}"):
            del portfolio[folder]
            save_portfolio(portfolio)

# Ajouter un nouveau dossier
new_folder = st.sidebar.text_input("Nouveau dossier:")
if st.sidebar.button("Créer un dossier"):
    if new_folder and new_folder not in portfolio:
        portfolio[new_folder] = []
        save_portfolio(portfolio)

# Sauvegarder les modifications du portfolio
save_portfolio(portfolio)
