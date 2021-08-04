from pytube import YouTube as PY
import time
while True:
    ask = input("Do you want to download Videos(y/n): ")
    if ask.lower() == "y":
        try:
            url = input("Enter the youtube video url")
            video = PY(url)
            stream = video.streams.get_highest_resolution()
            #video.register_on_complete_callback(r"C:\Users\Jayant\OneDrive\Desktop")
            video.register_on_progress_callback(stream)
            stream.download()
        except:
            print("Error Occured, Trying again in 3 secs")
            time.sleep(3)
            
    elif ask.lower() =="n":
        break
    else:
        continue
