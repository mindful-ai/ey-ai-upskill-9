# Imports
from groq import Groq 

# Read API keys
with open(r"E:\Lenovo Ideapad 330\company-material\digital-workforce-transformation\ai-upskill-9\key-vault\groq\api.key", "r") as f:
    api_key = f.read().strip()

# Initialize Groq client
client = Groq(api_key=api_key)

# Select model
model="llama-3.1-8b-instant"

# Chat function
def chat():

    # Welcome message
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    print("------------------------------------------------------------")
    print("AI: Hello! How can I assist you today?")
   
    # Conversation history (list)
    conversation_history = []

    # Inifinite loop
    while True:
    
        # User input
        user_input = input("You: ")

        # Check for the exit condition (exit, quit, end)
        if user_input.lower() in ["exit", "quit", "end"]:
            print("AI: Goodbye!")
            break

        # Add user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Build a prompt using conversation history
        try:

            # Get the Groq response
            response = client.chat.completions.create(
                model=model,
                messages=conversation_history,
                max_tokens=150,
                temperature=0.7,
            )

            # extract the output text
            ai_message = response.choices[0].message.content.strip()


            # print the output text
            print(f"AI: {ai_message}")

            # add the ai message into the conversation history as an object with a role
            conversation_history.append({"role": "assistant", "content": ai_message})


        except Exception as e:

            # Add an exception message
            print(f"AI: Sorry, I encountered an error: {str(e)}")

# run the chatbot
if __name__ == "__main__":
    chat()
