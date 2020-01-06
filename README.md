# Filter OPTIONS Method
[![Version](https://img.shields.io/badge/Version-v1.0-green.svg)]()
[![Language](https://img.shields.io/badge/Language-Python-orange.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)]()


A Burp extension that filters out `OPTIONS` requests from populating Burp's Proxy history. This extension works by doing the following:

1. Forcing the `Content-Typ` header value to `text/css; charset=UTF-8`.
2. Emptying the response body so Burp will not recognize the MIME type incorrectly.

A post about this extension can be found [post]().

### Installation

1. Download [burp-filter-options-method.py]() to your machine.
2. Go to _**Extender > Extensions**_ tab, then click on the _**Add**_ button. On the new window, browse the location of **burp-filter-options-method.py** and click the _**Next**_ button.
![Load Extension](/images/load-extension.png)


### How to Use

To filter out these `OPTIONS` requests, go to _**HTTP history > Filter by MIME type**_, and untick the _**CSS**_ checkbox.
![Filter CSS](/images/filter-css.png)