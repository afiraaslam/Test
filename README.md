# Multi-Agent System for Video Analysis and Conversation

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
