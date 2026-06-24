from argparse import ArgumentParser
from utils import convert, visualize
from dotenv import load_dotenv
import os 
import subprocess

def main(**args):
    # Get the spotify public playlist link
    spotify_link = args.link
    playlist_name = args.playlist_name

    script_to_run = f"python -m zotify {spotify_link}"
    subprocess.run(script_to_run)
    
    # Get all mp3
    ogg_folder = os.getenv('DOWNLOAD_PARENT_FOLDER') + f'/{playlist_name}'
    convert.convert_ogg_to_mp3(ogg_folder)
    

if __name__ == "__main__":
    # Arguments
    parser = ArgumentParser()
    parser.add_argument('--link', help="spotify playlist link", type=str)
    parser.add_argument('--playlist_name', help="spotify playlist name", type=str)
    args = parser.parse_args()

    # Load dotenv
    load_dotenv()
    
    # Main Process
    main(**args)