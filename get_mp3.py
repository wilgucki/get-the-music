import argparse
import os
import subprocess
import sys

from pytube import YouTube


def main(url):
    yt = YouTube(url)

    # download the first stream there is. if you need the best quality you might want to iterate over list of streams
    # and get the best one
    file = yt.streams.first().download()
    output = f'{os.path.splitext(file)[0]}.mp3'

    subprocess.run(f'ffmpeg -i "{file}" "{output}"', shell=True)
    os.unlink(file)

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts given Youtube video into mp3 file')
    parser.add_argument('--url', help='Youtube video url')

    args = parser.parse_args()

    if args.url is None:
        raise argparse.ArgumentTypeError('url is missing')

    sys.exit(main(args.url))
