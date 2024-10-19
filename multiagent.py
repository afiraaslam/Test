from autogen import AssistantAgent, UserProxyAgent
from src import llm, analyze_videos, get_response
import asyncio

assistant1 = AssistantAgent(
    name="assistant1",
    system_message="""You are an assitant who provides solutions.""",
)
assistant1.llm = llm
assistant2 = AssistantAgent(
    name="assistant2",
    system_message="""You are an assistant specializing in summarizing YouTube videos. 
    Your task is to extract key points and provide concise summaries in JSON format. 
    Always respond with a list of summaries like this: ['summary1', 'summary2'].""",
)
assistant2.llm = llm
user_proxy = UserProxyAgent(name="user_proxy")


def multi_agent_workflow(input_text, video=False):
    if video:
        response = analyze_videos(input_text)
        response = asyncio.run(
            assistant2.a_initiate_chat(
                assistant2,
                message=response,
            )
        )
    else:
        response = get_response(input_text)
        response = asyncio.run(
            assistant1.a_initiate_chat(
                assistant1,
                message=response,
            )
        )

    return response.chat_history[0]["content"]
