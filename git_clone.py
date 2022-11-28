#!/usr/bin/env python
import subprocess
import shlex
import os

def main():
    repo_list = ["https://github.com/atlanhq/atlas_scan", "https://github.com/atlanhq/code-scanning-documentation"]
    path = "/Users/sanyam.jain/Desktop/internal_adhoc/github_advance_features/clone_repos/repo_folder"
    os.chdir(path)
    #os.system("ls")
    #git remote set-url origin git@github.com:username/repo.git
    try:
        for clone_repo in repo_list:
            #command = ["git", "clone", "{0}.git".format(clone_repo)]
            command = ["git", "clone", "git@github.com:atlanhq/{0}.git".format(clone_repo.split('/')[-1])]
            subprocess.check_output(command, stderr=subprocess.PIPE)
    except Exception as e:
        print(e)
        return

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc

if __name__ == "__main__":
    print("start")
    main()
    print("End")
    