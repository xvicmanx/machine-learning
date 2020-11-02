# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='machine_learning',
  syntax='proto3',
  serialized_options=b'\n\030io.grpc.machine_learningB\017MachineLearningP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\x12\x10machine_learning\"%\n\x14PredictSalaryRequest\x12\r\n\x05years\x18\x01 \x01(\x05\"\'\n\x15PredictSalaryResponse\x12\x0e\n\x06salary\x18\x01 \x01(\x02\x32u\n\x0fMachineLearning\x12\x62\n\rPredictSalary\x12&.machine_learning.PredictSalaryRequest\x1a\'.machine_learning.PredictSalaryResponse\"\x00\x42-\n\x18io.grpc.machine_learningB\x0fMachineLearningP\x01\x62\x06proto3'
)




_PREDICTSALARYREQUEST = _descriptor.Descriptor(
  name='PredictSalaryRequest',
  full_name='machine_learning.PredictSalaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='years', full_name='machine_learning.PredictSalaryRequest.years', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=72,
)


_PREDICTSALARYRESPONSE = _descriptor.Descriptor(
  name='PredictSalaryResponse',
  full_name='machine_learning.PredictSalaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='salary', full_name='machine_learning.PredictSalaryResponse.salary', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['PredictSalaryRequest'] = _PREDICTSALARYREQUEST
DESCRIPTOR.message_types_by_name['PredictSalaryResponse'] = _PREDICTSALARYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictSalaryRequest = _reflection.GeneratedProtocolMessageType('PredictSalaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTSALARYREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:machine_learning.PredictSalaryRequest)
  })
_sym_db.RegisterMessage(PredictSalaryRequest)

PredictSalaryResponse = _reflection.GeneratedProtocolMessageType('PredictSalaryResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTSALARYRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:machine_learning.PredictSalaryResponse)
  })
_sym_db.RegisterMessage(PredictSalaryResponse)


DESCRIPTOR._options = None

_MACHINELEARNING = _descriptor.ServiceDescriptor(
  name='MachineLearning',
  full_name='machine_learning.MachineLearning',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=115,
  serialized_end=232,
  methods=[
  _descriptor.MethodDescriptor(
    name='PredictSalary',
    full_name='machine_learning.MachineLearning.PredictSalary',
    index=0,
    containing_service=None,
    input_type=_PREDICTSALARYREQUEST,
    output_type=_PREDICTSALARYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MACHINELEARNING)

DESCRIPTOR.services_by_name['MachineLearning'] = _MACHINELEARNING

# @@protoc_insertion_point(module_scope)
