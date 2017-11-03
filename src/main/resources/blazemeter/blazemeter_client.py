import json
from org.apache.http.client import ClientProtocolException
from java.io import IOException
from xlrelease.HttpRequest import HttpRequest

class BlazemeterClient(object):
    def __init__(self, params, api_version):
        try:
            self.request = HttpRequest(params)
        except ClientProtocolException:
            raise Exception("URL is not valid")

        self.api_version = api_version

    def updateTest(self, test_id, content_type, data, headers):
        path = '/api/%s/tests/%s' % (self.api_version, test_id)
        data = data
        json_data = json.dumps(data)

        try:
            response = self.request.put(path, json_data, contentType = content_type, headers = headers)
        except IOException as error:
            print "\nFailed to update test configuration. Error details: `%s`" % error
            return False

        if response.isSuccessful():
            return True

        return False

    def startTest(self, test_id, headers):
        path = '/api/%s/tests/%s/start' % (self.api_version, test_id)

        try:
            response = self.request.post(path, '', headers = headers)
        except IOException as error:
            print "\nFailed to start test. Error details: `%s`" % error
            return ''

        if response.isSuccessful():
            data = json.loads(response.getResponse())
            master_id = data['result']['id']
            return master_id

        return ''

    def checkCiStatus(self, master_id, headers):
        path = '/api/{}/masters/{}/ci-status'.format(self.api_version, master_id)
        try:
            response = self.request.get(path, headers=headers)
        except IOException as error:
            print "\nFailed to check test pass/fail status due to connection problems. Error details: `%s`" % error
            return ''

        if response.isSuccessful():
            data = json.loads(response.getResponse())
            status = data['result']['status']
            return status
        else:
            print "\nFailed to check test pass/fail status. Received an error from the Blazemeter server: `%s`" % response.response
            return ''

    def checkTestCompleteStatus(self, master_id, headers):
        statusContext = '/api/{}/masters/{}/status?events=false'.format(self.api_version, master_id)

        try:
            response = self.request.get(statusContext, headers=headers)
        except IOException as error:
            print "\nFailed to check test status due to connection problems. Will retry in the next polling run. Error details: `%s`" % error
            return ''

        if response.isSuccessful():
            data = json.loads(response.getResponse())
            test_status = data['result']['status']
            return test_status

        print "\nFailed to check the test status. Received an error from the Blazemeter server: `%s`" % response.response
        return ''

    def startMultiTest(self, collection_id, headers):
        path = '/api/{}/collections/{}/start'.format(self.api_version, collection_id)
        
        try:
            self.request.post(path, '', headers=headers)
        except IOException as error:
            print "\nFailed to start multi test. Error details: `%s`" % error 
            return ''

        if response.isSuccessful():
            data = json.loads(response.getResponse())
            master_id = data['result']['id']
            return master_id

        return ''
