import facebook_scraper
import sys
import json
import requests.exceptions

def to_json(dict_var):
    return json.dumps(dict_var, default=str)


if len(sys.argv) != 5:
    print("ERROR: wrong number of arguments")
    exit(1)


try:
    proxy = sys.argv[4]
    facebook_scraper.set_proxy(proxy)

    command = sys.argv[1]
    if command == "feed":
        username = sys.argv[2]
        limit = int(sys.argv[3])
        posts = facebook_scraper.get_posts(account=username, options={"reactions": True})
        with open(username + ".txt", "w") as f:
            count = 0
            for post in posts:
                s = to_json(post)
                print(s)
                f.write(s + "\n")
                count += 1
                if count >= limit:
                    break

    elif command == "post":
        url = sys.argv[2]
        file = sys.argv[3]
        posts = facebook_scraper.get_posts(post_urls=[url], options={"reactions": True})
        with open(file, "w") as f:
            post = next(posts)
            f.write(to_json(post))
    else:
        print("unknown command: " + command)
        exit(1)

except requests.exceptions.ProxyError:
    exit(2)
