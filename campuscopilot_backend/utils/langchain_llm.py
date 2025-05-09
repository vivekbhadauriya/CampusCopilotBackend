from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage, SystemMessage
import os
import logging

logger = logging.getLogger(__name__)

class LangChainHuggingFaceLLM:
    def __init__(self):
        api_key = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
        if not api_key:
            raise ValueError("HUGGINGFACEHUB_API_TOKEN environment variable not set")
        self.llm = HuggingFaceHub(
            repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
            huggingfacehub_api_token=api_key,
            model_kwargs={"temperature": 0.5, "max_new_tokens": 512}
        )

    def generate_response(self, messages, max_length=512):
        prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
        try:
            response = self.llm.invoke(prompt)
            return response.strip()
        except Exception as e:
            logger.error(f"Error in LangChainHuggingFaceLLM.generate_response: {e}")
            return "Sorry, I couldn't generate a response right now."

langchain_llm = LangChainHuggingFaceLLM()