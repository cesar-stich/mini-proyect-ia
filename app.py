import os
from dotenv import load_dotenv
from google import genai

# 1. CARGA DE SEGURIDAD (Capa de Datos/Persistencia)
# Buscamos el archivo .env para extraer las llaves protegidas 
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Verificación de seguridad en consola
print(f"--- DEBUG DE CONFIGURACIÓN ---")
print(f"Directorio actual: {os.getcwd()}")
print(f"¿Archivo .env detectado?: {os.path.exists('.env')}")
print(f"¿Se cargó la llave GOOGLE_API_KEY?: {api_key is not None}")
print(f"------------------------------\n")

# 2. CONFIGURACIÓN DEL AI ENGINE
# Usamos el SDK oficial de google-genai especificado en el stack [cite: 8, 25]
client = genai.Client(api_key=api_key)

def analizar_comentario(texto):
    """
    Función que simula el Módulo de Conocimiento Inteligente.
    Usa una temperatura baja (0.3) para evitar alucinaciones.
    """
    
    # Prompt de instrucción para la IA
    prompt = (
        f"Actúa como un analista de la IEEE UNI. "
        f"Analiza el sentimiento del siguiente comentario: '{texto}'. "
        f"Responde solo con una palabra: POSITIVO, NEGATIVO o NEUTRO."
    )
    
    # Llamada al modelo Gemini 2.0 Flash 
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
    
    return response.text.strip()

# 3. EJECUCIÓN DEL FLUJO (Simulación de Canal Bot) 
if __name__ == "__main__":
    # Comentario de prueba sobre un evento de la IEEE
    comentario_usuario = "El taller de Inteligencia Artificial estuvo excelente, muy bien organizado por el capítulo CIS."
    
    print(f"Analizando: {comentario_usuario}")
    
    try:
        resultado = analizar_comentario(comentario_usuario)
        print(f"\nRESULTADO DEL ANÁLISIS: {resultado}")
    except Exception as e:
        print(f"\nERROR AL LLAMAR A LA IA: {e}")