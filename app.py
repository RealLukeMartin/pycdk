#!/usr/bin/env python3
import os

import aws_cdk as cdk

from pycdk.pycdk_stack import PycdkStack


app = cdk.App()
PycdkStack(app, "PycdkStack")

app.synth()
