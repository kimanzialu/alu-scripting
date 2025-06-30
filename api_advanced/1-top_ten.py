#!/usr/bin/python3
"""1-top_ten.py"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'script:ALUStudentBot:1.0 (by /u/New-Football1059)'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
