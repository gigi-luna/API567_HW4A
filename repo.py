import requests
import json


def user_info(user):
    output = []
    user_web = 'https://api.github.com/users/{user}/repos'.format(user)
    res = requests.get(user_web)
    repos = json.loads(res.test)
    output.append('User: {}'.format(user))

    for repo in repos:
        repo_name = repo['name']
        repo_url = 'http://api.github.com/repos/{}/{}/commits'.format(
            user, repo_name)
        repo_info = requests.get(repo_url)
        repo_info_json = json.loads(repo_info.text)

    return output


if __name__ == '__main__':
    for entry in user_info():
        print(entry)
