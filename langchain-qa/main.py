import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from openai import APIError, AuthenticationError, RateLimitError

# Load API key
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    print("Error: Add your API key to the .env file.")
    exit()

# Connect to OpenAI
model = ChatOpenAI(
    model="gpt-6-luna",
    use_responses_api=True,
    output_version="responses/v1"
)

# Create the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Q&A assistant. Give clear and simple answers."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

# Connect prompt and model
chain = prompt | model

# Store conversation history
history = []

print("Q&A Assistant started!")
print("Type 'exit' to stop.\n")

while True:
    question = input("You: ").strip()

    # Check for empty questions
    if not question:
        print("Please enter a question.\n")
        continue

    if question.lower() == "exit":
        print("Goodbye!")
        break

    try:
        # Get an answer
        response = chain.invoke({
            "history": history,
            "question": question
        })

        answer = response.text
        print("\nAssistant:", answer, "\n")

        # Save conversation
        history.append(HumanMessage(content=question))
        history.append(AIMessage(content=answer))

        # Keep only the last 3 exchanges
        history = history[-6:]

    except AuthenticationError:
        print("Error: Check your API key.\n")

    except RateLimitError as error:
        print("API request was limited.")
        print("Details:", error.message)
        print("Error code:", error.code)

    except APIError:
        print("Error: OpenAI could not process the request.\n")

    except Exception as error:
        print("Unexpected error:", error)