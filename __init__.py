import sys
import re
from subprocess import Popen,PIPE, call


class MetaData:

    """A class to return a list of tuples with metadata keys and 
    values for a given video path. Uses mplayer tp probe video. 
    """
    
    def __init__(self, path):
        self.path = path
        self.kv = {}

        id_re = re.compile('(^ID.*)=(.*)')
        lt_values = []
        p = Popen('mplayer -nolirc -vo null -ao null -frames 0 -identify ' + self.path, shell=True, stdout=PIPE)
        while True:
            o = p.stdout.readline()
            if o == '' and p.poll() != None: break
            # the 'o' variable stores a line from the command's stdout
            # do anything u wish with the 'o' variable here
            # this loop will break once theres a blank output 
            # from stdout and the subprocess have ended
            try:
                match = re.findall(id_re,o)[0]
                lt_values.append(match) 
            except:
                pass
        self.kv = dict(lt_values)
        #if self.kv['ID_VIDEO_FORMAT'] is '0': 
        #    print "invalid video"
        #    sys.exit()

    def all_values(self):
        #return dictionary of all values
        return self.kv

    @property
    def audio_bitrate(self):
        return self.kv['ID_AUDIO_BITRATE']
    
    @property
    def audio_codec(self):
        return self.kv['ID_AUDIO_CODEC']

    @property
    def audio_format(self):
        return self.kv['ID_AUDIO_FORMAT']

    @property
    def audio_id(self):
        return self.kv['ID_AUDIO_ID']
    
    @property
    def video_id(self):
        return self.kv['ID_VIDEO_ID']
    
    @property
    def demuxer(self):
        return self.kv['ID_DEMUXER']

    @property
    def video_format(self):
        return self.kv['ID_VIDEO_FORMAT']

    @property
    def video_bitrate(self):
        return self.kv['ID_VIDEO_BITRATE']

    @property
    def video_width(self):
        return self.kv['ID_VIDEO_WIDTH']

    @property
    def video_height(self):
        return self.kv['ID_VIDEO_HEIGHT']

    @property
    def video_fps(self):
        return self.kv['ID_VIDEO_FPS']

    @property
    def video_aspect(self):
        return self.kv['ID_VIDEO_ASPECT']

    @property
    def audio_format(self):
        return self.kv['ID_AUDIO_FORMAT']
    
    @property
    def audio_rate(self):
        return self.kv['ID_AUDIO_RATE']

    @property
    def audio_ch(self):
        return self.kv['ID_AUDIO_NCH']

    @property
    def duration(self):
        return self.kv['ID_LENGTH']

