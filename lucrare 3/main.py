import os
import hashlib
import time

# Clasa pentru gestionarea informațiilor despre fișiere
class Info:
    @staticmethod
    def fileInfo(folder_path, file_name):
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            last_modified = time.ctime(os.path.getmtime(file_path))
            print(f"File: {file_name}\nSize: {file_size} bytes\nLast Modified: {last_modified}")
        else:
            print("File not found.")

# Clase pentru tipurile specifice de fișiere
class TextFiles(Info):
    pass

class ImageFiles(Info):
    pass

class ProgramFiles(Info):
    pass

# Clasa pentru monitorizarea folderelor
class FolderMonitor:
    @staticmethod
    def compareFolders(local_path, cloud_path, should_commit):
        # Cod pentru compararea folderelor locale și de cloud
        pass

# Clasa pentru comiterea schimbărilor
class Commit:
    @staticmethod
    def commit(local_path, cloud_path):
        # Cod pentru comiterea schimbărilor din folderul local în cel de cloud
        pass

# Funcția principală
def main():
    # Definirea calelor către foldere
    CLOUD_PATH = "Y:\\Lucrari_OOP\\Lucrare 3\\Cloud" 
    FOLDER_PATH = "Y:\\Lucrari_OOP\\Lucrare 3\\LocalMachine" 

    # Inițializarea obiectelor pentru gestionarea informațiilor
    info = Info()
    info_text = TextFiles()
    info_image = ImageFiles()
    info_program = ProgramFiles()

    # Funcția pentru planificarea execuției
    def scheduler():
        while True:
            try:
                FolderMonitor.compareFolders(FOLDER_PATH, CLOUD_PATH, True)
            except Exception as e:
                raise RuntimeError(e)
            time.sleep(5)
    scheduler()

    # Interfața de linie de comandă interactivă
    while True:
        print("""
                GIT CLI
                    1. Commit
                    2. Info <fileName.extension>
                    3. Status
                    4. Quit
                Please choose one of the above options:")

        choice = input().strip()

        if choice == '1':
            Commit.commit(FOLDER_PATH, CLOUD_PATH)
        elif choice == '2':
            file_name = input("Please enter a file name: ").strip()
            extension = file_name.split('.')[-1] if '.' in file_name else "NONE"
            if extension == "txt":
                info_text.fileInfo(FOLDER_PATH, file_name)
            elif extension in ["jpeg", "jpg", "png"]:
                info_image.fileInfo(FOLDER_PATH, file_name)
            elif extension == "java":
                info_program.fileInfo(FOLDER_PATH, file_name)
                print("May not be 100% accurate due to certain limitations")
            else:
                info.fileInfo(FOLDER_PATH, file_name)
        elif choice == '3':
            FolderMonitor.compareFolders(FOLDER_PATH, CLOUD_PATH, False)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

              