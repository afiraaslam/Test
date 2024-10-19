from llama_cpp import Llama
from langchain_community.tools import YouTubeSearchTool
import asyncio

# Initialize LLaMA
llm = Llama(
    model_path="E:\Second_Test\model\Meta-Llama-3-8B-Instruct-Q4_K_M.gguf",
)

# Initialize YouTubeSearchTool
tool = YouTubeSearchTool()


def get_response(query):
    output = llm(
        prompt=f"""You are a conversation chatbot. User will ask questions and you have to provide assistance.
                Always follow following instructions:
                1. Keep the answers relevant
                2. Do not add extra information in your answers
                user Question: {query}""",
        max_tokens=200,
        echo=False,
        temperature=0.5,
    )
    return output["choices"][0]["text"]


def analyze_videos(search_query):
    results = tool.run(search_query)
    # video_prompt = convert_videos_to_prompt(results)
    return results


# def convert_videos_to_prompt(videos):
#     prompt = f"""You are helpfull assistant who helps in summarizing youtube videos.
#     videos are provided in list {videos}"""
#     return prompt
