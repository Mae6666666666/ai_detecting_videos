from config import API_KEY, BASE_URL, MODEL
import json
import requests
from ddgs import DDGS
from openai import OpenAI

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

GORILLAZ_GENERATOR ={
    "name": "Gorillaz",
    "system_prompt": '''You are an expert in all information revolving around the band Gorillaz. You know 
    at least 5 about each band member, every album released, and other little things about the band such as 
    promotions they have done, collaborations, and music videos promoting said collaboration'''

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



def gorillaz_fact_checker(fact):
    print("-" * 50)

    messages = [
        {"role": "system", "content": GORILLAZ_GENERATOR["system_prompt"]},
        {"role": "user", "content": f"verify if this fact is real. you can use tools, use the internet to fact check: {fact} DO NOT use your own knowledge. if you cant verify via the internet, simply say you don't know"}
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


gorillaz_fact_checker("Phase three of the band Gorillaz is titled Plastic Beach")

