#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {
        'User-Agent': 'script:ALUStudentBot:1.0 (by /u/Fine-Blacksmith3995)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get('data', {}).get('children', [])
    for post in posts:
        print(post.get('data', {}).get('title'))

