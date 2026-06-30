import os
import subprocess
from argparse import ArgumentParser

from dotenv import load_dotenv
from utils import convert


def main(**args):
    # Get the spotify public playlist link
    spotify_link = args.get("link")
    playlist_name = args.get("playlist_name")

    # Download the playlist using zotify
    script_to_run = f"python -m zotify {spotify_link}"
    subprocess.run(script_to_run)

    # Get all mp3
    ogg_folder = os.getenv("DOWNLOAD_PARENT_FOLDER") + f"/{playlist_name}"
    convert.convert_ogg_to_mp3(ogg_folder, os.getenv("SAVE_FOLDER"))


if __name__ == "__main__":
    # Arguments
    parser = ArgumentParser()
    parser.add_argument("--link", help="spotify playlist link", type=str)
    parser.add_argument("--playlist_name", help="spotify playlist name", type=str)
    args = parser.parse_args()

    # Load dotenv
    load_dotenv()

    # Main Process
    main(**args)
