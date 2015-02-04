#!/usr/bin/env python

import shlex
import json
import sys
from boto.s3.connection import S3Connection, Key
from ansible.module_utils.basic import *

module = AnsibleModule(
  argument_spec = dict(
    bucket = dict( required=True ),
    object = dict( required=True ),
    dest   = dict( required=True ),
    aws_access_key = dict( required=False),
    aws_secret_key = dict( required=False),
    mode = dict( required=False )
  )
)
if 'aws_access_key' in module.params and 'aws_secret_key' in module.params:
  conn = S3Connection(module.params.get('aws_access_key'),module.params.get('aws_secret_key'))
else:
  conn = S3Connection()
bucket = conn.get_bucket(module.params.get('bucket'), validate=False)
k = bucket.new_key(module.params.get('object'))
k.get_contents_to_filename(module.params.get('dest'))

module.exit_json(failed=False,changed=True)