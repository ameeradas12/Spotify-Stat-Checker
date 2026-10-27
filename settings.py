import json
import os

SETTINGS_DIR = os.path.join(os.getenv("APPDATA"), "SpotifyStatsViewer")
SETTINGS_FILE = os.path.join(SETTINGS_DIR, "settings.json")


def load_client_id():
    if not os.path.exists(SETTINGS_FILE):
        return None
    with open(SETTINGS_FILE) as f:
        data = json.load(f)
    return data.get("client_id")


def save_client_id(client_id):
    os.makedirs(SETTINGS_DIR, exist_ok=True)
    with open(SETTINGS_FILE, "w") as f:
        json.dump({"client_id": client_id}, f, indent=2)


if __name__ == "__main__":
    print(load_client_id())        # first run: None
    print(load_client_id())        # should print test123