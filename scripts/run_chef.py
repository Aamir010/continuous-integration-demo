[root@artifact_server scripts]# cat run_chef.py
#!/usr/bin/python

import subprocess,os

command_chef_client = "chef-client --no-color -z -c /var/chef/chef-repo/.chef/client.rb"
command_node_run = "knife node run_list add -z `knife node list -z` ""recipe[webserver]"""
command_chef_run = "chef-client --no-color -z -c /var/chef/chef-repo/.chef/client.rb"

os.chdir("/var/chef/chef-repo")

os.system(command_chef_client)
os.system(command_node_run)
os.system(command_chef_run)
