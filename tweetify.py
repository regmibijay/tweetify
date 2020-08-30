import sys,os,subprocess,datetime
from argparse import ArgumentParser
def main(argv):
    print("Twittify V1.0, coded by Bijay Regmi [https://github.com/regmibijay]")
    print("Converts any video file to mp4 format suitable to Twitter standards using FFMPEG.")
    parser = ArgumentParser()
    parser.add_argument("-i", help = "Input a video file to be converted.")
    parser.add_argument("-ss", help = "Start time (format 00:00:00)", nargs="?", default = "00:00:00")
    parser.add_argument("--dur", help = "Duration of the video", nargs = '?',default = "length")
    parser.add_argument("-o", help="Output file name with format (e.g. out.mp4)")
    args = parser.parse_args()
    print("---")
    if args.i is None:
     print ("[FATAL ERROR] .. Please input a video file to be converted with -i <path>")
     sys.exit()
    if args.o is None:
     print ("[FATAL ERROR] .. Please input an output file name with video format (e.g. out.mp4) with -o <path>")
     sys.exit()
    if not os.path.isfile(args.i):
      print("The given input file does not exist. Please make sure specified file name is written correctly.")
      sys.exit()
    fargs = ""
    if args.dur != "length":
     args.dur = "-t " + args.dur
     fargs = 'ffmpeg -y -ss ' + args.ss + ' -i ' + args.i + ' '+ args.dur + ' -vcodec libx264 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -pix_fmt yuv420p -strict experimental -r 30 -t 2:20 -acodec aac -vb 1024k -minrate 1024k -maxrate 1024k -bufsize 1024k -ar 44100 -ac 2 ' + args.o  
    if args.dur == "length":
      fargs = 'ffmpeg -y -ss ' + args.ss + ' -i ' + args.i + ' -vcodec libx264 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -pix_fmt yuv420p -strict experimental -r 30 -t 2:20 -acodec aac -vb 1024k -minrate 1024k -maxrate 1024k -bufsize 1024k -ar 44100 -ac 2 ' + args.o
    #print (fargs)
    error = 0
    start = datetime.datetime.now()
    print("Converting now ... this might take a while.")
    try:
      rc = subprocess.call(fargs, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except:
      print ("Something went wrong while converting the video.")
      sys.exit()
    finally:
      end = datetime.datetime.now()
      print("Script ended. Conversion took " + str(end - start))    
if __name__ == "__main__":
 main(sys.argv[1:]) 