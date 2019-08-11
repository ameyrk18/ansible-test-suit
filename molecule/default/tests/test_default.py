import os
import sys

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_check_read_write(host):
    users = ["dev1","dev2","dev3","dev4"]
    for u in users:
        host_users = _get_check_read_write(u)
        read_write = host.file(host_users).user
        if u == read_write:
            print ("User",read_write,"and he can read and write because he has the directory ownership...")
        else:
            sys.exit('UNIT TEST FAILED! One or more users cannot read and write')


def _get_check_read_write(passed_users):
    return {
        "dev1": "/var/www/mango.com/public_html",
        "dev2": "/var/www/apple.com/public_html",
        "dev3": "/var/www/papaya.com/public_html",
        "dev4": "/var/www/grapes.com/public_html"
    }.get(passed_users)


def test_check_cannot_read_write_to_others(host):
    users = ["dev1","dev2","dev3","dev4"]
    for u in users:
        host_users = _get_check_read_write(u)
        read_write = host.file(host_users).mode
        # match returned octal integer from test infra hosts with the defined octal integer of developers
        if 493 == read_write:
            print ("User",read_write,"read, write permissions and other users have execute and read except root user")
        else:
            print (read_write,u)
            sys.exit('UNIT TEST FAILED!One or more users cannot read and write')

def _get_check_cannot_read_write_to_others(passed_users):
    return {
        # 493 octal integer of 0755
        "dev1": "493",
        "dev2": "493",
        "dev3": "493",
        "dev4": "493"
    }.get(passed_users)