import openai
import json

openai.api_key = "YOUR_API_KEY"  # Replace with your own API key

def generate_response(prompt):
    # Generate a response from the API
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the generated text from the response
    message = response.choices[0].text.strip()

    return message

# Example usage
prompt = "Hi, how are you doing today?"
response = generate_response(prompt)
print(response)
