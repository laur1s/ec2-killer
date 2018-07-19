# ec2-killer
A Python script that kills your ec2 instances 

## What is ec2-killer

ec2 killer is a script that uses your aws credentials to connect to the ec2 api. It might be useful if your AWS credentials
were compromised it can delete instances that were created today.

## how to use

1. Install the required python modules: `pip install -r requirements.txt`
2. dry run the script `python instances.py`
3. run the script if you're sure that you want to terminate the instances `python instances.py commit` WARNING: This will terminate
instances
