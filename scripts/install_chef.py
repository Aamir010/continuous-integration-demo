#!/usr/bin/python

import subprocess, os
#command_chef = "curl -L https://www.opscode.com/chef/install.sh | bash"
#command_ruby = "apt-get install ruby -y"
command_master_download = "wget http://github.com/opscode/chef-repo/tarball/master"
command_dir = "mkdir -p /var/chef"
command_tar = "tar -zxf master && mv /var/chef/chef-chef-repo* /var/chef/chef-repo"
command_create_dir = "mkdir -p chef-repo/.chef"

#subprocess.Popen(command_chef, shell=True, stdout=subprocess.PIPE).wait()
#subprocess.Popen(command_ruby, shell=True, stdout=subprocess.PIPE).wait()
subprocess.Popen(command_dir, shell=True, stdout=subprocess.PIPE).wait()
os.chdir("/var/chef")
subprocess.Popen(command_master_download, shell=True, stdout=subprocess.PIPE).wait()
subprocess.Popen(command_tar, shell=True, stdout=subprocess.PIPE).wait()
subprocess.Popen(command_create_dir, shell=True, stdout=subprocess.PIPE).wait()

op = open("/var/chef/chef-repo/.chef/knife.rb","w")
op.write("cookbook_path [ '/var/chef/chef-repo/cookbooks' ]\n")
op.write("node_path [ '/var/chef/chef-repo/nodes' ]")
op.close()

op = open("/var/chef/chef-repo/.chef/client.rb","w")
op.write("cookbook_path [ '/var/chef/chef-repo/cookbooks' ]\n")
op.write("node_path [ '/var/chef/chef-repo/nodes' ]")
op.close()
