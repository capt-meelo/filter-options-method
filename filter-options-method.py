"""
Name:           Filter OPTIONS Method
Version:        1.2
Author:         Capt. Meelo (@CaptMeelo)
Description:    A Burp extension that filters out `OPTIONS` requests from populating Burp's Proxy history. 
Blog Post:      https://captmeelo.com/pentest/2020/01/06/filter-options-method.html
Idea From:      https://parsiya.net/blog/2019-04-06-hiding-options-an-adventure-in-dealing-with-burp-proxy-in-an-extension/ (Huge Thanks!)
"""

from burp import IBurpExtender
from burp import IHttpListener

class BurpExtender(IBurpExtender, IHttpListener):

    # implement IBurpExtender
    def registerExtenderCallbacks(self, callbacks):
        
        # obtain an extension helpers object
        self._helpers = callbacks.getHelpers()
        
        # set our extension name
        callbacks.setExtensionName("Filter OPTIONS Method")
        
        # register ourselves as an HTTP listener
        callbacks.registerHttpListener(self)

    # implement IHttpListener
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        
        # only process responses
        if messageIsRequest:
            return

        # focus on Proxy tool only (constant value is "4") and ignore other tools (e.g. Repeater)
        # constant values here: https://portswigger.net/burp/extender/api/constant-values.html#burp.IBurpExtenderCallbacks.TOOL_PROXY
        # if you want to include all tools (e.g Repeater, etc.), comment out these two lines
        if toolFlag != 4:
            return

        # analyze the requests and focus only on OPTIONS method
        requestBytes = messageInfo.getRequest()
        requestInfo = self._helpers.analyzeRequest(requestBytes)
        if requestInfo.getMethod() == "OPTIONS":

            # analyze the responses and its headers
            responseBytes = messageInfo.getResponse()
            responseInfo = self._helpers.analyzeResponse(responseBytes)
            responseHeaders = responseInfo.getHeaders()

            # analyze the header and remove "Content-Type" header if it exists
            removeHeaders = ""
            for headers in responseHeaders:
                if "Content-Type: " in headers:
                    removeHeaders = headers
            try:
                responseHeaders.remove(removeHeaders)
            except:
                pass

            # add the new Content-Type
            responseHeaders.add("Content-Type: text/css; charset=UTF-8")
            
            # comment out the response body (refer to the blog why I did it)
            responseBodyBytes = "/* Injected by 'Filter OPTIONS Method' */"
            
            # rebuild the new response
            responseModified = self._helpers.buildHttpMessage(responseHeaders, responseBodyBytes)
            messageInfo.setResponse(responseModified)
