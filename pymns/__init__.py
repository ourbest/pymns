from pymns.mns_client import MNSClient

__version__ = '0.1.3'


def connect(ak, sk, endpoint, queue_name):
    return MNSClient(ak, sk, endpoint, queue_name)
