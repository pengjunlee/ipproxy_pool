# -*- coding: utf-8 -*-
import re
import time
from settings import PROXY_URL_FORMATTER

schema_pattern = re.compile(r'http|https$', re.I)
ip_pattern = re.compile(r'^([0-9]{1,3}.){3}[0-9]{1,3}$', re.I)
port_pattern = re.compile(r'^[0-9]{2,5}$', re.I)

class IPProxy:
    '''
    {
        "schema": "http",
        "ip": "127.0.0.1",
        "port": "8050",
        "used_total": 11,
        "success_times": 5,
        "continuous_failed": 3,
        "created_time": "2018-05-02"
    }

    '''

    def __init__(self, schema, ip, port, used_total=0, success_times=0, continuous_failed=0,
                 created_time=None):
        """Initialize the proxy instance"""
        if schema == "" or schema is None:
            schema = "http"
        self.schema = schema.lower()
        self.ip = ip
        self.port = port
        self.used_total = used_total
        self.success_times = success_times
        self.continuous_failed = continuous_failed
        if created_time is None:
            created_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.created_time = created_time

    def _get_url(self):
        ''' Return the proxy url'''
        return PROXY_URL_FORMATTER % {'schema': self.schema, 'ip': self.ip, 'port': self.port}

    def _check_format(self):
        ''' Return True if the proxy fields are well-formed,otherwise return False'''
        if self.schema is not None and self.ip is not None and self.port is not None:
            if schema_pattern.match(self.schema) and ip_pattern.match(self.ip) and port_pattern.match(self.port):
                return True
        return False

    def _is_https(self):
        ''' Return True if the proxy is https,otherwise return False'''
        return self.schema == 'https'


if __name__ == '__main__':
    proxy = IPProxy('HTTPS', '1922.168.2.25', "8080")
    print(proxy._get_url())
    print(proxy._check_format())
    print(proxy._is_https())
