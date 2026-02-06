from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_KEY")

def analyze_sentiment(text):
    if not text:
        return "Neutral"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"""
                Analyze the sentiment of the following news article.
                Respond with only one word: Positive, Neutral, or Negative.

                Text:
                {text}
                """
            }
        ]
    )

    return response.choices[0].message.content.strip()
