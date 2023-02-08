"""
This script is used to convert a csv with the format "title;artist;path_to_audio_file" into an m3u playlist.

Created by:
Johannes Schnurrenberger

Last Changed:
08.02.2023
"""

# Modules

def make_m3u_entry(list_entry):
    """
    Creates two lines for the m3u playlist. 1. is the title information, 2. line is the file location
    """
    entry =  []
    start_line = "#EXTINF:"

    for element in list_entry.split(";"):
        entry.append(element)
        
    return "{}{}{}\n{}".format(start_line, entry[0], entry[1], entry[2])


def main():

    playlist = []

    with open (".\Playlist.csv", "r", encoding="utf-8") as f:
        playlist = f.readlines()

    header = "#EXTM3U"

    with open("./playlist.m3u" , "a", encoding="utf-8") as f:
        f.write(header)
        for i in playlist:
            f.write(make_m3u_entry(i)) 


if __name__ == "__main__":
    main()