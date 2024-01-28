from setuptools import find_packages, setup
from typing import List

E_DOT = '-e .'


def get_package_info(file_path:str)->List[str]:
    ''' generate the list of package to install.
    '''
    packages_ = []
    with open(file_path) as file:
        packages_ = file.readlines()
        # replacing \n with ''
        packages_ = [pkg_name.replace('\n', '') for pkg_name in packages_]
        if E_DOT in packages_:
            packages_.remove(E_DOT)
    return packages_


setup(
    name="ML-etz",
    version='0.0.1',
    author="Akvi",
    author_email="pygojs@gmail.com",
    packages=find_packages(),
    install_requires=get_package_info(file_path='./requirements.txt')
)