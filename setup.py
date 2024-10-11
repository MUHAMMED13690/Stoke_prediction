from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the given file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Remove '-e .' if it's present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
setup(
    name="Stok Prediction",
    version="0.1",
    description="This project is a stock prediction application that leverages data science techniques to analyze market trends and     forecast future stock prices.",
    author="MUHAMMED SUNAIN",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author_email="msaban371@gmail.com"
)

