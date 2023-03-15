## The script will look for all the installed packages and attempt to upgrade to newest version

import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]

call("pip install --upgrade " + ' '.join(packages), shell=True)
