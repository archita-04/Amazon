from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_list: List[str] = []

    with open("requirements.txt") as file:
        requirement_list = file.readlines()
        requirement_list = [req.replace("\n", "") for req in requirement_list]

        if "-e ." in requirement_list:
            requirement_list.remove("-e .")

    return requirement_list


setup(
    name="flipkart",
    version="0.0.1",
    author="Archita",
    author_email="imarchita04@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
