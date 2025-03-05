from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from dotenv import load_dotenv

load_dotenv()

model =  ChatOpenAI()


# without chat history maintain
# while True:
#     user_input = input("You: ")
#     if user_input == 'exit':
#         break
#     result = model.invoke(user_input)
#     print("AI: ", result.content)



# with chat history maintain to better output

chat_history = [
    SystemMessage(content="You are a knowledgeable AI assistant.")
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)