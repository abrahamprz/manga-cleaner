import requests

BASE_URL = "https://api.mangadex.org"

# Function to get manga id from title
def get_manga_id(title):
    r = requests.get(
        f"{BASE_URL}/manga",
        params={"title": title}
    )
    return [manga["id"] for manga in r.json()["data"]]

if __name__ == "__main__":
    manga_id = get_manga_id(input("Enter manga title: "))
    print(manga_id)