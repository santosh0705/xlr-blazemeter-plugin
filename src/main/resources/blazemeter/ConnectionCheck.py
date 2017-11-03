import json
from org.apache.http.client import ClientProtocolException

params = {'url': configuration.url,
    'proxyHost': configuration.proxyHost, 'proxyPort': configuration.proxyPort,
    'proxyUsername': configuration.proxyUsername, 'proxyPassword': configuration.proxyPassword}

APIPath = configuration.checkConfigurationPath
if hasattr(configuration, 'checkConfigurationContentType') and configuration.checkConfigurationContentType:
    contentType = configuration.checkConfigurationContentType
else:
    contentType = 'application/json'


response = None
try:
    response = HttpRequest(params).get(APIPath, contentType = contentType, headers = {'x-api-key': configuration.APIKey})
except ClientProtocolException:
    raise Exception("URL is not valid")

if response.isSuccessful():
    data = json.loads(response.getResponse())
    print "Blazemeter API version: %s" % data['api_version']
else:
    reason = "Unknown"
    if response.status == 400:
        reason = "Bad request"
    elif response.status == 401:
        reason = "Unauthorized"
    elif response.status == 403:
        reason = "Forbidden"
    raise Exception("HTTP response code %s (%s)" % (response.status, reason))
