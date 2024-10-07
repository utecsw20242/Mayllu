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

        # handle folder structure
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
            "src/controllers/__init__.py",
            "src/controllers/routes.py"
        ]
        for file in files:
            self.create_file(f"{self.path}{file}")
        
        # use requirements.txt for handle dependencies
        self.create_file(f"{self.path}requirements.txt", self.get_crud_requirements())
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
            "src/api/routes/hello_route.py"
        ]
        for file in files:
            if file == "app.py":
                self.create_file(f"{self.path}{file}", self.get_api_app_content())
                # add basic content for API app (balbuena said that app must have a hello route)
            elif file == "src/api/routes/hello_route.py":
                self.create_file(f"{self.path}{file}", self.get_api_hello_route_content())
            else:
                self.create_file(f"{self.path}{file}")
        
        self.create_file(f"{self.path}requirements.txt", self.get_api_requirements())
        print("> API structure generated successfully!")

    def get_api_app_content(self):
        return """
        from fastapi import FastAPI
        from src.api.routes.hello_route import router as hello_router

        app = FastAPI()
        app.include_router(hello_router)
        
        if __name__ == "__main__":
            import uvicorn
            uvicorn.run(app, host="0.0.0.0", port=8000)
        """

    def get_api_hello_route_content(self):
        return """
        from fastapi import APIRouter

        router = APIRouter()

        @router.get("/hello")
        async def hello():
            return {"message": "Hello from Devies Inc API!"}
        """

    def get_crud_requirements(self):
        return """
        Flask==2.0.1
        """

    def get_api_requirements(self):
        return """
        fastapi==0.68.0
        uvicorn==0.15.0
        """

def main():
    if (len(sys.argv) != 3):
        print("> Please provide type structure: python generate_structure.py <--CRUD|--API> <project_name>")
        print("> Args received:", sys.argv)
        os._exit(1)

    typeStructure = sys.argv[1]
    projectName = sys.argv[2]
    generateStructure = GenerateStructure(typeStructure, projectName)
    generateStructure.handleType()

if __name__ == "__main__":
    main()
