#slide:ffmpeg main part, probe,play, 
#slide pribe, slide
#inherit the material from the sandbox


import subprocess,os

#p= subprocess.cal('ffmpeg code goes here', shell=True)
#mention sometimes you will see ffmpeg.exe
#p = subprocess.call('ffmpeg.exe -i video.mp4', shell=True)
#it may be hard to see what is going on so lets do it this way 




#this will take audio of each file
def extractAudioFromVid():
    files = os.listdir("./")
    for f in files:
        if f.lower()[-3:] == "mp4":
            print("processing", f)
            process(f)

def process(f):
    inFile = f
    outFile = f[:-3] + "mp3"
    cmd = "ffmpeg -i {} -vn  -ac 2 -ar 44100 -ab 320k -f mp3 {}".format(inFile, outFile)
    #this is old and not recommended you can rewrite this using the other
    os.popen(cmd)

#extractAudioFromVid()
#if you file has no audio then it will say 
##Output file #0 does not contain any stream
#test the building block for the ffmpeg splut 
##os.system("ffmpeg -i video.mp4 -ss 00:00:00 -to 00:05 -c:v copy -c:a copy snip_video.mp4")

name="in.mp4"
number=1
output=f"cut_{number}_{name}"
#os.system(f"ffmpeg -i {name} -ss 00:00:00 -to 00:05 -c:v copy -c:a copy {output}")
#os.system(f"ffmpeg -i {name} -vf fps=1 out%d.png")
#os.system(f"ffplay {name}")
#os.system(f'ffplay {name} -vf "setpts=4.0*PTS" output.mp4')

import subprocess

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    print(f"{float(result.stdout)}")
    return float(result.stdout)

#get_length(name)

#output for get length is :8.083333 measuresd in 

#https://www.ostechnix.com/how-to-rotate-videos-using-ffmpeg-from-commandline/
os.system(f'ffmpeg -i vid.mp4 -vf "transpose=3" 20170919_191711.mp4')