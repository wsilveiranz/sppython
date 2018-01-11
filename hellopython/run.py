import os
import platform
import json
import pandas  as pd

postreqdata = json.loads(open(os.environ['req']).read())

message = "Hello world from {0} - Using Python '{1}'. Pandas version is {2}".format(postreqdata['name'],platform.python_version(), pd.__version__)
print(message)

response = open(os.environ['res'], 'w')
response.write(message)
response.close()