# MIT License
#
# Copyright (c) 2021 Jean-Jacques François Reibel
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import platform
import subprocess
# By JJ Reibel, using Python 3.10
# Newer versions of Python, at the time of writing,
# intend to replace os, at least in part, with subprocess

# Get Computer Name
node = str(platform.node())
# Get Machine
machine = str(platform.machine())
# Get Processor
processor = str(platform.processor())
# Get OS
system = str(platform.system())
# Get OS Release
release = str(platform.release())
# Get OS Version
platform = str(platform.platform())

print("##########################################################")
print("### INFORMATION ##########################################")
print("##########################################################")
print()
print("Computer Name: \t" + node)
print("Machine: \t" + machine)
print("Processor: \t" + processor)
print("System: \t" + system)
print("Platform: \t" + platform)
print("Release: \t" + release)

if system == "Windows":
    # Get and display processes in Windows
    outputProcesses = os.popen('wmic process get description, processid').read()
    print()
    print("##########################################################")
    print("### PROCESSES ############################################")
    print("##########################################################")
    print(outputProcesses)
    print("##########################################################")
    print("### FILES ################################################")
    print("##########################################################")
    # Get and display local files in Windows
    outputFiles = os.popen('dir').read()
    print(outputFiles)
    print()
    print("##########################################################")
elif system == "Java":
    pass
else:
    # Get and display running processes in Linux or Unix systems
    outputProcesses = os.popen('ps ax').read()
    print()
    print("##########################################################")
    print("### PROCESSES ############################################")
    print("##########################################################")
    print(outputProcesses)
    print()
    print("##########################################################")

    # Get and display running apps in Linux or Unix systems
    outputApps = os.popen('ps -ax | grep .app').read()
    print()
    print("##########################################################")
    print("### APPS #################################################")
    print("##########################################################")
    print(outputApps)
    print()
    print("##########################################################")

    # Get and display running system apps in Linux or Unix systems
    outputSysApps = os.popen('ps -ax | grep /System/Applications').read()
    print()
    print("##########################################################")
    print("### SYSTEM APPS ##########################################")
    print("##########################################################")
    print(outputSysApps)
    print()
    print("##########################################################")

    # Get and display running system apps in Linux or Unix systems
    # that are directly in Application folder
    outputAppsInSysApps = subprocess.Popen('ps -ax | grep /System/Applications/*.app', shell=True)
    print()
    print("##########################################################")
    print("### APPS DIRECTLY IN SYSTEM APPLICATIONS FOLDER ##########")
    print("##########################################################")
    print(outputAppsInSysApps)
    print()
    print("##########################################################")

#EOF
