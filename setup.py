from setuptools import setup
from typing import List


DESCRIPTION="Project Description"
REQUIRENMENT_FILE_NAME="requirements.txt"

def get_requirenment_list()->List[str]:
    """
    Description : This funtion going to list requirenment from requirenment file

    return this will retun the name of lib required in requirenment.txt
    """
    with open(REQUIRENMENT_FILE_NAME) as requirenment_file:
        return requirenment_file.readline()



setup(
    name="HousingPredictor",
    version="0.0.1",
    author="Deepak",
    description=DESCRIPTION,
    packages=["housing"],
    install_requireed=get_requirenment_list()
)