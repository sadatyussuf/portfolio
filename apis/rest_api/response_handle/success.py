from rest_framework.response import Response as response
from rest_framework import status
from datetime import datetime


class Response(response):

    default_message = "Response Successful"
    default_data = []

    def __init__(self, data=None, status=None,message=None, **kwargs):
        if message is None:
            message = self.default_message

        if data is None:
            data = self.default_data
        if not isinstance(data, list) and data is not None:
            data = [data]

        # self.detail = {
        res = {
            "success": True,
            "status": status,
            "message": message,
            "data": data,
            "current_time": datetime.now().isoformat(),
        }
        super().__init__(res, status=status, **kwargs)