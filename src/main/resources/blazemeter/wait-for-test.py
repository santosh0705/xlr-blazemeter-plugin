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
        print 'Test Completed'
        ci_status = client.checkCiStatus(masterId, headers)
        if ci_status != '':
            testStatus = ci_status
        else:
            print "\nFailed to check test status whether it is passed or not."
    else:
        task.setStatusLine(test_status)
        task.schedule("blazemeter/wait-for-test.py")
else:
    print "\nFailed to check the test status. Received an error from the Blazemeter server: `%s`" % response.response
