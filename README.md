# Filter OPTIONS Method
[![Version](https://img.shields.io/badge/Version-v1.2-green.svg)]()
[![Language](https://img.shields.io/badge/Language-Python-orange.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](https://github.com/capt-meelo/filter-options-method/blob/master/LICENSE)


A Burp extension that filters out `OPTIONS` requests from populating Burp's Proxy history. This extension works by doing the following:

1. Force the `Content-Type` header value to `text/css; charset=UTF-8`.
2. Comment out the entire response body so Burp will not recognize the MIME type incorrectly.

A post about this extension can be found [post](https://captmeelo.com/pentest/2020/01/06/filter-options-method.html).

# Installation

## Via Burp Store

Install the extension from the [BApp Store](https://portswigger.net/bappstore/fa14ac579cff4682b32f39af8d3651e7).

## Manually

1. Download [burp-filter-options-method.py](filter-options-method.py) to your machine.
2. Go to _**Extender > Extensions**_ tab, then click on the _**Add**_ button. On the new window, browse the location of **burp-filter-options-method.py** and click the _**Next**_ button.
![Load Extension](/images/load-extension.png)


## How to Use

To filter out these `OPTIONS` requests, go to _**HTTP history > Filter by MIME type**_, and untick the _**CSS**_ checkbox.
![Filter CSS](/images/filter-css.png)
