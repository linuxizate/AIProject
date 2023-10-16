# 1. Cargar la bbdd con langchain
from langchain.utilities import SQLDatabase
db_uri = "sqlite://///Users/javier/OpenAI-projects/AIProject/ecommerce.db"
db = SQLDatabase.from_uri(db_uri)

# 2. Importar las APIs
import a_env_vars
import os
os.environ["OPENAI_API_KEY"] = a_env_vars.OPENAI_API_KEY

# 3. Crear el LLM
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

# 4. Crear la cadena
from langchain_experimental.sql import SQLDatabaseChain
cadena = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# 5. Formato personalizado de respuesta
formato = """
Dada una pregunta del usuario:
1. crea una consulta de sqlite3
2. revisa los resultados
3. devuelve el dato
4. si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español
#{question}
"""

# 6. Función para hacer la consulta
def consulta(input_usuario):
    consulta = formato.format(question=input_usuario)
    resultado = cadena.run(consulta)
    return resultado

#cadena.run("cuantas columnas hay en la base de datos?")
