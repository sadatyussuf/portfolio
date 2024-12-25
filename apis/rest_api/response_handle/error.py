from rest_framework.views import exception_handler
import datetime


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler
    response = exception_handler(exc, context)


    # add HTTP status code to the response.
    if response is not None:
        print(response.__dict__)
        custom_response_data = {
            "success": False,
            "status": response.status_code,
            "data": response.data,
            "current_time": datetime.datetime.now().isoformat(),
        }
        response.data = custom_response_data

    return response



# from rest_framework.exceptions import APIException
# from rest_framework import status
# from datetime import datetime


# class CustomValidationError(APIException):
#     status_code = status.HTTP_400_BAD_REQUEST
#     default_detail = "Validation error."

#     def __init__(self, detail=None, code=None):
#         if detail is None:
#             detail = self.default_detail
#         if code is None:
#             code = self.status_code

#         # Get the current time
#         current_time = datetime.now().isoformat()

#         # Format the error detail
#         self.detail = {
#             "status": "error",
#             "status_code": self.status_code,
#             "message": detail if isinstance(detail, str) else "Validation error.",
#             "errors": [
#                 {
#                     "code": code,
#                     "details": (
#                         detail
#                         if isinstance(detail, str)
#                         else detail.get("details", "Validation error.")
#                     ),
#                 }
#             ],
#             "current_time": current_time,
#         }




