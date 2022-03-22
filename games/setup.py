import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MOT-Bot-Games", # Replace with your own username
    version="1.0.1",
    author="Lea-S, NatiBckr, Fulachs, Nowo",
    author_email="nm1w6jrgrw5z@blurme.net",
    description="Games of the MOT Bot",
    long_description= long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/NoWo2000/MOT-Multi-Functional-Bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)