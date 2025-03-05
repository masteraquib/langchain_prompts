from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

# Define a ChatPromptTemplate using tuples
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="chat_history"),  # Dynamic chat history, load chat history
    ("human", "Explain in simple terms, what is {query}?")
])

# Example dynamic message history
# this can be get from the database
chat_history = [
    ("human", "What is AI?"),
    ("ai", "AI stands for Artificial Intelligence."),
]

# Inject values dynamically
formatted_prompt = chat_template.invoke({
    "chat_history": chat_history,  # Pass previous conversation dynamically
    "query": "Machine Learning"
})

# Print formatted messages
print(formatted_prompt)
