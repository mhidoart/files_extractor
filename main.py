import sys
import os
import shutil


class Type_Extractor():
    def __init__(self):
        self. root = '.'
        # knowen extensions of files
        self.IMAGE = ('.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg', '.xpm', '.ief', '.pbm',
                '.tif', '.gif', '.ppm', '.xbm', '.tiff', '.rgb', '.pgm', '.png', '.pnm')

        self.VIDEO = ('.m1v', '.mpeg', '.mov', '.qt', '.mpa',
                '.mpg', '.mpe', '.avi', '.movie', '.mp4','webm','flv')

        self.AUDIO = ('.ra', '.aif', '.aiff', '.aifc',
                '.wav', '.au', '.snd', '.mp3', '.mp2')
        self.SOURCE_PATH = '.'
        self.DESTINATION_PATH = 'EXTRACTION_RESULTS'
        self.IMAGE_PATH = "IMAGE"
        self.VIDEO_PATH = "VIDEO"
        self.AUDIO_PATH = "AUDIO"
        self.DELETE_AFTER_COPY = False
        self.fl = []

    def create_dir(self,folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
    def create_tree_destination(self, root):
        self.create_dir(root)
        self.IMAGE_PATH = os.path.join(root, self.IMAGE_PATH)
        self.VIDEO_PATH = os.path.join(root, self.VIDEO_PATH)
        self.AUDIO_PATH = os.path.join(root, self.AUDIO_PATH)
        self.create_dir(self.IMAGE_PATH)
        self.create_dir(self.VIDEO_PATH)
        self.create_dir(self.AUDIO_PATH)

    def extract(self, extensions):
        for path, subdirs, files in os.walk(self.SOURCE_PATH):
            for name in files:
                if(not path  == self.DESTINATION_PATH):
                    print(os.path.join(path, name))
                    if(name.endswith(tuple(extensions))):
                        self.fl.append(os.path.join(path, name))

    def copy_extracted_files(self):
        for file in self.fl:
            try:
                print("copying: " + str(file) + " to :  " + str(self.DESTINATION_PATH))
                if file.endswith(tuple(self.IMAGE)):
                    shutil.copy2(file, self.IMAGE_PATH)
                if file.endswith(tuple(self.VIDEO)):
                    shutil.copy2(file, self.VIDEO_PATH)
                if file.endswith(tuple(self.AUDIO)):
                    shutil.copy2(file, self.AUDIO_PATH)
                # if user have shozen to delete files after copying
                if self.DELETE_AFTER_COPY:
                    print("Deleting file :  " + str(file))
                    os.remove(file)
            except Exception as ex:
                print("error while copying : " + str(ex))

    #DESTINATION_PATH = os.path.join('.',DESTINATION_PATH)
    #create_dir(DESTINATION_PATH)
    #extract(IMAGE)
    #copy_extracted_files()

    def start_extracting(self):
        if len(sys.argv) < 5:
            print(""" ! you have at least to enter 5 params such as 'copy images from ./example [ to /root/somefolder]' !""") 
        else:
            # convert entered params to lowercase strings
            for item in sys.argv:
                item = str(item).lower()
            #copy or cut
            if(sys.argv[1] == "copy"):
                self.DELETE_AFTER_COPY = False
            else: 
                self.DELETE_AFTER_COPY = True
            # copy IMAGE or VIDEO or AUDIO or ALL of them 
            entered_args = sys.argv[2].split(',')
            extensions = []
            if("image" in entered_args):
                extensions.extend(self.IMAGE)
            if("video" in entered_args):
                extensions.extend(self.VIDEO)
            if("audio" in entered_args):
                extensions.extend(self.AUDIO)
            # source path
            self.SOURCE_PATH = sys.argv[4]
            if not os.path.exists(self.SOURCE_PATH):
                sys.exit("error in 'from' argument  ! source path doesn't exist! ")
            # destination path if user specify
            if(len(sys.argv) == 7 ):
                self.DESTINATION_PATH = sys.argv[6]
            else: 
                self.DESTINATION_PATH = os.path.join('.', self.DESTINATION_PATH)
            
            self.create_tree_destination(self.DESTINATION_PATH)
            self.extract(extensions)
            self.copy_extracted_files()


type_extractor = Type_Extractor()
type_extractor.start_extracting()
