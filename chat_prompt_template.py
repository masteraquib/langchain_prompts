# how we can send the Dynamic List of Messages
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model =  ChatOpenAI()

# chat_template =  ChatPromptTemplate([
#     SystemMessage(content="Your are a helpful {domain} expert"),
#     HumanMessage(content="Explian in simple terms, what is {topic}")
# ])


chat_template =  ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert."),
    ("human", "Explain in simple terms, what is {topic}?")
])

prompts =  chat_template.invoke({
    "domain":"cricket",
    "topic":"Dusra"
})

print(prompts)


