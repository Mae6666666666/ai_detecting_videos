from config import API_KEY, BASE_URL, MODEL
import json
import requests
from ddgs import DDGS
from openai import OpenAI

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

AI_DESCRIPTION ={
    "name": "AI Video Verifier",
    "system_prompt": '''You are an AI trained to specifically analyse descriptions given by another AI agent which previously analysed the video and turned it into json for you to read and verify, and confirm the likeliness of them being AI generated. Use tools and the internet to help you. If the prompt involves verifying if a movie is fake, for example asking if a movie trailer is legit, use the internet to check it. DO NOT use your own knowledge'''

}

tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the internet using DuckDuckGo. Returns top results.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query (e.g. '2d was born on 1978')",
                    }
                },
                "required": ["query"],
            },
        },
    }
]

def web_search(query):
    try:
        ddgs = DDGS()
        results = ddgs.text(query, max_results=5)
        if results:
            return json.dumps(results)
        else:
            return json.dumps([{"error": "No results found"}])
    except Exception as e:
        return json.dumps([{"query": query, "error": f"Search failed: {str(e)}"}])



def gorillaz_fact_checker(video_json):
    print("-" * 50)

    messages = [
        {"role": "system", "content": AI_DESCRIPTION["system_prompt"]},
        {"role": "user", "content": f"Please verify the json of this video and tell me if it is real or likely AI generated as a percentage: {video_json}"}
    ]

    max_tool_calls = 5  # Safety limit so it doesn't loop forever
    tool_call_count = 0

    while tool_call_count < max_tool_calls:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
        )

        message = response.choices[0].message

        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_args = json.loads(tool_call.function.arguments)
                query = tool_args.get("query", "?")

                print(f'[Searching the web for: "{query}"]')

                # Run the REAL search
                result = web_search(query)

                # Show a preview of what came back
                result_data = json.loads(result)

                messages.append(message)
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result_data),
                    }
                )
                tool_call_count += 1
        else:
            print(f"[Fact Checker]: {message.content}")
            break

    if tool_call_count >= max_tool_calls:
        print("[Hit max tool calls -- stopping]")




video0 = {
    "title": "Cat playing saxophone",
    "extra_limbs": True,
    "innacurate_lighting": True,
    "unnatural_animal_behaviour": True,
    "grainy_off_sounding_voices": False
}

video1 = {
    "title": "Dog playing with a frizbee",
    "extra_limbs": False,
    "innacurate_lighting": True,
    "unnatural_animal_behaviour": False,
    "grainy_off_sounding_voices": False
}

video2 = {
    "title": "Damon Albarn giving away free phones",
    "extra_limbs": False,
    "innacurate_lighting": True,
    "unnatural_facial_expressions": True,
    "off_lip_syncing": True,
    "odd_sounding_audio": True
}

video3 = {
    "title": "Masters Of The Universe Trailer",
    "extra_limbs": False,
    "innacurate_lighting": False,
    "unnatural_facial_expressions": False,
    "off_lip_syncing": False,
    "odd_sounding_audio": False
}


gorillaz_fact_checker(video3)

