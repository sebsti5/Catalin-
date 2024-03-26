import os
import time
from datetime import datetime
from PIL import Image

class Info:
    """
    Gives you basic file information: File name, extension, created and update date and time
    """
    def fileInfo(self, localMachine, fileName):
        # Getting the file
        localFile = os.path.join(localMachine, fileName)

        # Check if the file does exist
        if not os.path.exists(localFile):
            print("File does not exist!")
        else:
            extension = os.path.splitext(fileName)[-1].upper().replace('.', '')
            last_modified = datetime.fromtimestamp(os.path.getmtime(localFile)).strftime('%Y-%m-%d %H:%M:%S')
            creation_time = datetime.fromtimestamp(os.path.getctime(localFile)).strftime('%Y-%m-%d %H:%M:%S')
            print(f"File Name: {os.path.basename(localFile)}\n" +
                  f"File Extension: {extension}\n" +
                  f"Last modified: {last_modified}\n" +
                  f"Date Created: {creation_time}")

class ImageFiles(Info):
    """
    Gives you basic file information: File name, extension, created and update date and time as well as image size (ex. 1024x860)
    """
    def fileInfo(self, localMachine, fileName):
        super().fileInfo(localMachine, fileName)
        # Image size
        image_path = os.path.join(localMachine, fileName)
        img = Image.open(image_path)
        width, height = img.size
        print(f"Image size: {width}x{height}")

class TextFiles(Info):
    """
    Gives you basic file information: File name, extension, created and update date and time, line count, word count, and character count
    """
    def fileInfo(self, localMachine, fileName):
        print("This is a text file")
        super().fileInfo(localMachine, fileName)
        # Line count, word count, and character count
        file_path = os.path.join(localMachine, fileName)

        # Line count
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
            print(f"Line count: {line_count}")

        # Word count
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()
            word_count = len(words)
            print(f"Word count: {word_count}")

        # Character count
        with open(file_path, 'r', encoding='utf-8') as file:
            char_count = sum(len(line) for line in file)
            print(f"Character count: {char_count}")

def main():
    # Folder paths
    CLOUD_PATH = "Y:\\Lucrari_OOP\\Lucrare 3\\Cloud"
    FOLDER_PATH = "Y:\\Lucrari_OOP\\Lucrare 3\\LocalMachine"

    # Initializing classes
    info = Info()
    info_text = TextFiles()
    info_image = ImageFiles()

    # fileInfo method calls
    info.fileInfo(FOLDER_PATH, "fileName")
    info_text.fileInfo(FOLDER_PATH, "textFileName")
    info_image.fileInfo(FOLDER_PATH, "imageFileName")

if __name__ == "__main__":
    main()
