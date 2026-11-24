# LangChain Q&A Assistant

## Description

This project is a simple AI assistant built with LangChain
and the OpenAI API.

It accepts questions and returns answers.
It also remembers recent conversation history.

## Main Components

- Prompt: Instructions that tell the AI how to respond.
- Model: OpenAI's GPT-6 Luna language model.
- Chain: Connects the prompt to the model.
- History: Stores the last three conversations.
- Agent: An AI system that can choose tools and take
  actions. This project does not use an agent.

## How It Works

The user enters a question.

The prompt combines the instructions, conversation history,
and new question.

The chain sends this information to the model.

The model returns an answer, which is displayed and saved
in conversation history.

## Setup

Create a virtual environment:

    python3 -m venv .venv

Activate it:

    source .venv/bin/activate

Install the packages:

    python -m pip install -r requirements.txt

Create your environment file:

    cp .env.example .env

Add your OpenAI API key to the .env file.

## Run

    python main.py

Type exit to stop the assistant.

## Testing

Five test questions and their answers are recorded in
test_evidence.md.

## Errors

The program checks for:
- Empty questions
- Invalid API keys
- API usage limits
- Other API errors

## Risks and Limitations

- The assistant can provide incorrect information.
- Conversation history disappears when the program closes.
- API requests require internet access.
- API usage may incur charges.
- The assistant does not verify every answer.
- The API key must never be uploaded to GitHub.