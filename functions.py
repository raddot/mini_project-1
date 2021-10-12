import unshare
import argparse
import os
import sys
from cgroups import Cgroup
import subprocess

def uts_namespace(args):
    unshare.unshare(unshare.CLONE_NEWUTS)
    hostname="hostname " + args.hostname
    os.system(hostname)
    pass

def net_namespace(args):
    unshare.unshare(unshare.CLONE_NEWNET)
    os.system("ip netns add myns1")
    os.system("modprobe dummy")
    os.system("ip link add dummy1 type dummy")
    os.system("ip link set name eth1 dev dummy1")
    os.system("ifconfig eth1 " + args.ip_addr)
    pass

def mnt_namespace(args):
    unshare.unshare(unshare.CLONE_NEWNS)
    pass

def pid_namespace(args):
    unshare.unshare(unshare.CLONE_NEWPID)
    pass

def cpu_cgroup(args):
    pass




def mem_cgroup(args):
    control_group = Cgroup("memory_cgroup")
    control_group.set_memory_limit(args.mem_size)
    control_group.add(os.getpid())
    pass
