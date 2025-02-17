import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

# TODO
# this could be set up directly on the config endpoints.json file but it should involve major changes on code parts
# where we read, parse and extract values from endpoints.json
SUPPRESS_WARNING_ENVS = ['dtl2']


def suppress_insecure_request_warns(env) -> bool:
    """
    this methods suppress InsecureRequestWarnings caused by the SUPPRESS_WARNING_ENVS list environments and return bool
    whether requests must verify ssl or not

    InsecureRequestWarning: Unverified HTTPS request is being made to host 'inscurehost.com'.
    Adding certificate verification is strongly advised.
    See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    """
    verify = True
    if env in SUPPRESS_WARNING_ENVS:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        verify = False
    return verify
