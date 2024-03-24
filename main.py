#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance

class CdkTerraformEc2WebsiteStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # Define AWS provider
        AwsProvider(self, "Aws", region="us-east-1")
        

        # Define EC2 instance
        instance = Instance(self, "WebServer",
                                ami="ami-0c55b159cbfafe1f0",
                                instance_type="t2.micro",
                                tags={"Name": "WebServer"}
                                )

        # Output the public IP of the EC2 instance
        TerraformOutput(
            self,
            "public_ip",
            value=instance.public_ip
        )

app = App()
CdkTerraformEc2WebsiteStack(app, "cdk-terraform-ec2-website")
app.synth()
