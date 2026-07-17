import os
import requests
from typing import TypedDict

from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END
from pinecone import Pinecone

# Configurations

with open(r"E:\Lenovo Ideapad 330\company-material\digital-workforce-transformation\ai-upskill-8\key-vault\openai\api.key") as f:
    openai_api_key = f.read().strip()
os.environ["OPENAI_API_KEY"] = openai_api_key

RAG_URL = r""

with open(r"E:\Lenovo Ideapad 330\company-material\digital-workforce-transformation\ai-upskill-9\key-vault\nvd-database\api.key") as f:
    nvd_api_key = f.read().strip()
MODEL = "gpt-4.1-mini"
llm = ChatOpenAI(model=MODEL, temperature=0)


