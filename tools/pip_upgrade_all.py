import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call('sudo pip install --upgrade ' + dist.project_name, shell=True)
    