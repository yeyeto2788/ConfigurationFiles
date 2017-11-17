#!/usr/bin/env python

"""
IMPORT MODULES NEEDED
"""
import os
import re
import zipfile


class CreateZIPFile:

    def __init__(self, FolderToZIP, ExcludedFiles, ExcludedDirectories):
        """
        Initialize the class by doing some check and executing main functions of the code.
        
        Args:
            FolderToZIP: Path of the folder to be pack into a ZIP file.
            ExcludedFiles: Tuple of files extension to exclude.
            ExcludedDirectories: Tuple of directories to exclude.
        """
        if self.checkDir(FolderToZIP):
            self.checkReleaseFolder(FolderToZIP)
            zipName = 'Release_V%s.zip' % self.getNextRelease(os.path.join(FolderToZIP, 'Releases'))
            print("Creating the ZIP folder...")
            zipFolder = zipfile.ZipFile(os.path.join(FolderToZIP, 'Releases', zipName), 'w', zipfile.ZIP_DEFLATED)
            self.writeToZIP(os.path.join(FolderToZIP), zipFolder, ExcludedFiles, ExcludedDirectories)
            zipFolder.close()
            print("The ZIP %s file was created successfully...." % zipName)
        else:
            print("Seems like the folder does not exist.\nTry again...")

    def checkDir(self, FolderToCheck):
        """
        Checks whether the folder to pack exists or not.
        
        Args:
            FolderToCheck: Path of the folder to check and then pack into the ZIP.

        Returns:
                Boolean depending if the directory exists or not.
        """
        if os.path.exists(FolderToCheck):
            return True
        else:
            return False

    def checkReleaseFolder(self, FolderToZIP):
        """
        This functions is needed since the zipfile module seems not to be creating a containing folder by default,
        so it checks if the folder 'Releases' exists, if not it will create the folder.
        Args:
            FolderToZIP: Path of the folder to check and then pack into the ZIP.

        Returns:

        """
        if not os.path.exists(os.path.join(FolderToZIP, 'Releases')):
            os.mkdir(os.path.join(FolderToZIP, 'Releases'))
            print("Releases folder created!")

    def getNextRelease(self, directory):
        """
        From the 'Releases' folder it will look the last created ZIP file and it will get the last number of the release
        plus one.
        
        Args:
            directory: Path plus 'Releases' folder where the ZIP files are.

        Returns:
                String with the next Release number for the file naming.
        """
        files = os.listdir(directory)
        lastRelease = 0
        for file in files:
            if file.endswith('.zip'):
                fileName = re.match(r"([a-zA-Z\_]+)([0-9]+)", str(file).rstrip('.zip'))
                # print(fileName.group(1)) will look for the letters
                lastRelease = fileName.group(2)
        return '%0.3d' % (int(lastRelease) + 1)

    def writeToZIP(self, containerFolder, ziph, filesToExclude, DirToExclude):
        """
        This is the core function where it adds the files into the ZIP file, excluding the files and directories given 
        by parameters.
        
        Args:
            containerFolder: Path of the folder to ZIP.
            ziph: zipfile object.
            filesToExclude: Tuple of files extensions to exclude.
            DirToExclude: Tuple of directories to exclude.

        Returns:

        """
        containerBase = os.path.basename(containerFolder)
        for root, dirs, files in os.walk(containerFolder):
            for file in files:
                if root.endswith(DirToExclude):
                    break
                else:
                    print(("*" * 10) + os.path.realpath(root))
                    if not file.endswith(filesToExclude):
                        newContainer = os.path.basename(root)
                        if newContainer == containerBase:
                            ziph.write(os.path.join(root, file), file)
                            print("Adding %s" % file)
                        else:
                            ziph.write(os.path.join(root, file), os.path.join(newContainer, file))
                            print("Adding %s" % os.path.join(newContainer, file))


"""
EXECUTE THE CODE
"""

DirsExcluded = ('DeleteBackup')
FilesExcluded = ('.jpg', '.md', '.zip', '.png')
DirToZip = input("What directory you want make the release for?\n>>>")
CreateZIPFile(DirToZip, FilesExcluded, DirsExcluded)




