import os
from google import genai
from google.genai import types

# Initialisation du client GenAI (la clé API doit être définie dans tes variables d'environnement)
client = genai.Client()

def lancer_debat_ia(sujet_initial):
    print(f"--- Sujet de départ : {sujet_initial} ---\n")

    # --- AGENT 1 : Le Créateur ---
    print("🤖 Agent 1 (Le Créateur) réfléchit...")
    prompt_agent_1 = f"Agis en tant que Créateur créatif et innovant. Propose un premier concept détaillé ou un texte court sur le sujet suivant : {sujet_initial}"
    
    reponse_1 = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_agent_1,
    )
    texte_agent_1 = reponse_1.text
    print(f"\n[Idée du Créateur] :\n{texte_agent_1}\n" + "-"*40)

    # --- AGENT 2 : Le Critique ---
    print("\n🤖 Agent 2 (Le Critique) analyse...")
    prompt_agent_2 = f"""Agis en tant que Critique constructif et exigeant. 
    Analyse le texte suivant produit par le Créateur et propose des améliorations, des failles à corriger ou des axes d'optimisation :
    
    {texte_agent_1}"""
    
    reponse_2 = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_agent_2,
    )
    texte_agent_2 = reponse_2.text
    print(f"\n[Critique et suggestions] :\n{texte_agent_2}\n" + "-"*40)

    # --- AGENT 3 : Le Synthétiseur ---
    print("\n🤖 Agent 3 (Le Synthétiseur) finalise...")
    prompt_agent_3 = f"""Agis en tant que Synthétiseur expert. 
    Prends en compte l'idée originale du Créateur et les retours du Critique pour rédiger la version finale et parfaite du texte :
    
    --- IDÉE ORIGINALE ---
    {texte_agent_1}
    
    --- CRITIQUES ---
    {texte_agent_2}"""
    
    reponse_3 = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_agent_3,
    )
    texte_agent_3 = reponse_3.text
    print(f"\n[Version Finale par le Synthétiseur] :\n{texte_agent_3}\n" + "="*40)

if __name__ == "__main__":
    # Test du script avec un sujet de ton choix
    sujet = "Créer une routine matinale pour booster sa productivité et sa sérénité."
    lancer_debat_ia(sujet)
