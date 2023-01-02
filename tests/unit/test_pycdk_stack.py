import aws_cdk as core
import aws_cdk.assertions as assertions

from pycdk.pycdk_stack import PycdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in pycdk/pycdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PycdkStack(app, "pycdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
