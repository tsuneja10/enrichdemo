
class APIResponseParser:
    """
    ApiResponseParser
    Common api Response Parser for all API Response.
    """

    def __init__(self):
        pass

    @staticmethod
    def response(**api_response_data):
        """
        kwargs: all Kwargs Parameter comes from to APIView Class.
        return: Response
        """
        try:
            if api_response_data['status']:
                return Response(
                    {
                        'status': api_response_data['status'],
                        'message': api_response_data['message'],
                        api_response_data['result']: api_response_data['data'],
                    }
                )
            return Response(
                {
                    'message': api_response_data['message'],
                    'status': False
                }
            )
        except Exception as msg:
            return Response(
                {
                    'message': "Data not found",
                    'errors': str(msg),
                    'status': False
                }
            )

    @staticmethod
    def responses(**api_response_data):
        """
        kwargs: all Kwargs Parameter comes from to APIView Class.
        return: Response
        """
        json_response = {}
        try:
            if api_response_data['status']:
                for key, values in api_response_data['data'].items():
                    json_response[key] = values
                json_response['message'] = api_response_data['message']
                json_response['status'] = api_response_data['status']
                return Response(json_response)
            return Response(
                {
                    'message': api_response_data['message'],
                    'status': False
                }
            )
        except Exception as msg:
            return Response(
                {
                    'message': "Data not found",
                    'errors': str(msg),
                    'status': False
                }
            )