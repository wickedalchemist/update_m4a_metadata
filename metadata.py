import glob
import string
import numpy as np
from mutagen.mp4 import MP4
from mutagen.id3 import ID3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC

#Get list of all m4a files in current directory
#Each file has filename structure artist-song-album.m4a
files=glob.glob('*.m4a')
info=[]
for i in range(len(files)):
    info.append(string.split(files[i],'_'))    
  
artist=[]
album=[]
song=[]

#Loop though files, get artist, song, album from filename
#Edit metadata with this information so that it will show up in media player
for i in range(len(files)):
    artist=string.replace(info[i][0],'-',' ')
    song=string.replace(info[i][1],'-',' ')
    album=string.replace(info[i][2],'-',' ')[:-4]
    audio=ID3()
    audio.add(TPE1(encoding=3, text=unicode(artist)))
    audio.add(TIT2(encoding=3, text=unicode(song)))
    audio.add(TALB(encoding=3, text=unicode(album)))
    audio.save(files[i],v1=2)
    audio.pprint()    
  
#That's it!
print "All Files's Metadata Updated"


 
