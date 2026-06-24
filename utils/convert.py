# Convert .ogg to .mp3
import subprocess 

def convert_ogg_to_mp3(ogg_folder):
    cmd_script = f'audioconvert convert "{ogg_folder}" "D:/Data Science/SpotifyViz/data/" --output-format .mp3'
    subprocess.run(cmd_script)

if __name__ == "__main__":
    convert_ogg_to_mp3("C:/Users/Bob/Music/Zotify Music/My top tracks playlist/")