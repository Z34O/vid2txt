import cv2
from PIL import Image
import os
import math

while True:
    choice = input("> ")

    if choice == "convert":
        videonm = input("Video name (without file extension): ")
        video = cv2.VideoCapture(videonm + ".mp4")
        os.mkdir(videonm)
        count = 0

        print("Extracting frames...")
        while video.isOpened():
            ret, frame = video.read()
            if ret:
                cv2.imwrite(os.path.join(videonm, str(count) + "orig.jpg"), frame)
                count += 1
            else:
                break

        print("Done! " + str(count) + " frames in total")

        rep = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
        sensitivity = len(rep)

        os.chdir(videonm)
        resize = input("Resize (w, h): ").split(", ")

        print("Converting frames to ASCII...")
        for filenum in range(0, count+1):
            fileascii = Image.open(str(filenum) + "orig.jpg").convert("L")
            fileascii = fileascii.resize((int(resize[0]), int(resize[1]))) if resize[0].count(",") == 1 else fileascii
            w, h = fileascii.size

            file = open(str(filenum) + ".txt", "w")
            for heightrun in range(0, h):
                for widthrun in range(0, w):
                    shade = math.floor(fileascii.getpixel((widthrun, heightrun)) / sensitivity)
                    file.write(rep[shade])
                file.write("\n")
            file.close()

            os.remove(str(filenum) + "orig.jpg")

        print("Done converting!")
        os.chdir("..")

    elif choice == "play":
        playvid = input("asv name: ")
        frames = input("Frames to play: ")

        os.chdir(playvid)

        for frame in range(0, int(frames)):
            file = open(str(frame) + ".txt", "r")
            print(file.read())
            os.system('clear')

        os.chdir('..')

    elif choice == "exit":
        break
