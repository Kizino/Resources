# Create Virtual Environment
python3 -m venv venv
virtualenv -p python3 venv

# Activate Virtual Environment
# On Windows run:
venv\Scripts\activate.bat
# On Unix or MacOS:
source venv/bin/activate

# Close Virtual Environment
deactivate

# Create requirement.txt
pip3 free > requirement.txt

# Install libraries from requirement.txt
python3 -m pip3 install -r requirement.txt