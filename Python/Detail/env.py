# pip is package manager for python

## pip3 --version
## pip3 list # to list all the packages installed in your environment
## pip3 install package_name # to install a package
## pip3 uninstall package_name # to uninstall a package
## pip3 show package_name # to show details about a package
## pip3 install --upgrade package_name # to upgrade a package
## pip3 freeze > requirements.txt # to create a requirements file with all the installed packages and their versions
## pip3 install -r requirements.txt # to install all the packages listed in the requirements file
## pip3 freeze # to list all the installed packages and their versions in the current environment


## Python virtual environments are a way to create isolated environments for your Python projects. This allows you to manage dependencies 
# and avoid conflicts between different projects.

# python3 -m venv myenv # to create a virtual environment named myenv
# source myenv/bin/activate # to activate the virtual environment
# deactivate # to deactivate the virtual environment


# pip3 install pipenv # to install pipenv, a tool for managing virtual environments and dependencies
# pipenv install package_name # to install a package in the virtual environment
# pipenv shell # to activate the virtual environment created by pipenv
# pipenv lock # to create a Pipfile.lock file with the exact versions of the installed packages
# pipenv --venv # to show the path to the virtual environment created by pipenv
# pipenv shell # to activate the virtual environment created by pipenv
