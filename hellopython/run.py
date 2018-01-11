import os
import platform
import json

postreqdata = json.loads(open(os.environ['req']).read())

message = "Hello world from {0} - Using Python '{1}'".format(postreqdata['name'],platform.python_version())
print(message)

response = open(os.environ['res'], 'w')
response.write(message)
response.close()