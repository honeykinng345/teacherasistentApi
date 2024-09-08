from quart import jsonify


class JsonResponse:

    @classmethod
    def getErrorResponse(cls, message, code):
        return jsonify({"response": None, "error": message}), code

    @classmethod
    def getSuccessResponse(cls, result, message, error, code):
        return jsonify({"response": result, "message": message,}), code
