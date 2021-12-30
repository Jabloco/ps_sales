import logging
import requests

from constants import API_URL

logging.basicConfig(handlers=[logging.FileHandler('api_error.log', 'a', 'utf-8')],
                    format='%(levelname)s - %(message)s')


class BotApiClient:
    API_BASE_URL = API_URL

    def start(self, user_id) -> list:
        try:
            req = requests.post(f'{self.API_BASE_URL}/start/{user_id}')
            req.raise_for_status()
            answer = req.json()
        except ValueError as error:
            logging.exception(error)
            return
        except requests.RequestException as error:
            logging.exception(error)
            return
        return answer
