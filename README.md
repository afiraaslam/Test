# Multi-Agent System

This project implements a multi-agent system using Flask, LLaMA, and YouTube video summarization tools. The system allows users to interact with two assistants: one for general conversation and another specifically for summarizing YouTube videos.

## Features

- **Conversational Agent**: Provides solutions and assistance based on user queries.
- **YouTube Video Summarization**: Extracts key points and summarizes YouTube videos in JSON format.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **LLaMA**: A large language model for generating responses.
- **YouTubeSearchTool**: A tool to search and retrieve YouTube video details.
- **Asyncio**: For managing asynchronous operations in Python.

## Prerequisites

1. Python 3.7 or higher.
2. Required packages:
   - `flask`
   - `autogen`
   - `llama-cpp`
   - `langchain-community`

You can install the required packages using requirements.txt file:

```bash
pip install -r requirements.txt

## Setup

1. Clone the repository
``bash
git clone https://github.com/afiraaslam/Test.git

2. Download llama3 model from [link](https://huggingface.co/bartowski/Meta-Llama-3-8B-Instruct-GGUF/tree/main)

3. Update downloaded model path in src.py file

4. run the code by following command
``bash
python main.py



