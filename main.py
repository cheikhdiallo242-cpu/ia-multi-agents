import os
from google import genai

# Initialisation du client avec la clé d'environnement
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def lancer_debat_ia(sujet_initial):
    print(f"--- Sujet de départ : {sujet_initial} ---")
    
    # Agent 1 : Le Créateur
    print("🤖 Agent 1 (Le Créateur) réfléchit...")
    prompt_agent_1 = f"Agis en tant que Créateur, propose une idée originale et inspirante sur le sujet suivant : {sujet_initial}"
    reponse_1 = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_agent_1,
    )
    texte_agent_1 = reponse_1.text
    print(f"\n[Idée du Créateur] :\n{texte_agent_1}")
    
    # Agent 2 : Le Critique
    print("\n🤖 Agent 2 (Le Critique) analyse...")
    prompt_agent_2 = f"Agis en tant que Critique. Analyse cette idée de manière constructive : {texte_agent_1}"
    reponse_2 = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_agent_2,
    )
    texte_agent_2 = reponse_2.text
    print(f"\n[Critique et suggestions] :\n{texte_agent_2}")
    
    # Agent 3 : Le Synthétiseur
    print("\n🤖 Agent 3 (Le Synthétiseur) finalise...")
    prompt_agent_3 = f"Agis en tant que Synthétiseur. Reprends l'idée du Créateur et les retours du Critique pour créer une version finale parfaite et équilibrée.\n\nIdée initiale :\n{texte_agent_1}\n\nCritique :\n{texte_agent_2}"
    reponse_3 = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_agent_3,
    )
    texte_agent_3 = reponse_3.text
    print(f"\n[Version Finale par le Synthétiseur] :\n{texte_agent_3}")

if __name__ == "__main__":
    sujet = "Créer une routine matinale pour booster sa productivité et sa sérénité."
    lancer_debat_ia(sujet)
