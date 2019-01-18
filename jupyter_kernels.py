#!/usr/bin/env python3

"""
Jupyter Notebook Script

Allows to show open Notebook Kernels + PID + open files

requires linux, osx (lsof, ps, grep)
Tested on linux

Date: Fr Jän 18 10:50:45 CET 2019

"""

def get_notebook_name(servers):
    """
    Return the full path of the jupyter notebook.
    """
    import json
    import os.path
    import re
    import ipykernel
    import requests
    from requests.compat import urljoin
 
    out = {}
    for ss in servers:
        print("URL:", ss['url'], "DIR:", ss['notebook_dir'], "PID:", ss['pid'])
        response = requests.get(urljoin(ss['url'], 'api/sessions'),
                                params={'token': ss.get('token', '')})
        for nn in json.loads(response.text):
            relative_path = nn['notebook']['path']
            out[nn['kernel']['id']] = (nn['kernel']['name'], os.path.join(ss['notebook_dir'], relative_path))
    return out

def get_pid_kernels():
    """
    get PID of kernel
    """
    from subprocess import Popen, PIPE, STDOUT
    cmd = "ps ux | grep jupyter"
    ps = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    output = ps.communicate()[0]
    out = {}
    for i in output.splitlines():
        p = i.decode('utf8').split()
        k = p[len(p)-1]  # kernel
        k = k.split('/')[-1].replace('kernel-','').replace('.json','')
        out[k] = p[1]  # PID
    return out

def get_openfiles(pid):
    """
    get open files, filter
    """
    from subprocess import Popen, PIPE, STDOUT
    cmd = "lsof -a -d 0-999 -p %s | grep REG | grep -v '.log' | grep -v 'sqlite' | grep -v 'fonts'" % pid
    ps = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    output = ps.communicate()[0]
    if len(output) > 0:
        print("Open files: ")
        for i in output.splitlines():
            print(i.decode('utf8'))

        print("---")
    
if __name__ == '__main__':
    import sys
    from notebook.notebookapp import list_running_servers

    show_files = False
    if len(sys.argv) > 1:
        if sys.argv[1] == '-f':
            show_files = True
        else:
            print("Usage: %s -f" % sys.argv[0])
    
    # get running servers
    servers = list_running_servers()
    print("#"*10)
    print("Servers:")
    files = get_notebook_name(servers)
    # get PIDS to kernels 
    pids = get_pid_kernels()

    print("#"*10)
    print("Kernels + Notebooks:")
    print("%36s %7s %10s %s" % ("ID","PID","PY","Notebook"))
    for i,j in files.items():
        print("%36s %7s %10s %s" % ((i, pids[i],) + j))
        if show_files:
            get_openfiles(pids[i])
    print("#"*10)
    
    
