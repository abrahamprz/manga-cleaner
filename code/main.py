import requests

base_url = "https://api.mangadex.org"

r = requests.get(
    f"{base_url}/manga",
    params={"title": input("Manga title: ")}
)

print([manga["id"] for manga in r.json()["data"]])