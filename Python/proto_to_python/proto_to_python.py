#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import subprocess

def generate_python_modules_for_proto(proto_directory):
    print(proto_directory)
    for root, dirs, files in os.walk(proto_directory):
        print("root:")
        print(root)
        print("dirs:")
        print(dirs)
        print("files:")
        print(files)
        for file in files:
            print(file)
            if file.endswith(".proto"):
                proto_file_path = os.path.join(root, file)
                command = "protoc -I={} --python_out={} {}".format(proto_directory, proto_directory, proto_file_path)
                print(command)
                subprocess.call(command, shell=True)

proto_root_directory = "/citibot/Demo/Python/proto_to_python"


generate_python_modules_for_proto(proto_root_directory)
