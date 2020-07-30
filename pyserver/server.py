import chat.views as repository
import user_pb2_grpc
import logging

class ChatServicer(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        try:
            userresponse = repository.user_lookup(request)
            return userresponse
        except Exception as e:
            logging.error(e)
