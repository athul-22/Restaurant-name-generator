import getpass
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass(
        "Provide your Google API Key")

try:
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    

except Exception as e:
    print(f"Error creating model: {e}")


def generate_name(cuisine):
    result = llm.invoke("Restaurant name generate a name for a {cuisine} restaurant. give in a response['restaurant_name'] and response['menu_items']. type format ")
    print(result.content)

    return result.content
