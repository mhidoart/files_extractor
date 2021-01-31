# files_extractor
the aim of this project is to extract files (images,videos,audios) from a source folder to destination folder,files are extracted from the folder and sub folders,the user must choose between image , videos , audios or he can choose to extract all of them to a folder or to the current workig directory (more in how to use section) 

# How to use

before executing you should know that the script has 6 params next is an example of use:

```
python3 main.py copy image,video,audio from /home/xana/Bureau/snB to /home/xana/Bureau/results 

```
after the name of the script which is 'main.py' there is the first param 'copy' it could be replaced by 'cut' if you want to remove files after copying

from : is the source folder where the script extract files
to:  the destination folder where files will be copied to (in case u don't specify the param its the current directory see the next example for more explanation)

### example cut files to current directory
```
python3 main.py cut image,video,audio from /home/xana/Bureau/snB 

```

or

```
python3 main.py cut image,video,audio from /home/xana/Bureau/snB to .

```

### example coppy only IMAGE files to current directory
```
python3 main.py copy image from /home/xana/Bureau/snB 

```

# NOTE !!! 
 you may need to execute the script as a super user 'sudo' if you are working with some privileged files 

 # Buy me a coffee if i helped you :
 [![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
