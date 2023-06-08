import setuptools
from setuptools import find_packages,setup
from typing import List

# It helps us to reed the README.md file when it is deploy as a pypy package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #it helps to read the package name one by one from requirements.txt
        requirements=[req.replace("\n","") for req in requirements]  # it helps to avoid the "/n" comes from readline function 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)   #it automatically connect the requirements file
            
        return requirements
    
    
__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "ajitkumarpatel1"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "1ajitkumarpatel@gmail.com"
DESCRIPTION = "A small python package for NLP app"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= DESCRIPTION,
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements('requirements.txt')
)