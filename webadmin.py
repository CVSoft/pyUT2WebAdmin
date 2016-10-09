import httplib

from base64 import standard_b64encode as b64encode
from urllib import urlencode

class WebAdminAccess(object):
    def __init__(self, ip, port=80, auth='Admin:Admin'):
        if type(ip) == str: self.host = (ip, port)
        elif type(ip) == tuple: self.host = ip
        else: raise ValueError
        self.uwebserver = httplib.HTTPConnection(self.host[0], self.host[1])
        self.auth = auth

    def __enter__(self):
        return self

    def __exit__(self, et, ev, tb):
        return

    def load_auth(self):
        if ':' not in self.auth: raise ValueError
        return b64encode(self.auth)

    def console(self, s):
        """Sends s to server console"""
        msg = urlencode((("SendText", s), ("Send", "Send")), True)
        hdr = {"Authorization":"Basic %s" % self.load_auth(),
               "Content-Type":"application/x-www-form-urlencoded",
               "Accept":"text/html",
##               "Referer":"http://%s:%d/ServerAdmin/current_console_send" % \
##               self.host,
               "Content-Length":str(len(msg)),
               "Connection":"close"}
        self.uwebserver.request("POST", "/ServerAdmin/current_console",
                                msg, hdr)
        return self.uwebserver.getresponse()
