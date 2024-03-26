import os
import shutil
from datetime import datetime

class Commit(FolderMonitor):
    @staticmethod
    def commit(source, destination):
        # Update Snapshot Time and store it inside a file
        snapshot_time = datetime.now()
        print("Snapshot created at:", snapshot_time)
        with open("CommitFile.txt", "w") as commit_file:
            commit_file.write(str(snapshot_time))

        # Define locations for the LOCAL_FOLDER and CLOUD_FOLDER
        local_machine = source
        cloud = destination

        # Copy directory structure recursively
        for root, dirs, files in os.walk(local_machine):
            for dir_name in dirs:
                source_dir = os.path.join(root, dir_name)
                target_dir = os.path.join(cloud, os.path.relpath(source_dir, local_machine))
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
            for file_name in files:
                source_file = os.path.join(root, file_name)
                target_file = os.path.join(cloud, os.path.relpath(source_file, local_machine))
                shutil.copy2(source_file, target_file)

        print("Commit successful!")

def main():
    source_folder = "path/to/local/machine"
    destination_folder = "path/to/cloud"
    Commit.commit(source_folder, destination_folder)

if __name__ == "__main__":
    main()
