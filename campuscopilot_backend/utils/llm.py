from .langchain_llm import langchain_llm
import logging

logger = logging.getLogger(__name__)

def ask_llm(messages):
    try:
        logger.info("Generating response from LangChain+Google LLM")
        response =  langchain_llm.generate_response(messages)
        logger.info("Successfully generated response")
        return response
    except Exception as e:
        logger.error(f"Error in ask_llm: {str(e)}")
        return "Sorry, I couldn't generate a response right now."