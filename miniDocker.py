#!/usr/bin/python3
import unshare
import argparse
import os
import sys
from cgroups import Cgroup
import functions as func

def exe_bash(args):
    newpid = os.fork()
    if newpid == 0:
        dir_path = args.root_path                                                              #specifying path of root project/file
        #os.chdir(dir_path)
        os.chroot('.')                                                                         #to change root directory
        os.system("mount -t proc proc /proc")                                                  #to mount the proc file system on /proc (name, mount_path, dest)
        os.execle('/bin/bash', '/bin/bash', os.environ)                                        #execle(path,arg0...argn,environment) - replaces the current file with new image specified by path
    else:
        os.wait()                                                             #to wait till child process is completed
    pass

if __name__ == "__main__":                                                    #main function
    print ("*************************")
    print ("*                       *")
    print ("*      Mini Docker      *")
    print ("*                       *")
    print ("*************************")

    parser = argparse.ArgumentParser(description='This is a miniDocker.')                            #to parse all data in python data type
                                                                            
    parser.add_argument('--hostname', action="store", dest="hostname", type=str, default="administrator", help='set the container\'s hostname')
                                                                                                                            #set hostname as administrator
    parser.add_argument('--ip_addr', action="store", dest="ip_addr", type=str, default="10.0.0.1",
                        help='set the container\'s ip address')                                                             #set default IP address as 10.0.0.1 

    parser.add_argument('--mem', action="store", dest="mem_size", type=int, default=10,
                        help='set the container\'s memory size (MB)')                                               #memory size is set to 10 by default

    parser.add_argument('--cpu', action="store", dest="cpu_num", type=int, default=1,
                        help='set the container\'s cpu number')                                                    #number of CPU is set to 1 by default

    parser.add_argument('--root_path', action="store", dest="root_path", type=str, default="./new_root", help='set the new root file system path of the container')
args = parser.parse_args()                                                                                         #set default path as new_root


#create hostname namespace
func.uts_namespace(args)
#create network namespace
func.net_namespace(args)
#create filesystem namespace
func.mnt_namespace(args)
#create cpu cgroup
func.cpu_cgroup(args)
#create memory cgroup
func.mem_cgroup(args)
#create pid namespace
func.pid_namespace(args)
#execute the bash process "/bin/bash"
exe_bash(args)
