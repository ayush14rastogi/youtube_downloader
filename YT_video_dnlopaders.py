from pytube import YouTube

# read values from command line & resolution
a = input("Enter the Youtube URL : ")
yt = YouTube(a)

Save_path = "C:/personal/v"  # to_do
#yt = YouTube('https://www.youtube.com/watch?v=_uLNGWB_IgQ')
videos = yt.get_videos()

try:
    # object creation using YouTube which was imported in the beginning
#    yt = YouTube('https://www.youtube.com/watch?v=_uLNGWB_IgQ')
    yt = YouTube(a)
    filename = yt.filename
    print("The name of video is : ", filename)
    videos = yt.get_videos()
    for v in videos:
        # print(v.resolution,"",v.extension,"",v.profile)
        # DOWNLOAD VIDEO1
        # print(type(v.resolution),type(str(yt.filter('720p'))))
        #print(v)
        try:
            # if v.resolution == str(yt.filter('720p')) and v.extension == yt.filter('mp4'):
            if v.profile == 'High':
                v.download(Save_path)
                print("Video download successfully to -->", Save_path)
        except:
            print("Error while download check you Download section in code")
except:
    print("Connection Error")  # to handle exception

