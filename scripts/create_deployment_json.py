#!/usr/bin/python

import os, json

with open('deployment_config_demo.json') as data_file:
	data = json.load(data_file)

data["id"] = str(os.environ["Project"]+"-"+os.environ["BUILD_NUMBER"])
data["cpus"] = float(os.environ["cpus"])
data["mem"] = float(os.environ["mem"])
data["container"]["docker"]["image"] = str(os.environ["DOCKER_REGISTRY_URL"]+"/"+os.environ["Project"]+":"+os.environ["BUILD_NUMBER"])
deployment_file=str("/tmp/deployment-"+os.environ["JOB_NAME"]+"-"+os.environ["BUILD_NUMBER"]+".json")
with open(deployment_file,"w") as data_file:
	json.dump(data, data_file)
