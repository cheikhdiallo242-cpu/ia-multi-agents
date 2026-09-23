import os
from flask import Flask
from google import genai

app = Flask(__name__)

# Initialisation du client avec la clé d'environnement Render
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/")
def home():
    sujet = "Le rôle de l'intelligence artificielle dans l'éducation de demain."
    
    # 1. Agent 1 : Le Créateur (propose une idée de départ)
    prompt_agent_1 = f"En tant que créateur d'idées, propose une perspective originale et détaillée sur le sujet : '{sujet}'."
    reponse_1 = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt_agent_1,
    )
    
    # 2. Agent 2 : Le Critique (analyse et apporte des axes d'amélioration)
    prompt_agent_2 = f"En tant que critique constructif, analyse la proposition suivante et apporte des contre-points ou des améliorations :\n\n{reponse_1.text}"
    reponse_2 = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt_agent_2,
    )
    
    # 3. Agent 3 : Le Synthétiseur (crée la conclusion finale équilibrée)
    prompt_agent_3 = f"En tant que synthétiseur, combine l'idée originale et la critique pour rédiger une conclusion finale claire, percutante et prête à être appliquée :\n\n- Proposition : {reponse_1.text}\n\n- Critique : {reponse_2.text}"
    reponse_3 = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt_agent_3,
    )
    
    # Mise en forme HTML propre pour le navigateur
    resultat = f"""
    <div style='font-family: sans-serif; padding: 20px; max-width: 800px; margin: auto; line-height: 1.6;'>
        <h1 style='color: #2c3e50;'>Débat Collaboratif à 3 Agents IA</h1>
        <p><strong>Sujet traité :</strong> {sujet}</p>
        <hr style='border: 0; border-top: 1px solid #ccc;'>
        
        <h3 style='color: #2980b9;'>1. Agent Créateur</h3>
        <p>{reponse_1.text.replace(chr(10), '<br>')}</p>
        
        <h3 style='color: #d35400;'>2. Agent Critique</h3>
        <p>{reponse_2.text.replace(chr(10), '<br>')}</p>
        
        <h3 style='color: #27ae60;'>3. Agent Synthétiseur (Conclusion)</h3>
        <p>{reponse_3.text.replace(chr(10), '<br>')}</p>
    </div>
    """
    return resultat

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
