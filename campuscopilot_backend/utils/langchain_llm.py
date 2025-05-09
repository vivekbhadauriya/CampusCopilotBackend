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

    def generate_response(self, messages, max_length=256):
        system_prompt = next((m['content'] for m in messages if m['role'] == 'system'), "")
        user_message = next((m['content'] for m in reversed(messages) if m['role'] == 'user'), "")

        # Add clear instructions for concise, structured output
        instructions = (
            "Please answer concisely, using headings and bullet points where appropriate. "
            "Keep the response short and easy to read."
        )

        prompt = f"{system_prompt}\nInstructions: {instructions}\nQuestion: {user_message}\nAnswer:"

        try:
            response = self.llm.invoke(prompt)
            # Only return the part after 'Answer:'
            if "Answer:" in response:
                return response.split("Answer:", 1)[1].strip()
            return response.strip()
        except Exception as e:
            logger.error(f"Error in LangChainHuggingFaceLLM.generate_response: {e}")
            return "Sorry, I couldn't generate a response right now."

langchain_llm = LangChainHuggingFaceLLM()