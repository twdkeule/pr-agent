from os import environ
from pr_agent.algo.ai_handlers.base_ai_handler import BaseAiHandler
from retry import retry

from pr_agent.algo.ai_handlers.base_ai_handler import BaseAiHandler
from pr_agent.algo import NO_SUPPORT_TEMPERATURE_MODELS
from pr_agent.config_loader import get_settings
from pr_agent.log import get_logger
from httpx import AsyncClient


OPENAI_RETRIES = 5


class AmAIHandler(BaseAiHandler):
    def __init__(self):
        self.base_url = get_settings().get("OPENAI.api_base", None)
        self.api_key = get_settings().get("OPENAI.KEY", None)

    @property
    def deployment_id(self):
        return get_settings().get("OPENAI.DEPLOYMENT_ID", None)

    async def chat_completion(self, model: str, system: str, user: str, temperature: float = 0.2, img_path: str = None):
        """
        This method should be implemented to return a chat completion from the AI model.
        Args:
            model (str): the name of the model to use for the chat completion
            system (str): the system message string to use for the chat completion
            user (str): the user message string to use for the chat completion
            temperature (float): the temperature to use for the chat completion
        """
        get_logger().debug("Prompts", artifact={"model": model, "system": system, "user": user})
        url = self.base_url + '/chat/completions'
        headers = {
            'Authorization': 'Bearer ' + self.api_key,
        }
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]
        content = {
            "model": model, 
            "messages": messages,
        }
        if model not in NO_SUPPORT_TEMPERATURE_MODELS:
            content["temperature"] = temperature
        
        try:
            client = AsyncClient(verify=False)
            r = await client.post(url, json=content, headers=headers, timeout=300)
            r.raise_for_status()
            chat_completion = r.json()
            choice0 = chat_completion["choices"][0]
            resp = choice0["message"]["content"]
            finish_reason = choice0["finish_reason"]
            get_logger().debug(f"AI response: {resp}")
            return resp, finish_reason
        except Exception as e:
            get_logger().error(f"Unknown error during AmAI inference: {e}")
            raise e