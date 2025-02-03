from setuptools import setup, find_packages

setup(
    name="ci_cd_project",
    version="0.1.0",
    # Les sources se trouvent dans src/
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
