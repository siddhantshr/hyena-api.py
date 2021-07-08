from setuptools import setup, find_packages
requirements = []

from hyena.__init__ import __version__, __author__, __license__

with open('requirements.txt', 'r', encoding="utf-8") as f:
    requirements = [x.split("==", 1)[0] for x in f.read().splitlines()]

with open('./README.md', 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hyena-api.py",
    version=__version__,
    author=__author__,
    author_email="31.siddhant.sharma@gmail.com",
    description="A wrapper for the Hyena API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=requirements,
    keywords=['wrapper', 'api-wrapper', 'hyena-api', 'python'],
    url="https://github.com/AHiddenDonut/hyena-api.py",
    license=__license__,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Topic :: Software Development :: Build Tools",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)
