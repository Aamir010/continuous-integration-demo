#!/usr/bin/python

import os
#print os.environ["Name"]

docker_filename = str("dockerfile_"+os.environ["BUILD_NUMBER"])

op = open("/tmp/"+docker_filename,"w")

op.write("# Docker File for " + os.environ["Project"] + " And Build number is " + os.environ["BUILD_NUMBER"] + "\n\n")
op.write("FROM ubuntu:14.04\n\n")
op.write("MAINTAINER " + os.environ["Name"] + "\n\n")
op.write("# Install dependancy packages and redirect ports\n\n")
op.write("RUN apt-get install -y " + os.environ["Package"] + "\n\n")
op.write("COPY . /tmp\n\n")
op.write("RUN rm -rf /var/www/html/*\n\n")
op.write("RUN cp -r /tmp/source/* /var/www/html/\n\n")
op.write("RUN dpkg -i /tmp/chef_12.5.1-1_amd64.deb\n\n")
op.write("RUN apt-get install ruby python -y\n\n")
op.write("RUN python /tmp/script/install_chef.py\n\n")
op.write("RUN cp -r /tmp/cookbooks/* /var/chef/chef-repo/cookbooks/\n\n")
op.write("RUN python /tmp/script/run_chef.py\n\n")
op.write("ENTRYPOINT service apache2 restart && while true; do sleep 10; done")

command_scp = str("scp /tmp/"+docker_filename+" root@artifact:"+os.environ["docker_file_path"])
os.system(command_scp)
