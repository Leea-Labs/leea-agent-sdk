# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protocol.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'protocol.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eprotocol.proto\x12\x0eleea_agent_sdk\"\xc9\x01\n\x08\x45nvelope\x12\x32\n\x04Type\x18\x01 \x01(\x0e\x32$.leea_agent_sdk.Envelope.MessageType\x12\x0f\n\x07Payload\x18\x02 \x01(\x0c\"x\n\x0bMessageType\x12\x0e\n\nAgentHello\x10\x00\x12\x0f\n\x0bServerHello\x10\x01\x12\x14\n\x10\x45xecutionRequest\x10\x64\x12\x13\n\x0f\x45xecutionResult\x10\x65\x12\x11\n\rExecutionStep\x10\x66\x12\n\n\x05\x45rror\x10\xf4\x03\"Z\n\nAgentHello\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x02 \x01(\t\x12\x13\n\x0bInputSchema\x18\x03 \x01(\t\x12\x14\n\x0cOutputSchema\x18\x04 \x01(\t\"\r\n\x0bServerHello\"+\n\x05\x45rror\x12\x11\n\tRequestID\x18\x01 \x01(\t\x12\x0f\n\x07Message\x18\x02 \x01(\t\"E\n\x10\x45xecutionRequest\x12\x11\n\tRequestID\x18\x01 \x01(\t\x12\x0f\n\x07\x41gentID\x18\x02 \x01(\t\x12\r\n\x05Input\x18\x03 \x01(\t\"3\n\rExecutionStep\x12\x11\n\tRequestID\x18\x01 \x01(\t\x12\x0f\n\x07Message\x18\x02 \x01(\t\"J\n\x0f\x45xecutionResult\x12\x11\n\tRequestID\x18\x01 \x01(\t\x12\x14\n\x0cIsSuccessful\x18\x02 \x01(\x08\x12\x0e\n\x06Result\x18\x03 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protocol_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENVELOPE']._serialized_start=35
  _globals['_ENVELOPE']._serialized_end=236
  _globals['_ENVELOPE_MESSAGETYPE']._serialized_start=116
  _globals['_ENVELOPE_MESSAGETYPE']._serialized_end=236
  _globals['_AGENTHELLO']._serialized_start=238
  _globals['_AGENTHELLO']._serialized_end=328
  _globals['_SERVERHELLO']._serialized_start=147
  _globals['_SERVERHELLO']._serialized_end=160
  _globals['_ERROR']._serialized_start=345
  _globals['_ERROR']._serialized_end=388
  _globals['_EXECUTIONREQUEST']._serialized_start=390
  _globals['_EXECUTIONREQUEST']._serialized_end=459
  _globals['_EXECUTIONSTEP']._serialized_start=461
  _globals['_EXECUTIONSTEP']._serialized_end=512
  _globals['_EXECUTIONRESULT']._serialized_start=514
  _globals['_EXECUTIONRESULT']._serialized_end=588
# @@protoc_insertion_point(module_scope)
