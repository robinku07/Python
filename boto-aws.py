FILE_ROOT = "c:\\repos\\Python\\audits.log"
import boto3
ec2 = boto3.client('ec2', 'us-east-1')
response = ec2.describe_regions()
region_list = []
with open(FILE_ROOT, mode='w') as iam_audit:
    pass
iam_audit.close()
for region in response['Regions']:
    region_list.append(region['RegionName'])
with open(FILE_ROOT , mode='a+') as vpcs_audit:
    for region in region_list:
        ec2 = boto3.client('ec2', region)
        region_security_groups = ec2.describe_security_groups()
        vpcs = ec2.describe_vpcs()
        subnets = ec2.describe_subnets()
        endpoints = ec2.describe_vpc_endpoints()
        vpn_peer_connections = ec2.describe_vpc_peering_connections()
        vpn_connections = ec2.describe_vpn_connections()
        vpn_gateways = ec2.describe_vpn_gateways()
        internet_gateways = ec2.describe_internet_gateways()
        nat_gateways = ec2.describe_nat_gateways()
        network_acls = ec2.describe_network_acls()
        route_tables = ec2.describe_route_tables()
        print("Region:" + region)
        print("VPCs and Security Groups List:")
        vpcs_audit.write("Region:" + region + "\nVPCs and Security Groups List:\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "VPCs List" + "-" * 50 + "\n")
        for response in vpcs['Vpcs']:
            print(response)
            vpcs_audit.write(str(response) + "\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "Subnets List" + "-" * 50 + "\n")
        for response in subnets['Subnets']:
            print(response)
            vpcs_audit.write(str(response) + "\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "VpcEndpoints List" + "-" * 50 + "\n")
        for response in endpoints['VpcEndpoints']:
            print(response)
            vpcs_audit.write(str(response) + "\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "VPC Peering Connections List" + "-" * 50 + "\n")
        for response in vpn_peer_connections['VpcPeeringConnections']:
            print(response)
            vpcs_audit.write(str(response) + "\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "VPN Connections List" + "-" * 50 + "\n")
        for response in vpn_connections['VpnConnections']:
            print(response)
            vpcs_audit.write(str(response) + "\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "VPN Gateways List" + "-" * 50 + "\n")
        for response in vpn_gateways['VpnGateways']:
            print(response)
            vpcs_audit.write(str(response) + "\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "Internet Gateways List" + "-" * 50 + "\n")
        for response in internet_gateways['InternetGateways']:
            print(response)
            vpcs_audit.write(str(response) + "\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "NAT Gateways List" + "-" * 50 + "\n")
        for response in nat_gateways['NatGateways']:
            print(response)
            vpcs_audit.write(str(response) + "\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "Network ACLs List" + "-" * 50 + "\n")
        for response in network_acls['NetworkAcls']:
            print(response)
            vpcs_audit.write(str(response) + "\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "Route Tables List" + "-" * 50 + "\n")
        for response in route_tables['RouteTables']:
            print(response)
            vpcs_audit.write(str(response) + "\n")
        vpcs_audit.write("\t" * 4 + "-" * 50 + "Security Groups List" + "-" * 50 + "\n")
        for response in region_security_groups['SecurityGroups']:
            print(response)
            vpcs_audit.write(str(response)+ "\n")
vpcs_audit.close()
iam = boto3.client('iam','us-east-1')
users = iam.list_users()
with open(FILE_ROOT, mode='a+') as iam_users:
    print("IAM Users List:")
    iam_users.write("IAM Users List:\n")
    for response in users['Users']:
        print(response)
        iam_users.write(str(response) + "\n")
iam_users.close()
groups = iam.list_groups()
with open(FILE_ROOT, mode='a+') as iam_groups:
    print("IAM Groups List:")
    iam_groups.write("IAM Groups List:\n")
    for response in groups['Groups']:
        print(response)
        iam_groups.write(str(response) + "\n")
iam_groups.close()
roles = iam.list_roles()
with open(FILE_ROOT, mode='a+') as iam_roles:
    print("IAM Roles List:")
    iam_roles.write("IAM Roles List:\n")
    for response in roles['Roles']:
        print(response)
        iam_roles.write(str(response) + "\n")
iam_roles.close()
policies = iam.list_policies()
with open(FILE_ROOT, mode='a+') as iam_policies:
    print("IAM Policies List:")
    iam_policies.write("IAM Policies List:\n")
    for response in policies['Policies']:
        print(response)
        iam_policies.write(str(response) + "\n")
iam_policies.close()

