# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chatserver_pb2 as chatserver__pb2


class MessageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessage = channel.unary_unary(
                '/chat_service.Message/SendMessage',
                request_serializer=chatserver__pb2.MessageData.SerializeToString,
                response_deserializer=chatserver__pb2.StatusMessage.FromString,
                )
        self.ForwardMessage = channel.unary_unary(
                '/chat_service.Message/ForwardMessage',
                request_serializer=chatserver__pb2.MessageData.SerializeToString,
                response_deserializer=chatserver__pb2.StatusMessage.FromString,
                )


class MessageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ForwardMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=chatserver__pb2.MessageData.FromString,
                    response_serializer=chatserver__pb2.StatusMessage.SerializeToString,
            ),
            'ForwardMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.ForwardMessage,
                    request_deserializer=chatserver__pb2.MessageData.FromString,
                    response_serializer=chatserver__pb2.StatusMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chat_service.Message', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Message(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat_service.Message/SendMessage',
            chatserver__pb2.MessageData.SerializeToString,
            chatserver__pb2.StatusMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ForwardMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat_service.Message/ForwardMessage',
            chatserver__pb2.MessageData.SerializeToString,
            chatserver__pb2.StatusMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)