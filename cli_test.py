#!/usr/bin/python

import time
import sys
import cli_test_lib

def main():
    dir_del="go#ep2/~/godata/"
    dir_transfer="go#ep1/share/godata/ go#ep2/~/godata/"
    dir_list="go#ep2/~/godata/"
    task_id=None

    env, username, ssh_userhost = cli_test_lib.process_args(sys.argv)

    print("-----Housekeeping-----\n")
    task_id = cli_test_lib.cli_delete(ssh_userhost, dir_del)
    if task_id is not None:
        print("Cleaning up test directory if needed.\n")
        time.sleep(2)
        if cli_test_lib.cli_status(ssh_userhost, task_id) is False:
            exit(1)
    print("----------------------\n")

    print("-----Transfer Test-----\n")
    task_id = cli_test_lib.cli_transfer(ssh_userhost, dir_transfer)
    print("Checking if transfer succeeded.\n")
    time.sleep(2)
    if cli_test_lib.cli_status(ssh_userhost, task_id) is False:
        exit(1)
    print("-----------------------\n")

    print("-----Dir List Test-----\n")
    cli_test_lib.cli_dir_list(ssh_userhost, dir_list)
    print("-----------------------\n")

    print("-----Delete Test-----\n")
    task_id = cli_test_lib.cli_delete(ssh_userhost, dir_del)
    if task_id is not None:
        print("Checking if delete succeeded.\n")
        time.sleep(2)
        if cli_test_lib.cli_status(ssh_userhost, task_id) is False:
            exit(1)
    print("---------------------\n")

    exit(0)


if __name__ == "__main__":
    main()
