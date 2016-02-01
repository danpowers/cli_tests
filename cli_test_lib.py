import subprocess
import time

def cli_delete(ssh_userhost, target):
   try:
       print("Attempt: ssh " + ssh_userhost + " rm -r " + target + "\n")
       result=subprocess.check_output(["ssh", ssh_userhost, "rm -r", target], stderr=subprocess.STDOUT)
       print(result + "\n")
       return result[result.find(":")+2:result.find("\n")]
   except subprocess.CalledProcessError as e:
       if "No such file or directory" in e.output:
           print("Dir did not exist.\n")
           return None
       else:
           print("Unexpected error:\n" + e.output)
           exit(1)


def cli_transfer(ssh_userhost, dir_transfer):
    try:
        print("Attempt: ssh " + ssh_userhost + " transfer -- " + dir_transfer + " -r\n")
        result=subprocess.check_output(["ssh", ssh_userhost, "transfer --", dir_transfer, "-r"],
                                       stderr=subprocess.STDOUT)
        print(result + "\n")
        return result[result.find(":")+2:result.find("\n")]
    except subprocess.CalledProcessError as e:
        print("Unexpected error:\n" + e.output)
        exit(1)


def cli_dir_list(ssh_userhost, dir_list):
    try:
        print("Attempt: ssh " + ssh_userhost + " ls " + dir_list + "\n")
        result=subprocess.check_output(["ssh", ssh_userhost, "ls", dir_list], stderr=subprocess.STDOUT)
        print(result + "\n")
        return result[result.find(":")+2:result.find("\n")]
    except subprocess.CalledProcessError as e:
        if "No such file or directory" in e.output:
            print("No such file or directory: " + dir_list + "\n")
            return None
        else:
            print("Unexpected error:\n" + e.output)
            exit(1)


def cli_status(ssh_userhost, task_id):
    count = 0
    result = ""

    while count < 10:
        try:
            print("Attempt: ssh " + ssh_userhost + " status " + task_id + "\n")
            result=subprocess.check_output(["ssh", ssh_userhost, "status", task_id], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print("Unexpected error:\n" + e.output)
            exit(1)

        if "SUCCEEDED" in result:
            print(result + "\n")
            return True
        elif count >= 10:
            print("Tried: " + count + " times to get status without SUCCEEDED result. Giving up.\n")
            return False
        else:
            time.sleep(10)

def process_args(args):
    bad_arg = False
    env = 1
    username=""
    ssh_userhost = ""

    if len(args) < 2 or len(args) > 3:
        bad_arg = True
    elif len(args) == 3:
        try:
            env = int(args[2])
            if env < 1 or env > 5:
                bad_arg = True
        except:
            bad_arg = True

    if bad_arg is True:
        print("Usage: " + args[0] + " CLI_USERNAME" + " [ENV] \nWhere ENV = 1 prod (default), 2 staging, 3 sandbox," \
                                                         " 4 authsandbox, 5 beta\n")
        exit(1)

    username = args[1]
    ssh_userhost = username + "@XXX"

    if env == 2:
        ssh_userhost=username + "@XXX"
    elif env == 3:
        ssh_userhost=username + "@XXX"
    elif env == 4:
        ssh_userhost=username + "@XXX"
    elif env == 5:
        ssh_userhost=username + "@XXX"

    return env, username, ssh_userhost
