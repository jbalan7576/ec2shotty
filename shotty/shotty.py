import boto3
if __name__ == '__main__':
		session=boto3.Session(profile_name='shotty')
		servers=session.resource('ec2')


for i in servers.instances.all():
    print(i)
