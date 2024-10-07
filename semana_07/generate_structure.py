import sys
import os

class GenerateStructure:
    def __init__(self, typeStructure, projectName):
        self.projectName = projectName
        self.typeStructure = typeStructure
        self.path = f"{os.getcwd()}/{self.projectName}/"

    def create_directory(self, path):
        os.makedirs(path, exist_ok=True)

    def create_file(self, path, content=""):
        with open(path, "w") as file:
            file.write(content)

    def handleType(self):
        if self.typeStructure == "--CRUD":
            self.generateCRUDStructure()
        elif self.typeStructure == "--API":
            self.generateAPIStructure()

    def generateCRUDStructure(self):
        print("> Generating CRUD structure...")
        self.create_directory(self.path)

        # hnndle folder structure
        folders = [
            "src/", 
            "src/models", 
            "src/views", 
            "src/controllers"
        ]

        for folder in folders:
            self.create_directory(f"{self.path}/{folder}")

        # handle files
        files = [
            "README.md",
            ".gitignore",
            ".env",
            "app.py", 
            "src/models/__init__.py", 
            "src/views/__init__.py", 
            "src/controllers/__init__.py"
        ]
        for file in files:
            self.create_file(f"{self.path}{file}")

        print("> CRUD structure generated successfully!")

    def generateAPIStructure(self):
        print("> Generating API structure...")
        self.create_directory(self.path)

        # handle folder structure
        folders = [
            "src/", 
            "src/api", 
            "src/api/routes",
            "src/api/middlewares",
            "src/api/validators",
            "src/core",
            "src/db",
            "src/db/models",
            "src/services",
            "tests"
        ]

        for folder in folders:
            self.create_directory(f"{self.path}/{folder}")

        # handle files
        files = [
            "README.md",
            ".gitignore",
            ".env",
            "app.py", 
        ]

        for file in files:
            self.create_file(f"{self.path}{file}")

        print("> API structure generated successfully!") 

def main():
    if (len(sys.argv) != 3):
        print("> Please provide type structure: python generate_structure.py <type --CRUD | --API> <projectName>")
        print("> Args received:", sys.argv)
        os._exit(1)
            
    typeStructure = sys.argv[1]
    projectName = sys.argv[2]

    generateStructure = GenerateStructure(typeStructure, projectName)
    generateStructure.handleType()

if __name__ == "__main__":
    main()
