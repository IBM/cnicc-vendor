##
##  IBM Confidential
##
##  Copyright IBM Corp. 2019
##
##  The source code for this program is not published or otherwise divested
##  of its trade secrets, irrespective of what has been deposited with the
##  U.S. Copyright Office.

import json
import requests
import time

ARM_URL = 'http://localhost:8080/api/v1.0/resource-manager'
MAX_RETRIES = 5 
@given('the ARM database is initialized')
def step_impl(context):

    for _ in range(MAX_RETRIES):
      results = requests.post("%s/database" % ARM_URL)
      if(results.ok):
          break
      time.sleep(10)
    
    print(results)
    context.results = results

@when(u'I call the "{transition}" transition on resource "{name}" with type "{r_type}"')
def step_impl(context, transition, name, r_type):
    transitionData = { 
                       "deploymentLocation": "world",
                       "properties": {},
                       "metricKey": "fc09c3f9-2fd0-409e-adc3-f9268059f35e",
                       "resourceManagerId": "ansible-rm",
                       "resourceName": name,
                       "resourceType": r_type,
                       "transitionName": transition
                     }

    for _ in range(MAX_RETRIES):
        results = requests.post("%s/lifecycle/transitions" % ARM_URL, json=transitionData)
        if(results.ok):
            break
        time.sleep(10)

    print(results.json())
    context.resource_id = results.json()['requestId']
    context.results = results

@step(u'that transition completes')
def step_impl(context):
    results = requests.get("%s/lifecycle/transitions/%s/status" % (ARM_URL, context.resource_id))
    context.results = results
