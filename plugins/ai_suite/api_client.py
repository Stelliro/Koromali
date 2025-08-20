# /plugins/ai_suite/api_client.py
import requests
from typing import Tuple, TYPE_CHECKING
from utils.logger import log

if TYPE_CHECKING:
    from app_core.settings_manager import SettingsManager

class ApiClient:
    """A client to interact with various AI model APIs."""

    PROVIDER_CONFIG = {
        "OpenAI": {
            "endpoint": "https://api.openai.com/v1/chat/completions",
            "models": ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"],
            "api_key_required": True
        },
    }

    def __init__(self, settings_manager: "SettingsManager"):
        self.settings_manager = settings_manager

    def get_api_key(self, provider: str) -> str | None:
        """Retrieves an API key for a given provider from settings (if required)."""
        api_keys = self.settings_manager.get("ai_api_keys", {})
        return api_keys.get(provider)

    def send_request(
        self, provider: str, model: str, system_prompt: str, user_prompt: str
    ) -> Tuple[bool, str]:
        """
        Sends a request to the specified AI provider.

        Returns a tuple: (success: bool, response_content: str)
        """
        config = self.PROVIDER_CONFIG.get(provider)
        if not config:
            return False, f"Configuration for provider '{provider}' not found."

        if config.get("api_key_required", True) and not self.get_api_key(provider):
            msg = f"API Key for {provider} not found. Please configure it in the settings."
            return False, msg

        if model not in config.get("models", []):
            log.warning(f"Model '{model}' not listed for provider '{provider}'. Proceeding anyway.")

        headers = {"Content-Type": "application/json"}
        if config.get("api_key_required", True):
            headers["Authorization"] = f"Bearer {self.get_api_key(provider)}"

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": 4096
        }

        try:
            log.info(f"Sending request to {provider} model {model}...")
            response = requests.post(
                config["endpoint"],
                headers=headers,
                json=payload,
                timeout=180
            )
            response.raise_for_status()

            data = response.json()
            content = data.get("choices", [{}])[0].get("message", {}).get("content")
            if not content:
                log.error(f"Unexpected response shape from {provider}: {data}")
                return False, "Received an unexpected response from the API. See logs for details."

            log.info("Successfully received response from AI.")
            return True, content.strip()

        except requests.exceptions.RequestException as e:
            detail = f"API request failed: {e}"
            if hasattr(e, 'response') and e.response is not None:
                detail += f"\nResponse: {e.response.text}"
            log.error(detail)
            return False, detail
        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"
            log.error(error_message, exc_info=True)
            return False, error_message