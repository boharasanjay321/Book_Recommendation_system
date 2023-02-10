from setuptools import find_packages,setup
REQUIREMENT_FILE_NAME="requirements.txt"
HYPEN_E_DOT="-e"
def get_requirements()->[str]:

    with open(REQUIREMENT_FILE_NAME) as requirements_file:
       requirement_list= requirements_file.readlines()
       requirement_list=[requirement_name.repalce("\n","") for requirement_name in requirement_list]
    if HYPEN_E_DOT in requirement_list:
        requirement_list.remove(HYPEN_E_DOT)

    return requirement_list

    setup(
     name="brs",  
     version="0.0.2",
     author='sanjay',
     package=find_packages(),
     install_requires=get_requirements(),

    )