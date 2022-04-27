"""Buggy code"""
# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-
# gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import subprocess

"""docstring"""
def transcode_file(filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


"""Assert statements"""
def function(user):
    assert user.is_admin, 'user does not have access'
    # secure code...


"""Pickles"""
class RunBinSh():
    """reduce"""
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))
    """reduce"""
    def __reduce2__(self):
        return (subprocess.Popen, (('/bin/sh',),))


"""docstring"""
def import_urlib_version(version):
    exec("import urllib%s as urllib" % version)


"""docstring"""
def index():
    """docstring"""
    module = flask.request.args.get("module")
    import_urlib_version(module)
