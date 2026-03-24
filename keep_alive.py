import os
import requests

# Vos infos Supabase
URL = "https://rcjuiazcuwywnunnhcog.supabase.co/rest/v1/"
# On utilise les secrets GitHub pour la sécurité
KEY = os.getenv("SUPABASE_KEY")

def ping_supabase():
    headers = {
        "apikey": KEY,
        "Authorization": f"Bearer {KEY}"
    }
    # On demande juste la liste des tables (requête légère)
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        print("Succès : Le projet Jlidi-Engine-2026 est réveillé !")
    else:
        print(f"Erreur : {response.status_code}")

if __name__ == "__main__":
    ping_supabase()
