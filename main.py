from pytube import YouTube
link = input("Enter the video url here -> ")
y_tube = YouTube(link)
print(f'Video title -> {y_tube.title}')
stream = y_tube.streams.filter(progressive=True)
video = list(enumerate(stream))
for i in video:
    print(i)
print("-----------------------------------------------------")
index = int(input("Enter the index of the desired stream -> "))
stream[index].download()
print("sucess")