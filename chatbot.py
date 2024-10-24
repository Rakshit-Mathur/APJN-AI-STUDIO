import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDX475MN7wtXDMjEqu6RIwm8yZh_WofgZE", transport='rest')

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="This chatbot Model is for deaf and blind people. It has a feature that allows deaf people to communicate with the chatbot using hand signs. deaf mode features voice interpretation along with printing on a paper for blind people on their dot language. Your name is karlson",
)

chat_session = model.start_chat()
while True: 
  response = chat_session.send_message(input("Enter your Message:"))
  print(response.text)
