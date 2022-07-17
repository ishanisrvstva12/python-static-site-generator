from pathlib import Path
from typing import List
import shutil

class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        if extension in self.extensions:
            return extension
            print("Extension is in the class variable")
        else:
            print("Extension is not in the class variable")

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / Path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        Parser.copy(path, source, dest)


