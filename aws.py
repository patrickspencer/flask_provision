import click
import boto3

@click.group()
def cli():
    pass

@click.group()
def instance():
    pass

ec2 = boto3.resource('ec2')

@click.command()
def create():
    instance = ec2.create_instances(
            ImageId='ami-4d5f8a5b',
            InstanceType='t2.micro',
            KeyName='patrick-x240-2',
            MinCount=1,
            MaxCount=1,
            SecurityGroups=[
                'launch-wizard-4',
            ],
        )
    print(instance)

@click.command()
def show():
    instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print(
                instance.id,
                instance.instance_type,
                instance.public_ip_address,
                instance.public_dns_name
                )

cli.add_command(create)
cli.add_command(show)

if __name__ == '__main__':
    cli()
