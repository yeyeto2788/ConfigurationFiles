# Configuration Files

Repository to host some files for Troubleshooting and Python PIP requirements

* **`RequirementsPIP.txt`**

  Modules to install on machine with python by typing `pip install -r requirements.txt`

* **`SortRequirementPIP.py`**

  Will sort alphabetically the modules I normally install on machines. The simple way to use it is by going to the terminal window and tiping:
  
  ```
  python SortRequirementPIP.py -i NameOfPipFile.txt
  ```
  
  Take into account that I reformat the code to take the input file directly from the command line instead of harcoding the name of the file on the script.

* **`Troubleshooting.md`**

  Some problems I found during executing scripts or looking for information.
  
* **`ReleaseZIP.py`**

  Make a ZIP file for releases, taking the files on a folder and adding them into the ZIP. It can exclude files and directories.
