from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_KEY")

def summarize_news(content):
    if not content:
        return "Summary not available."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Summarize this news in 3 short GenZ-friendly bullet points:\n{content}"
            }
        ]
    )
    return response.choices[0].message.content
