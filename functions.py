import unshare                          #used to run program in new namespace
import argparse                         #used to parse arguments and write a user friendly CLI
import os                               #used for OS dependency functionality
import sys                              #provides system specific parameters and functions
from cgroups import Cgroup              #used to allocate resources such as CPU time, memory, etc
import subprocess

def uts_namespace(args):                           #function to create hostname namespace
    unshare.unshare(unshare.CLONE_NEWUTS)          #clone creates the child process
    hostname="hostname " + args.hostname           #to set hostname
    os.system(hostname)                            #to get hostname
    pass

def net_namespace(args):                            #function to create a network namespace
    unshare.unshare(unshare.CLONE_NEWNET)           
    os.system("ip netns add myns1")                         #to create a new namespace whose name is myns1
    os.system("modprobe dummy")                             #to create a dummy interface
    os.system("ip link add dummy1 type dummy")              #to add additional dummy interface
    os.system("ip link set name eth1 dev dummy1")           #to set name to device dummy1
    os.system("ifconfig eth1 " + args.ip_addr)              #to get current network configuration
    pass

def mnt_namespace(args):                                    #function to create file system namespace
    unshare.unshare(unshare.CLONE_NEWNS)
    pass

def pid_namespace(args):                                    #function to create pid namespace
    unshare.unshare(unshare.CLONE_NEWPID)
    pass

def cpu_cgroup(args):                                       #function to create cpu cgroups
    pass

def mem_cgroup(args):                                       #function to create memory cgroup
    control_group = Cgroup("memory_cgroup")
    control_group.set_memory_limit(args.mem_size)            #to set memory range
    control_group.add(os.getpid())                           #to add group in cgroup
    pass
