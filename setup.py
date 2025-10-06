from setuptools import find_packages, setup
from typing import List



def get_requirements()->List:
    """ 
    this function will return list of requirements
    """
    requirement_list:List[str]=[]

    """writing a code to read requirements.txt file and append each
     requirements in requiremnts_list variable."""
    
    return requirement_list

setup(
    name='sensor',
    version='0.0.1',
    author='shreyas',
    author_email='shreyasmahangade15@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()

)