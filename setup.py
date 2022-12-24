import setuptools

with open("README.md", "r", encoding="utf-8") as read:
    README = read.read()

setuptools.setup(
        name="Technology-Note",
        version="0.0.1",
        author="CoolPlayLin",
        author_email="help@api-coolplaylin.eu.org",
        description="Learn the techniques developed in Python",
        long_description=README,
        long_description_content_type='text/markdown',
        packages=setuptools.find_packages(),
        license='GPL',
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