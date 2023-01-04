import setuptools
import pathlib

def File_Read():
    if not (pathlib.Path("README.md")).exists():
        with open("README.md", "w+", encoding="utf-8") as file:
            with open((pathlib.Path.cwd()/"docs/README.md"), "r", encoding="utf-8") as source:
                file.write(source.read())
    with open("README.md", "r", encoding="utf-8") as file:
        return file.read()

def Main():
    setuptools.setup(
            name="Technology-Note",
            version="0.0.3",
            author="CoolPlayLin",
            author_email="help@api-coolplaylin.eu.org",
            description="Learn the techniques developed in Python",
            long_description=File_Read(),
            long_description_content_type='text/markdown',
            packages=setuptools.find_packages(),
            project_urls={
                "Bug Report": "https://github.com/CoolPlayLin/Technology-Note/issues/new",
                "Feature Request": "https://github.com/CoolPlayLin/Technology-Note/issues/new"
            },
            download_url="https://github.com/CoolPlayLin/Technology-Note/releases",
            url="https://github.com/CoolPlayLin/Technology-Note/",
            classifiers=[
                "Development Status :: 2 - Pre-Alpha",
                "Natural Language :: English",
                "Programming Language :: Python :: 3",
                "Topic :: Software Development :: Libraries :: Python Modules",
                "License :: OSI Approved :: MIT License"
            ]
        )

if __name__ == "__main__":
    Main()