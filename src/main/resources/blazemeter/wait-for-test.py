import sys
from blazemeter.blazemeter_client import BlazemeterClient

params = {'url': blazemeterServer['url'],
    'proxyHost': blazemeterServer['proxyHost'], 'proxyPort': blazemeterServer['proxyPort'],
    'proxyUsername': blazemeterServer['proxyUsername'], 'proxyPassword': blazemeterServer['proxyPassword']}

headers = {"x-api-key": blazemeterServer['APIKey']}
api_version = blazemeterServer['apiVersion']

client = BlazemeterClient(params, api_version)

test_status = client.checkTestCompleteStatus(masterId, headers)
if test_status != '':
    if test_status == 'ENDED':
        print "\nTest Completed"
        ci_status = client.checkCiStatus(masterId, headers)
        testStatus = ci_status
        if ci_status != 'success':
            print "\nTest failed with status: `%s`\n\n" % ci_status
            sys.exit(1)
    else:
        task.setStatusLine(test_status)
        task.schedule("blazemeter/wait-for-test.py")
else:
    print "\nFailed to check the test status. Received an error from the Blazemeter server: `%s`" % response.response
