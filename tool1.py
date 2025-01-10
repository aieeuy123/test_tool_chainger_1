import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("@root")

def user_getter_tool(url="https://jsonplaceholder.typicode.com/posts/"):
    try:
        logger.info(f"Requesting to {url}")
        response = requests.get(url)
        logger.info("Request successful")
        logger.info(str(response.json()[0])+f" + {len(response.json())-1} ...")
        return response.json()
    except Exception as err:
        logger.error(f"Error occurred: {err}")
        return None
# USAGE
response = user_getter_tool()
print(response)