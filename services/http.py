import json
import requests
import sys

# TODO: change this URL before using the app
API_URL = "https://dev.p2p.ms/pp/apiTEST/"
#API_URL = "https://localhost:44365/"

def send_post_request(url: str, data: json) -> str:
    """
    Sends a POST request to the specified URL with the provided data.

    Args:
        url (str): The URL to send the POST request to.
        data (json): The data to include in the POST request. {"name": "Ekin Berk"}

    Returns:
        bytes: The content of the response if the request was successful, None otherwise.
    """

    final_url = API_URL + url

    # Request headers
    headers = {
        "Content-Type": "application/json"}

    print("\n\nPost process has been started. Please wait...\n ")

    try:
        # send the POST request with the provided URL and data
        response = requests.post(
            final_url, data=data, headers=headers, verify=False)
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
        sys.exit()
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))
        sys.exit()
    except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))
        sys.exit()

    if response.ok:  # check if the response was successful
        print("POST request successful\n")
        # return the content of the response if the request was successful
        # use response.text instead of response.content to return a str object
        return response.text
    else:
        print("POST request failed\n")
        print(response.text)
        sys.exit()


def get_request(url: str):
    """
    Sends a GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        response_data (json): The data returns if the GET request is successful. If not returns None.
    """

    # Create the url
    final_url = API_URL + url

    try:
        # Send GET request to the API.
        response = requests.get(url=final_url, verify=False)

        if response.status_code == 200:
            response_data = response.json()
            print("GET request successful")

            return response_data
    except Exception as e:
        print("Exception has occured: ", e)
        sys.exit()
