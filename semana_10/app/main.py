from fastapi import FastAPI
import requests

app = FastAPI()
API_URL = "https://pokeapi.co/api/v2/pokemon/"
MOCK_API_URL = "http://localhost:3000/pokemon/"

@app.get("/")
async def root():
    return {"message": "Utiliza /search/{pokemonNombre} para buscar un pokemon por su nombre"}

@app.get("/search/{pokemon_nombre}")
async def search_pokemon(pokemon_nombre: str):
    try:
        response = requests.get(f"{MOCK_API_URL}{pokemon_nombre.lower()}")
        
        # Test -> vamos a forzar errores
        if pokemon_nombre.lower() == "test_force_500":
            response.status_code = 500

        elif pokemon_nombre.lower() == "test_force_400":
            response.status_code = 400

        if response.status_code == 200:
            pokemon_data = response.json()
            # Solo retornamos los datos más relevantes
            return {
                "status": "success",
                "data": {
                    "nombre": pokemon_data["name"],
                    "altura": pokemon_data["height"],
                    "peso": pokemon_data["weight"],
                    "tipos": [tipo["type"]["name"] for tipo in pokemon_data["types"]]
                }
            }

        elif response.status_code == 400:
            return {
                "status": "error",
                "message": "Error 400: Petición incorrecta"
            }
        elif response.status_code == 500:
            return {
                "status": "error",
                "message": "Error 500: Error en el servidor"
            }
        else:
            return {
                "status": "error",
                "message": f"Pokemon no encontrado (Status: {response.status_code})"
            }

    except requests.RequestException:
        return {
            "status": "error",
            "message": "Error al conectar con la API de Pokemon"
        }
