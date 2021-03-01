import os

import requests
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_link(fact):
    url = f"https://hidden-journey-62459.herokuapp.com/piglatinize/"
    data = {"input_text": fact}
    response = requests.post(url, data=data, allow_redirects=False)

    return response.headers['Location']

@app.route('/')
def home():
    fact = get_fact().strip()
    link = get_link(fact)

    return str(link)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

