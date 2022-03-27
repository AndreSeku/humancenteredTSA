import os
import setuptools

# Load requirements.txt and readme ..
# dir_repo = os.path.abspath(os.path.dirname(__file__))
# # read the contents of REQUIREMENTS file
# with open(os.path.join(dir_repo, "requirements.txt"), "r") as f:
#     requirements = f.read().splitlines()
# # read the contents of README file
# with open(os.path.join(dir_repo, "README.md"), encoding="utf-8") as f:
#     readme = f.read()

setuptools.setup(
    name = 'hctsa',
    packages = setuptools.find_packages(),

    # add for requirements
    # python_requires=">=3.6", # TODO: check if this is needed
    # install_requires=requirements, # TODO: requirements.txt
    
    version = '0.1.0',  # Ideally should be same as your GitHub release tag version
    description = 'Human-Centered TimeSeries Analysis Package',
    author = 'Andre Sekulla',
    author_email = 'andreseku@gmail.com',
    url = 'https://github.com/AndreSeku/humancenteredTSA',
    download_url = 'https://github.com/AndreSeku/humancenteredTSA/archive/refs/tags/0.1.0.zip',
    keywords = ['timeseries', 'analysis', 'hcml'],

    # add for description
    # long_description=readme,
    # long_description_content_type="text/markdown",

    classifiers = [],
)