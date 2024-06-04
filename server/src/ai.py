'''
@brief 向大模型寻求旅游建议
@param location 地点
@param type str
@return 游玩建议
@return type str
'''
from zhipuai import ZhipuAI

def get_suggestion(location:str):
    client = ZhipuAI(api_key="a9bae78a296e575676bb91c8b125bcfa.Q8G7UawOhN6yF2rl")

    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {
                "role":"user",
                "content":f"我计划今天到{location}去游玩,请你给我一些游玩建议,包括介绍一下{location},今天的天气该穿什么衣服,有哪些推荐的参观点,以及推荐的参观路线"
            },
        ],
        max_tokens=8192,
        temperature=0.9,
        tools=[
            {
                "type":"web_search",
                "web_search":
                {
                    "enable":"true",
                    "search_query":f"{location}"
                }
            },
        ],
    )
    return response.choices[0].message.content # type:ignore

'''
@brief 直接向大模型提问
@param question 问题
@param type str
@return 回答
@return type str
'''
def get_response(question:str):
    client = ZhipuAI(api_key="a9bae78a296e575676bb91c8b125bcfa.Q8G7UawOhN6yF2rl")

    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {
                "role":"user",
                "content":f"{question}"
            },
        ],
        max_tokens=8192,
        temperature=0.9,
    )
    return response.choices[0].message.content # type:ignore

# print(get_response("你好"))