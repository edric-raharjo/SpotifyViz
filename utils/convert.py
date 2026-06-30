# Convert .ogg to .mp3
import subprocess


def convert_ogg_to_mp3(ogg_folder, save_folder):
    cmd_script = (
        f'audioconvert convert "{ogg_folder}" "{save_folder}" --output-format .mp3'
    )
    subprocess.run(cmd_script)


if __name__ == "__main__":
    convert_ogg_to_mp3(os.getenv("DOWNLOAD_PARENT_FOLDER"), os.getenv("SAVE_FOLDER"))
