# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chatserver.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63hatserver.proto\x12\x0c\x63hat_service\"G\n\x0bMessageData\x12\x0c\n\x04remt\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65st\x18\x02 \x01(\t\x12\x0f\n\x07ip_dest\x18\x03 \x01(\t\x12\x0b\n\x03msg\x18\x04 \x01(\t\" \n\rStatusMessage\x12\x0f\n\x07message\x18\x01 \x01(\t2\x9e\x01\n\x07Message\x12G\n\x0bSendMessage\x12\x19.chat_service.MessageData\x1a\x1b.chat_service.StatusMessage\"\x00\x12J\n\x0e\x46orwardMessage\x12\x19.chat_service.MessageData\x1a\x1b.chat_service.StatusMessage\"\x00\x42+\n\x15io.grpc.examples.chatB\x0b\x43hatServiceP\x01\xa2\x02\x02\x43Sb\x06proto3')



_MESSAGEDATA = DESCRIPTOR.message_types_by_name['MessageData']
_STATUSMESSAGE = DESCRIPTOR.message_types_by_name['StatusMessage']
MessageData = _reflection.GeneratedProtocolMessageType('MessageData', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEDATA,
  '__module__' : 'chatserver_pb2'
  # @@protoc_insertion_point(class_scope:chat_service.MessageData)
  })
_sym_db.RegisterMessage(MessageData)

StatusMessage = _reflection.GeneratedProtocolMessageType('StatusMessage', (_message.Message,), {
  'DESCRIPTOR' : _STATUSMESSAGE,
  '__module__' : 'chatserver_pb2'
  # @@protoc_insertion_point(class_scope:chat_service.StatusMessage)
  })
_sym_db.RegisterMessage(StatusMessage)

_MESSAGE = DESCRIPTOR.services_by_name['Message']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025io.grpc.examples.chatB\013ChatServiceP\001\242\002\002CS'
  _MESSAGEDATA._serialized_start=34
  _MESSAGEDATA._serialized_end=105
  _STATUSMESSAGE._serialized_start=107
  _STATUSMESSAGE._serialized_end=139
  _MESSAGE._serialized_start=142
  _MESSAGE._serialized_end=300
# @@protoc_insertion_point(module_scope)