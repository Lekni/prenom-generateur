import tkinter as tk
from tkinter import ttk
import streamlit as st
import random

# Fonction pour segmenter un prénom en syllabes (approximatif)
@@ -21,113 +20,46 @@ def segment_syllables(name):

    return syllables

# Fonction pour changer une syllabe du prénom
def change_syllable():
    name = name_entry.get()
    syllables = segment_syllables(name)

    if len(syllables) < 2:
        result_label.config(text="Le prénom doit avoir au moins deux syllabes.")
        return

    initial_syllable.set(syllables[0])
    if len(syllables) == 2:
        middle_syllable.set("")
        final_syllable.set(syllables[1])
    else:
        middle_syllable.set(syllables[1])
        final_syllable.set(syllables[-1])

    part = part_var.get()

    # Récupérer et segmenter les prénoms de la liste
    raw_names = name_list_text.get("1.0", tk.END).strip().split("\n")
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

    result_label.config(text="Prénoms générés :")
    for i, new_name in enumerate(new_names):
        result_labels[i].config(text=new_name)
# Page principale de l'application
st.title("Générateur de Prénoms")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de Prénoms")
name = st.text_input("Entrez un prénom:")

# Champ de saisie pour le prénom
name_label = ttk.Label(root, text="Entrez un prénom:")
name_label.pack(pady=5)
name_entry = ttk.Entry(root)
name_entry.pack(pady=5)
part = st.selectbox("Changer la syllabe :", ["initiale", "médiane", "finale"])

# Syllabes du prénom
initial_syllable = tk.StringVar()
middle_syllable = tk.StringVar()
final_syllable = tk.StringVar()
name_list_text = st.text_area("Collez votre liste de prénoms (un par ligne) :")

syllable_frame = ttk.Frame(root)
syllable_frame.pack(pady=5)

initial_label = ttk.Label(syllable_frame, text="Initiale:")
initial_label.grid(row=0, column=0, padx=5)
initial_entry = ttk.Entry(syllable_frame, textvariable=initial_syllable, state='readonly')
initial_entry.grid(row=1, column=0, padx=5)

middle_label = ttk.Label(syllable_frame, text="Médiane:")
middle_label.grid(row=0, column=1, padx=5)
middle_entry = ttk.Entry(syllable_frame, textvariable=middle_syllable, state='readonly')
middle_entry.grid(row=1, column=1, padx=5)

final_label = ttk.Label(syllable_frame, text="Finale:")
final_label.grid(row=0, column=2, padx=5)
final_entry = ttk.Entry(syllable_frame, textvariable=final_syllable, state='readonly')
final_entry.grid(row=1, column=2, padx=5)

# Boutons radio pour choisir la partie du prénom à changer
part_var = tk.StringVar(value="initiale")
initial_radio = ttk.Radiobutton(root, text="Initiale", variable=part_var, value="initiale")
initial_radio.pack(pady=5)
middle_radio = ttk.Radiobutton(root, text="Médiane", variable=part_var, value="médiane")
middle_radio.pack(pady=5)
final_radio = ttk.Radiobutton(root, text="Finale", variable=part_var, value="finale")
final_radio.pack(pady=5)

# Champ de saisie pour la liste de prénoms
name_list_label = ttk.Label(root, text="Collez votre liste de prénoms (un par ligne):")
name_list_label.pack(pady=5)
name_list_text = tk.Text(root, height=10, width=50)
name_list_text.pack(pady=5)
if st.button("Générer"):
    syllables = segment_syllables(name)

# Bouton pour générer le nouveau prénom
generate_button = ttk.Button(root, text="Générer", command=change_syllable)
generate_button.pack(pady=10)
    if len(syllables) < 2:
        st.error("Le prénom doit avoir au moins deux syllabes.")
    else:
        initial_syllable = syllables[0]
        middle_syllable = syllables[1] if len(syllables) > 2 else ""
        final_syllable = syllables[-1]

# Label pour afficher le résultat
result_label = ttk.Label(root, text="")
result_label.pack(pady=5)
        raw_names = name_list_text.strip().split("\n")
        name_list = [segment_syllables(n.strip()) for n in raw_names]

# Labels pour afficher les prénoms générés
result_frame = ttk.Frame(root)
result_frame.pack(pady=5)
result_labels = [ttk.Label(result_frame, text="") for _ in range(20)]
for i, label in enumerate(result_labels):
    label.grid(row=i//5, column=i%5, padx=5, pady=2)
        new_names = set()  # Utiliser un set pour éviter les doublons
        while len(new_names) < 20:  # Générer 20 prénoms uniques
            random_name_syllables = random.choice(name_list)
            if len(random_name_syllables) < 2:
                continue

# Lancer la boucle principale de l'interface graphique
root.mainloop()
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
