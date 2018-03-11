#!/usr/bin/env python

import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print json.dumps(self.inventory);


    # Example inventory for testing.
    def example_inventory(self):
        return  {
                    'all': {
                        'hosts': ['52.15.105.160'],
                        'vars': {
                            'ansible_user': 'ubuntu',
                            'ansible_ssh_private_key_file':
                                '~/.ssh/aws-key-pair.pem',
                            'example_variable': 'value'
                        }
                    },
                    '_meta': {
                        'hostvars': {
                            '52.15.105.160': {
                                'ec2_access_key' : 'AKIAICUJDXVI3MVLPKKQ',
                                'ec2_secret_key' : '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',
                                'aws_region' : 'us-east-2'
                            }
                        }
                    },
                    'all': ['52.15.105.160'],
                    'test': {
                        'hosts': ['52.15.105.161'],
                        'vars': {
                            'ansible_user': 'ubuntu',
                            'ansible_ssh_private_key_file':
                                '~/.ssh/aws-key-pair.pem',
                            'example_variable': 'value'
                        }
                    },
                    '_meta': {
                        'hostvars': {
                            '52.15.105.161': {
                                'ec2_access_key' : 'AKIAICUJDXVI3MVLPKKQ',
                                'ec2_secret_key' : '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',
                                'aws_region' : 'us-east-2'
                            }
                        }
                    },
                    'test': ['52.15.105.161']
                }
            

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()
