import openai

def generate_pmax_themes(grouped_keywords, api_key):
    client = openai.OpenAI(api_key=api_key)

    prompt = f"""Suggest PMax campaign asset group themes based on these keywords:
{grouped_keywords}
Include: Product Category, Use-case, Demographics, and Seasonal themes."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a digital marketing expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
