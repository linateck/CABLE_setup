#!/usr/bin/env python

"""
Get repository, copy locally to user area, download, build the executables
and run CABLE for Tumbarumba.

That's all folks.
"""

__author__ = "Martin De Kauwe"
__version__ = "1.0 (11.03.2019)"
__email__ = "mdekauwe@gmail.com"

import os
import shutil
import sys
import datetime
import subprocess
sys.path.append("scripts")
from get_cable import GetCable
from build_cable import BuildCable
from run_cable_site import RunCable
from set_default_paths import set_paths

now = datetime.datetime.now()
date = now.strftime("%d_%m_%Y")
cwd = os.getcwd()
(sysname, nodename, release, version, machine) = os.uname()

#------------- User set stuff ------------- #
user = "mgk576"

#
## user directories ...
#
src_dir = "src"
run_dir = "runs"
log_dir = "logs"
plot_dir = "plots"
output_dir = "outputs"
restart_dir = "restart_files"
namelist_dir = "namelists"

# If this is set the code will download a specific repo, otherwise
user_path = None
#user_path = "https://trac.nci.org.au/svn/cable/branches/Users/%s/CABLE_testing" % (user)

#
## Met files ...
#
met_subset = ['TumbaFluxnet.1.4_met.nc']
met_dir = None # if None, it will use default PLUMBER path

#
## Needs different paths for NCI, storm ... this is set for my mac
## comment out the below and set your own, see scripts/set_default_paths.py
#
(met_dir, NCDIR, NCMOD, FC, CFLAGS, LD, LDFLAGS) = set_paths(nodename, met_dir)

#
## science config
#
sci_config = {
                "cable_user%GS_SWITCH": "'medlyn'",
}

#
## MPI stuff
#
mpi = False
num_cores = None #4 # set to a number, if None it will use all cores...!

# ------------------------------------------- #

# clean out old src directory
if os.path.exists(src_dir):
    shutil.rmtree(src_dir)
    os.makedirs(src_dir)

#
## Get CABLE ...
#
G = GetCable(src_dir=src_dir, user=user)

if user_path is None:
    # Setup for the head of the trunk
    repo = "Trunk_%s" % (date)
    G.main(repo_name=repo, trunk=True)
else:
    # Setup for user specified path
    repo = os.path.basename(user_path)
    G.main(repo_name=user_path, trunk=False)

#
## Build CABLE ...
#
B = BuildCable(src_dir=src_dir, NCDIR=NCDIR, NCMOD=NCMOD, FC=FC,
               CFLAGS=CFLAGS, LD=LD, LDFLAGS=LDFLAGS)
B.main(repo_name=repo)

#
## Run CABLE for test case
#
if not os.path.exists(run_dir):
    os.makedirs(run_dir)
os.chdir(run_dir)


aux_dir = "../src/CABLE-AUX/"
cable_src = "../src/%s" % (repo)

R = RunCable(met_dir=met_dir, log_dir=log_dir,
             output_dir=output_dir, restart_dir=restart_dir,
             aux_dir=aux_dir, namelist_dir=namelist_dir,
             met_subset=met_subset, cable_src=cable_src, mpi=mpi,
             num_cores=num_cores)
R.main(sci_config)
os.chdir(cwd)
