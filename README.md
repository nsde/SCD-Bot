# Installation
Execute in root dir: `pip install -r requirements.txt` to install the needed libaries.
## Fix errors:
If you get "ERROR: Could not build wheels for multidict, yarl which use PEP 517 and cannot be installed directly":
- __(not recommended)__ Downgrade to Python 3.8.6 
- __(not recommended)__ Download the "cp39" (for Python 3.9)-Versions of:

    -**lfd.uci.edu/~gohlke/pythonlibs/#yarl**

    -**lfd.uci.edu/~gohlke/pythonlibs/#multidict**

    remember to choose the right win_amd64/win32-Version.

    And do `pip install `**FILENAME** (e.g *yarl-1.6.3-cp39-cp39-win_amd64.whl*)` --force-reinstall` in the directory you downloaded the files for **both the two files**. 

    Then try `pip install discord.py` or `pip install discord` again.

- __(recommended/best way)__ install **https://visualstudio.microsoft.com/visual-cpp-build-tools/** (this worked for me)

- alternatively, see: https://stackoverflow.com/a/64861883

Run the "main"-python file in /lib and follow the instructions and you are *good to go*!

# Security note
This section will inform you about how you can safe your bot against black hat hackers/exploits etc.

Please go to the Discord Developer Portal `/applications/<application id>/bot` and scroll down to the section "Bot permissions". From there, tick all **needed and used** permissions. Do NOT tick "Administrator" - this will allow the bot to do almost everything on your server. And, do NOT tick unused permissions.