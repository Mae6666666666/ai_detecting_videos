from config import API_KEY, BASE_URL, MODEL

from openai import OpenAI

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

GORILLAZ_GENERATOR ={
    "name": "Gorillaz",
    "system_prompt": '''You are an expert in all information revolving around the band Gorillaz. You know 
    at least 5 about each band member, every album released, and other little things about the band such as 
    promotions they have done, collaborations, and music videos promoting said collaboration'''

}

def gorillaz_fact_checker(fact_number):
    print("-" * 50)

    messages = [
        {"role": "system", "content": GORILLAZ_GENERATOR["system_prompt"]},
        {"role": "user", "content": f"Please give me {fact_number} facts about Gorillaz. Please write each facts with no more than 15 words"}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    print(response.choices[0].message)

gorillaz_fact_checker(3)