from os import path

from setuptools import find_packages, setup


def find_requirements(filename_list):
    all_requirements = []
    for filename in filename_list:
        with open(path.join(path.dirname(__file__), filename)) as f:
            requirements = f.read().splitlines()
            f.close()
        reqs = [r for r in requirements if '.txt' not in r]
        all_requirements.extend(reqs)
    return all_requirements


REQUIREMENTS_FILE = 'requirements.txt'


setup(
    name='dungeon-api',
    packages=find_packages(exclude=['tests']),
    scripts=['main.py'],
    use_scm_version=True,
    install_requires=find_requirements([REQUIREMENTS_FILE]),
    include_package_data=True
)
