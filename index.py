from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
   # max_tokens=None,
    #//timeout=None,
    #//max_retries=2,
    # other params...
groq_api_key='',

)
response=llm.invoke("first primeminster of india was..")
print(response.content)