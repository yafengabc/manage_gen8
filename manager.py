#!/opt/bin/python2.7
#coding:utf-8

import paramiko
import sys
import time
gen8=None
def init_ssh():
    global gen8
    gen8=paramiko.SSHClient()
    gen8.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    gen8.connect('192.168.0.10',222,'yafeng','12345668')
    
def ssh_exec(cmd):
    stdin,stdout,stderr=gen8.exec_command(cmd)
    ret=stdout.readlines()
    return ret

def fmt_ret(ret):
    for i in ret:
        if i.startswith('Server'):
            return(i.strip())
        if i.startswith('server'):
            return(i.strip())

def switch_cmd(cmd):
    if cmd=='status':
        ret=ssh_exec('power')
        print(ret)
        print(fmt_ret(ret))
        return fmt_ret(ret)
    if cmd=='on':
        ret=ssh_exec('power on')
        print(fmt_ret(ret))
        return fmt_ret(ret)
    if cmd=='off':
        ret=ssh_exec('power off')
        print(fmt_ret(ret))
        return fmt_ret(ret)

if __name__=="__main__":
    while True:
        init_ssh()
        ret=switch_cmd('status')
        ret=ret.split(':')
        if len(ret)>1:
            ret=ret[-1]
        print(ret)
        if ret=='on':
            pass
        if ret=='off':
            pass

        time.sleep(10)


    



