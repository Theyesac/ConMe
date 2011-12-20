"""Base classes for view handlers."""

class Handler(object):
    def __init__(self, request):
        self.request = request
