# mini_project-1

This project is based on two virtualization techniques - 

1) Docker (a light weight container-based virtualization technique) and 
2) QEMU (a user level full virtualization technique)

Tasks performed in this project are as below -

1) Deployed the docker and QEMU, familiarize with the basic operations, performed the performance using sysbench and summarized the result in report.
2) Implemented a docker-like tool which creates a container instance with configurable namespaces and control groups.

**Environment Setup -**

Configured a Google cloud instance using 2 vCPU, 4 GB memory, 30 GB disk size, andd Ubuntu 18.04 LTS image. This is referred as a native environment.

**Docker Performance -**

The performance of Docker containers are measured using sysbench benchmark. The main focus in this project is cpu test mode and fileio test mode.

**MiniDocker Container -**

Requirement -

Install cgroups using the below command
pip3 install cgroups

Install unshare library using the below command
pip3 install unshare

Files attached are as below -

miniDocker.py (This is a main file to run container like instance)
functions.py (All functions are present in this file and this file is imported into miniDocker.py)





