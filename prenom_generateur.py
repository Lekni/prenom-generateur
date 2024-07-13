import streamlit as st
import random
import re

def syllable_segment(name):
    # Simple syllable segmentation using regex
    pattern = re.compile(r'[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]|$))?', re.IGNORECASE)
    return pattern.findall(name)

def generate_names(syllables, num_names, num_syllables, num_letters):
    generated_names = []
    while len(generated_names) < num_names:
        name = ''
        while len(name) < num_letters:
            name += random.choice(syllables)
            if len(name) >= num_letters or len(name) >= num_syllables * 2:
                break
        if len(name) <= num_letters:
            generated_names.append(name.capitalize())
    return generated_names

# Prénoms exemples par origine (en réalité, vous voudrez peut-être utiliser des listes plus complètes)
name_data = {
    'Française': ['Alice', 'Charlotte', 'Émilie', 'Julien', 'Laurent'],
    'Anglaise': ['Oliver', 'Amelia', 'Harry', 'Jessica', 'George'],
    'Allemande': ['Hans', 'Greta', 'Fritz', 'Heidi', 'Klaus']
}

# Streamlit UI
st.title('Générateur de Prénoms à partir de Syllabes')

# Input for list of names
name_list_input = st.text_area('Collez une liste de prénoms (séparés par des nouvelles lignes):')
name_list = name_list_input.split('\n')

# Select origin
selected_origin = st.selectbox('Sélectionnez l\'origine des prénoms:', list(name_data.keys()))

# Parameters for generated names
num_syllables = st.number_input('Nombre de syllabes par prénom', min_value=1, value=2)
num_letters = st.number_input('Nombre de lettres par prénom', min_value=1, value=6)
num_names = 20

# Process the names to extract syllables
syllables = []
# Add syllables from the selected origin
for name in name_data[selected_origin]:
    syllables.extend(syllable_segment(name.strip().lower()))
# Add syllables from the user input
for name in name_list:
    syllables.extend(syllable_segment(name.strip().lower()))

# Generate new names
if st.button('Générer des prénoms'):
    new_names = generate_names(syllables, num_names, num_syllables, num_letters)
    
    # Display the generated names in columns of 5
    for i in range(0, len(new_names), 5):
        cols = st.columns(5)
        for col, name in zip(cols, new_names[i:i+5]):
            col.write(name)
