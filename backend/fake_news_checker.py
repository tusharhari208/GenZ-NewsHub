from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_KEY")

def check_fake_news(text):
    if not text:
        return "Unverified"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"""
                Analyze the following news content and classify it as:
                - Likely Genuine
                - Possibly Misleading
                - Unverified

                Text:
                {text}
                """
            }
        ]
    )

    return response.choices[0].message.content.strip()
