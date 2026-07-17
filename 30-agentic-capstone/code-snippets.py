import os
import requests
from typing import TypedDict

from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, START, END
from pinecone import Pinecone


