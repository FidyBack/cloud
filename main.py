import boto3
from keys import AWS_Access_Key, AWS_Secret_Key

# Initialize Sessions Ohio and North Virginha
ohio = boto3.session.Session(aws_access_key_id = AWS_Access_Key,
                                aws_secret_access_key = AWS_Secret_Key,
                                region_name = 'us-east-2')

nv = boto3.session.Session(aws_access_key_id = AWS_Access_Key,
                                       aws_secret_access_key = AWS_Secret_Key,
                                       region_name = 'us-east-1')

# Connect with EC2 Resources and Client
ec2_resource_ohio = ohio.resource('ec2')
ec2_client_ohio = ohio.client('ec2')

ec2_resource_nv = nv.resource('ec2')
ec2_client_nv = nv.client('ec2')

#==========================================================================#
#                          Configuration for Ohio                          #
#==========================================================================#
# UserData initialization for Postgres
with open("userdata_postgresql.txt", "r") as data:
    userdata_postgresql = data.read()

# Create Instance Ohio
instance_ohio = ec2_resource_ohio.create_instances(ImageId = 'ami-0a91cd140a1fc148a',
                                                InstanceType = 't2.micro',
                                                KeyName = 'AbelProj_OH',
                                                MaxCount = 1,
                                                MinCount = 1,
                                                SecurityGroupIds = ['sg-0c56fa1cb26170a32'],
                                                UserData = userdata_postgresql,
                                                TagSpecifications = [
                                                    {
                                                        'ResourceType': 'instance',
                                                        'Tags': [
                                                            {
                                                                'Key': 'Name',
                                                                'Value': 'abelInsancesOH'
                                                            },
                                                        ]
                                                    },
                                                ])
print (instance_ohio[0])

#==========================================================================#
#                    Configuration for N. Virginia                         #
#==========================================================================#
# UserData initialization for Postgres
with open("userdata_ORM.txt", "r") as data:
    userdata_orm = data.read()

# Create Instance North Virginia
instance_nv = ec2_resource_nv.create_instances(ImageId = 'ami-0885b1f6bd170450c',
                                            InstanceType = 't2.micro',
                                            KeyName = 'AbelProj_NV',
                                            MaxCount = 1,
                                            MinCount = 1,
                                            SecurityGroupIds = ['sg-02717999aab7532b8'],
                                            UserData = userdata_orm,
                                            TagSpecifications = [
                                                {
                                                    'ResourceType': 'instance',
                                                    'Tags': [
                                                        {
                                                            'Key': 'Name',
                                                            'Value': 'abelInsancesNV'
                                                        },
                                                    ]
                                                },
                                            ])
print (instance_nv[0])