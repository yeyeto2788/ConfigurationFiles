
## Issue list:
  * **[Cloning a GitHub repository](#Cloning-a-GitHub-repository)**
  * **[Color on REPL or terminal output from python color](#Color-on-REPL/Terminal)**
  * **[Get time of python script execution](Get-time-of-python-script-execution)**
  * **[Upgrade pip installed packages](Upgrade-all-pip-installed-packages)**
  * **[Clone all repositories from a User](Clone-all-repositories-from-a-User)**
  * **[]()**

###  Cloning a GitHub repository

When cloning a repository from GitHub the following error shows up:
**ERROR**
```
fatal: unable to access 'https://github.com/<user>/<repository>.git/': server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: nonep
```

* **SOLUTION 1**

  `sudo update-ca-certificates`

* **SOLUTION 2**

  If previous solution didn't work follow the steps below
  * Configure your time zone:
    `sudo dpkg-reconfigure tzdata`
    * Select you time zone you want to set for the system
  * Install `ntp`
    `sudo apt-get install -y ntp`
  * Check if ntp is working by:
    `ntpq -P` or `sudo ntpq -P` it should show something like this:
    ```
      remote           refid      st t when poll reach   delay   offset  jitter
      ==============================================================================
      ntp.redimadrid. .INIT.          16 u    -   64    0    0.000    0.000   0.000
      x.ns.gin.ntt.ne .INIT.          16 u    -   64    0    0.000    0.000   0.000
      85.254.217.235  .INIT.          16 u    -   64    0    0.000    0.000   0.000
    ```
    **NOTE:** Take into account I have setup Spain as my time zone.

    If this doesn't show anything or you get something like `No association ID's returned` then type `dpkg-reconfigure ntp` or `sudo dpkg-reconfigure ntp`
  * Add current time to system by:
    `date -s "22 AUG 2017 13:10:00"`
 
* **SOLUTION 3**
  
  `sudo apt-get install ssl-cert`

###  Color on REPL/Terminal:

This is to set the color on the output of the code. Take into account that for Bash or Shell the `\x1b` should be replace with `\033`

For more [info](https://en.wikipedia.org/wiki/ANSI_escape_code)

* **SOLUTION 1**

  Declare the variables and then use them on the code:
  
  **Variables:**

  ```python
  Color = {"White": "\x1b[0m",
  "Blue": "\x1b[01;34m",
  "Cyan": "\x1b[01;36m",
  "Green": "\x1b[01;32m",
  "Red": "\x1b[01;05;37;41m"}
  ```
  **How to use it on the code:**
  
  Just need to add the color plus the text you want to print.
  ```
  print (Blue + "Text to print..")
  ```
* **SOLUTION 2**

  Declare the variables/class and then use them on the code:
  ```python
  class bcolors:
    HEADER = '\x1b[95m'
    BLUE = '\x1b[94m'
    GREEN = '\x1b[92m'
    WARNING = '\x1b[93m'
    FAIL = '\x1b[91m'
    ENDC = '\x1b[0m'
    BOLD = '\x1b[1m'
    UNDERLINE = '\x1b[4m'
  ```

  **How to use it on the code:**
  
  Just need to add the color plus the text you want to print.
  ```
  print (bcolors.WARNING + "Warning text to print..")
  ```

### Get time of python script execution

In order to get the time of execution of a python script you should use the following:

* **SOLUTION 1**

  If you now that the program would be executed within minutes this will give you the seconds

  ```python
  import time
  start_time = time.time()
  main()
  print("--- %s seconds ---" % (time.time() - start_time))
  ```

* **SOLUTION 2**

  If you want to have minutes and so on this will also help you:
  
  ```python
  from time import gmtime, strftime
  StartTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  main()
  EndTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print(StartTime + ">>>" + EndTime)
  ```
  
### Upgrade all pip installed packages
  
  * **SOLUTION 1**
  
  In order to have all packages updated first we need to collect all packages on a `.txt` file by:
  ```
  pip list installed > requirements.txt
  ```
  
  then let's update them by:
  ```
  pip install -r requirements.txt --upgrade
  ```

### Clone all repositories from a User
  
  * **SOLUTION 1**
  ```
  USER=<GitHubUser>; curl "https://api.github.com/users/$USER/repos?per_page=1000" | grep -w clone_url | grep -o '[^"]\+://.\+.git' | xargs -L1 git clone
  ```
  
### Title
  
  * **SOLUTION 1**

