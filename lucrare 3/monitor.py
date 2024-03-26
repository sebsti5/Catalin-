import os
import hashlib

class FolderMonitor:
    @staticmethod
    def compareFolders(localMachine, cloud, isLoop):
        source = os.listdir(localMachine)
        destination = os.listdir(cloud)

        # Check if the folders exist
        if not os.path.exists(localMachine) or not os.path.exists(cloud):
            print("One or both folders can't be found or don't exist")
            return

        # Loop through the localMachine files
        for localFileName in source:
            localFile = os.path.join(localMachine, localFileName)
            localChecksum = FolderMonitor.getMD5Checksum(localFile)
            cloudFile = os.path.join(cloud, localFileName)

            # Check if file exists in Cloud folder
            if not os.path.exists(cloudFile):
                print(localFileName + " - new")
            else:
                try:
                    cloudChecksum = FolderMonitor.getMD5Checksum(cloudFile)
                    if localChecksum == cloudChecksum and not isLoop:
                        print(localFileName + " - unchanged")
                    elif localChecksum != cloudChecksum:
                        print(localFileName + " - changed")
                except Exception as e:
                    raise RuntimeError(e)

        # Loop through cloud files (to find new files)
        for cloudFileName in destination:
            cloudFile = os.path.join(cloud, cloudFileName)
            localFile = os.path.join(localMachine, cloudFileName)

            # Check if the file doesn't exist in localMachine
            if not os.path.exists(localFile):
                print(cloudFileName + " - deleted")

    @staticmethod
    def getMD5Checksum(file):
        try:
            with open(file, "rb") as f:
                md5 = hashlib.md5()
                while chunk := f.read(8192):
                    md5.update(chunk)
                return md5.hexdigest()
        except Exception as e:
            raise RuntimeError(e)

def main():
    localMachine = "path/to/local/machine"
    cloud = "path/to/cloud"
    FolderMonitor.compareFolders(localMachine, cloud, False)

if __name__ == "__main__":
    main()
