# TWEETIFY
Converts any video to mp4 format matching Twitter Video requirements using [FFMPEG](https://ffmpeg.org/). You can download binaries for your platform on release page.

### Usage
`tweetify -i test.mkv -ss 00:00:10 -t 00:00:20 -o output.mp4` 
1.  `-h` : prints help text
2.  `-i` : input video file
3.  `-ss`: start of video for trim option (in 00:00:00 format)
4.  `-t`: duration of video after -ss (in 00:00:00 format)
5.  `-o`: output video name with format.(e.g. output.mp4)
  
 ### Prerequisites
 1. FFMPEG must be added to PATH.
 2. Video input must be supported by FFMPEG.
 3. Please check max file size for video upload on Twitter.
 
