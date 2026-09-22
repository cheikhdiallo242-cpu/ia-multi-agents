import os
from flask import Flask
from google import genai

app = Flask(__name__)

# Initialisation du client avec la clé d'environnement Render
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def lancer_debat_ia(sujet_initial):
    resultats = []
    resultats.append(f"--- Sujet de départ : {sujet_initial} ---")
    
    # Agent 1 : Le Créateur
    prompt_agent_1 = f"Agis en tant que Créateur, propose une idée originale et inspirante sur le sujet suivant : {sujet_initial}"
    reponse_1 = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt_agent_1,
    )
    texte_agent_1 = reponse_1.text
    resultats.append(f"\n[Idée du Créateur] :\n{texte_agent_1}")
    
    # Agent 2 : Le Critique
    prompt_agent_2 = f"Agis en tant que Critique. Analyse cette idée de manière constructive : {texte_agent_1}"
    reponse_2 = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt_agent_2,
    )
    texte_agent_2 = reponse_2.text
    resultats.append(f"\n[Critique et suggestions] :\n{texte_agent_2}")
    
    # Agent 3 : Le Synthétiseur
    prompt_agent_3 = f"Agis en tant que Synthétiseur. Reprends l'idée du Créateur et les retours du Critique pour créer une version finale parfaite et équilibrée.\n\nIdée initiale :\n{texte_agent_1}\n\nCritique :\n{texte_agent_2}"
    reponse_3 = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt_agent_3,
    )
    texte_agent_3 = reponse_3.text
    resultats.append(f"\n[Version Finale par le Synthétiseur] :\n{texte_agent_3}")
    
    return "\n".join(resultats)

@app.route("/")
def home():
    sujet = "Créer une routine matinale pour booster sa productivité et sa sérénité."
    resultat = lancer_debat_ia(sujet)
    return f"<pre style='font-family: sans-serif; padding: 20px; line-height: 1.5;'>{resultat}</pre>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
