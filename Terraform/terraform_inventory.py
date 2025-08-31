#!/usr/bin/env python3
import json
import subprocess
import os

# Get Terraform output in JSON
tf_output = subprocess.check_output(["terraform", "output", "-json"]).decode()
tf_data = json.loads(tf_output)

# Extract IPs
ips = tf_data["web_instance_ips"]["value"]

# Build absolute path to the key
key_path = os.path.join(os.getcwd(), "web-key.pem")

# Build Ansible inventory format
inventory = {
    "webservers": {
        "hosts": [f"ec2-{i}" for i in range(len(ips))],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": key_path
        }
    },
    "_meta": {
        "hostvars": {
            f"ec2-{i}": {"ansible_host": ip} for i, ip in enumerate(ips)
        }
    }
}

print(json.dumps(inventory, indent=2))
