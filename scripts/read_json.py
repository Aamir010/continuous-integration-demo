#!/usr/bin/python

import json, os

with open('dependency.json') as data_file:
        data = json.load(data_file)


a = data.keys()
counter = 0

#for each in range(len(a)):
#        list_counter = 0
#        for each in range(len(data[a[counter]])):
#                if (type(data[a[counter]]) is list):
#                        print data[a[counter]][list_counter]
#			os.environ[a[counter]] = str(data[a[counter]])
#			print os.environ[a[counter]]
#                        list_counter = list_counter + 1
#                if not (type(data[a[counter]]) is list):
#			key_counter = 0
#			for each in range(len(data[a[counter]].keys())):
#                        	print data[a[counter]].keys()[key_counter]
#				print data[a[counter]].values()[key_counter]
#				os.environ[data[a[counter]].keys()[key_counter]] = str(data[a[counter]].values()[key_counter])
#				print os.environ[data[a[counter]].keys()[key_counter]]
#				key_counter = key_counter + 1
#        counter = counter + 1

#fo = open("inject_variable.properties","w")
#counter = 0
#for each in range(len(a)):
#	if (type(data[a[counter]]) is list):
#		print data[a[counter]]
#		os.environ[a[counter]] = str(data[a[counter]])
#		print os.environ[a[counter]][list_counter]
#		list_counter = 0
#		for each in range(len(data[a[counter]])):
#			concat_str = str(data[a[counter]][list_counter])
#			concat_str = concat_str + " "
#			list_counter = list_counter + 1
#		fo.write(str(a[counter])+"="+str(concat_str+"\n")
#	if not (type(data[a[counter]]) is list):
#		key_counter = 0
#		for each in range(len(data[a[counter]].keys())):
#			print data[a[counter]].keys()[key_counter]
#			os.environ[data[a[counter]].keys()[key_counter]] = str(data[a[counter]].values()[key_counter])
#			print os.environ[data[a[counter]].keys()[key_counter]]
#			fo.write(str(data[a[counter]].keys()[key_counter])+"="+str(data[a[counter]].values()[key_counter])+"\n")
#			key_counter = key_counter + 1
#	counter = counter + 1
#fo.close()

#print data[a[0]].split('')

fo = open("/tmp/inject_variable.properties","w")
counter = 0
for each in range(len(a)):
       if (type(data[a[counter]]) is list):
               list_counter = 0
               fo.write(str(a[counter])+"=")
               for each in range(len(data[a[counter]])):
                       concat_str = str(data[a[counter]][list_counter])
                       concat_str = concat_str + " "
                       fo.write(str(concat_str+" "))
                       list_counter = list_counter + 1
               fo.write("\n")
       if not (type(data[a[counter]]) is list):
               key_counter = 0
               for each in range(len(data[a[counter]].keys())):
                       fo.write(str(data[a[counter]].keys()[key_counter])+"="+str(data[a[counter]].values()[key_counter])+"\n")
                       key_counter = key_counter + 1
       counter = counter + 1
fo.close()
