import sys
from blazemeter.blazemeter_client import BlazemeterClient

if blazemeterServer is None:
    print "No Blazemeter server provided"
    sys.exit(1)

params = {'url': blazemeterServer['url'],
    'proxyHost': blazemeterServer['proxyHost'], 'proxyPort': blazemeterServer['proxyPort'],
    'proxyUsername': blazemeterServer['proxyUsername'], 'proxyPassword': blazemeterServer['proxyPassword']}

content_type = 'application/json'
headers = {"x-api-key": blazemeterServer['APIKey']}
api_version = blazemeterServer['apiVersion']

client = BlazemeterClient(params, api_version)

data = {
    "configuration" : {
        "plugins" : {
            "jmeter" : {
                "enginesArgs": jmeterEnginesArgs,
                "consoleArgs": jmeterConsoleArgs
            }
        }
    }
}

if client.updateTest(testId, content_type, data, headers):
    task.setStatusLine("Updated test: #%s" % testId)
else:
    print 'Unable to update test'
    task.setStatusLine("FAILED updating test: #%s" % testId)
    sys.exit(1)

master_id = client.startTest(testId, headers)
if master_id == '':
    print 'Could not get Master ID'
    task.setStatusLine("FAILED getting master ID")
    sys.exit(1)

task.setStatusLine("Test master ID: #%s" % master_id)
masterId = master_id
task.schedule("blazemeter/wait-for-test.py")
