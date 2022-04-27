"""Buggy code"""
# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-
# gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import subprocess

"""docstring"""
def transcode_file(filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!
