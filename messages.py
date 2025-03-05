from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# messages = [
#     SystemMessage(content="You are a helpful assistant"),
#     HumanMessage(content="tell me about LangChain")
# ]

messages = [
    SystemMessage(content="You are a knowledgeable AI assistant."),
    HumanMessage(content="What is LangChain and how is it used in LLM applications?")
]


result = model.invoke(messages)

messages.append(AIMessage(result.content))

print(messages)