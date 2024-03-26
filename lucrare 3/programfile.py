class ProgramFiles(Info):
    def fileInfo(self, localMachine, fileName):
        super().fileInfo(localMachine, fileName)

        # Get the line count
        file_path = os.path.join(localMachine, fileName)
        line_count = 0
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_count += 1
        print("Line count:", line_count)

        # Get the class count (May be inaccurate due to certain limitations)
        class_count = 0
        method_count = 0
        class_pattern = re.compile(r'class\s+([A-Z][\w]*)')
        method_pattern = re.compile(r'(?:(public|private|protected)\s+)?(?:static\s+)?\s*(\([\w,.\s\[\]]*\))\s+([A-Za-z_][A-Za-z0-9_]*)\s*(\(.*\))?\s*')

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if class_pattern.search(line):
                        class_count += 1
                    if method_pattern.search(line):
                        method_count += 1
        except Exception as e:
            raise RuntimeError(e)

        print("Number of classes:", class_count)
        print("Number of methods:", method_count)
