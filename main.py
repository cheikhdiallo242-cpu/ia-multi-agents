import os
from google import genai

client = genai.Client()

def lancer_debat_ia(sujet_initial):
    print(f"--- Sujet de départ : {sujet_initial} ---\n")

    print("🤖 Agent 1 (Le Créateur) réfléchit...")
    prompt_agent_1 = f"Agis en tant que Créateur créatif et innovant. Propose un premier concept détaillé ou un texte court sur le sujet suivant : {sujet_initial}"

    reponse_1 = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_agent_1,
    )
    texte_agent_1 = reponse_1.text
    print(f"\n[Idée du Créateur] :\n{texte_agent_1}\n" + "-"*40)

    print("\n🤖 Agent 2 (Le Critique) analyse...")
    prompt_agent_2 = f"Agis en tant que Critique constructif et exigeant. Analyse le texte suivant produit par le Créateur et propose des améliorations :\n\n{texte_agent_1}"

    reponse_2 = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_agent_2,
    )
    texte_agent_2 = reponse_2.text
    print(f"\n[Critique et suggestions] :\n{texte_agent_2}\n" + "-"*40)

    print("\n🤖 Agent 3 (Le Synthétiseur) finalise...")
    prompt_agent_3 = f"Agis en tant que Synthétiseur expert. Rédige la version finale en combinant l'idée et les critiques :\n\n--- IDÉE ---\n{texte_agent_1}\n\n--- CRITIQUES ---\n{texte_agent_2}"

    reponse_3 = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_agent_3,
    )
    texte_agent_3 = reponse_3.text
    print(f"\n[Version Finale par le Synthétiseur] :\n{texte_agent_3}\n" + "="*40)

if __name__ == "__main__":
    sujet = "Créer une routine matinale pour booster sa productivité et sa sérénité."
    lancer_debat_ia(sujet)
