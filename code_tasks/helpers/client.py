import requests


def json_reader(resp: requests.Response):
    return resp.json()


def bytes_reader(resp: requests.Response):
    return {'status': resp.status_code, 'content': resp.content.decode()}


if __name__ == "__main__":
    url = "http://localhost:8080"
    # response = requests.get(url)
    response = requests.post(url=url, data='asdf')

    # print(json_reader(response))
    print(bytes_reader(response))
