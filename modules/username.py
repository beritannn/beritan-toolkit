import requests

def run():
    username = input("Username: ")

    sites = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Dev.to": f"https://dev.to/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "StackOverflow": f"https://stackoverflow.com/users/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}"
    }

    print("\nChecking...\n")

    headers = {"User-Agent": "Mozilla/5.0"}

    for name, url in sites.items():
        try:
            r = requests.get(url, headers=headers, timeout=5)

            if r.status_code == 200:
                print(f"[FOUND] {name} -> {url}")
            else:
                print(f"[----] {name}")
        except:
            print(f"[ERR ] {name}")
