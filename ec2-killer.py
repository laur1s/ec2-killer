import boto3
from datetime import datetime, date
import sys
import pprint

dry_run = True

# Check whether dry run or to delete instances:
if len(sys.argv) == 2:
    if str(sys.argv[1] == "commit"):
        dry_run = False

client = boto3.client("ec2", region_name="us-east-1")

ec2_regions = [region["RegionName"] for region in client.describe_regions()["Regions"]]

instances_in_regions = {}
for region in ec2_regions:
    ec2 = boto3.resource("ec2", region_name=region)
    instances = ec2.instances.filter()
    running_instances = [
        instance for instance in instances if instance.state["Name"] == "running"
    ]
    instances_in_regions[region] = running_instances

    for instance in running_instances:
        if instance.launch_time.date() == datetime.today().date():
            instance.modify_attribute(Attribute="disableApiTermination", Value="False")
            instance.terminate(DryRun=dry_run)
            print(
                "Instance to be terminated/was terminated",
                instance.id,
                instance.instance_type,
                region,
            )

pprint.pprint(instances_in_regions)
