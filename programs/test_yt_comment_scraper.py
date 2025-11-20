import re, json, requests

VIDEO_ID = "qdfVsrpkOX4"
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120 Safari/537.36",
    "accept": "application/json, text/javascript, */*; q=0.01",
})

# 1) fetch video page
r = session.get(f"https://www.youtube.com/watch?v={VIDEO_ID}")
html = r.text

# 2) extract INNERTUBE_API_KEY and ytInitialData
key_m = re.search(r'INNERTUBE_API_KEY\":\"([^"]+)', html)
init_m = re.search(r'var ytInitialData = (\{.*?\});', html, re.DOTALL)
if not key_m or not init_m:
    raise SystemExit("Couldn't find INNERTUBE_API_KEY or ytInitialData")

api_key = key_m.group(1)
yt_initial = json.loads(init_m.group(1))

# 3) find first 'continuation' under the comments section
def find_continuation(obj):
    if isinstance(obj, dict):
        for k,v in obj.items():
            if k == "continuationEndpoint" or k == "continuation":
                return v
            res = find_continuation(v)
            if res:
                return res
    elif isinstance(obj, list):
        for item in obj:
            res = find_continuation(item)
            if res:
                return res
    return None

cont = find_continuation(yt_initial)
if not cont:
    raise SystemExit("No comments continuation found (maybe comments are disabled)")

# cont might be a dict with a token deep inside; extract token string:
if isinstance(cont, dict):
    # pattern differs; try common places:
    token = cont.get("continuation") or cont.get("token") or \
            (cont.get("continuationEndpoint") or {}).get("continuationCommand", {}).get("token")
else:
    token = cont

# 4) call youtubei next endpoint to get comments
url = f"https://www.youtube.com/youtubei/v1/next?key={api_key}"
payload = {
    "context": {
        "client": {
            "clientName": "WEB",
            # clientVersion ideally from page (INNERTUBE_CLIENT_VERSION)
            "clientVersion": "2.20201021.03.00"
        }
    },
    "continuation": token
}
resp = session.post(url, json=payload)
data = resp.json()
# data now contains comment renderers and possibly another continuation token to page further
print(data.keys())

