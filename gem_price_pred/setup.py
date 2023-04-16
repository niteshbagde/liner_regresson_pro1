from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path):
    requirements= list()
    with open(file_path) as f:
        req = f.readlines()
        for i in req:
            if HYPEN_E_DOT == i:
                pass
            else:
                requirements.append(i.replace("\n",""))
    return requirements

""" 
OR 

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

"""


setup(
    name='Regression_project',
    version='0.0.1',
    description='This package is for housing price detection in regression ML model',
    author='Aaron17',
    author_email='aaronnb17@gmail.com',
    install_requires=get_requirements(r"D:\ineuron\class demo\Regression project\gem_price_pred\requirements.txt"),
    packages=find_packages()             
    )



"""
2 ways to execute setup file

pip install -r requirements.txt [targest only entry poin as -e . and create few entries ]

and other is  

python setup.py install  [complete execution and file creation]

"""


