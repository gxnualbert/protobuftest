# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: as-proto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='as-proto.proto',
  package='fsp.sss.proto',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x61s-proto.proto\x12\rfsp.sss.proto\"2\n\x08LoginReq\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x13\n\x0buser_passwd\x18\x02 \x01(\t\"4\n\x08LoginRep\x12\x12\n\nerror_code\x18\x01 \x01(\r\x12\x14\n\x0c\x63lient_token\x18\x02 \x01(\t\"\x1f\n\tLogoutRep\x12\x12\n\nerror_code\x18\x01 \x01(\r\"{\n\x11\x41pplyForStreamReq\x12.\n\x0bstream_type\x18\x01 \x01(\x0e\x32\x19.fsp.sss.proto.StreamType\x12\x36\n\x0fstream_property\x18\x02 \x01(\x0e\x32\x1d.fsp.sss.proto.StreamProperty\"X\n\x11\x41pplyForStreamRep\x12\x12\n\nerror_code\x18\x01 \x01(\r\x12\x11\n\tstream_id\x18\x02 \x01(\t\x12\x1c\n\x14stream_publish_token\x18\x03 \x01(\t\"3\n\x1eUpwardNotifyStreamPublishedReq\x12\x11\n\tstream_id\x18\x01 \x01(\t\"4\n\x1eUpwardNotifyStreamPublishedRep\x12\x12\n\nerror_code\x18\x01 \x01(\r\"\x85\x01\n DownwardNotifyStreamPublishedReq\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12.\n\x0bstream_type\x18\x02 \x01(\x0e\x32\x19.fsp.sss.proto.StreamType\x12\x1e\n\x16stream_subscribe_token\x18\x03 \x01(\t\"6\n DownwardNotifyStreamPublishedRep\x12\x12\n\nerror_code\x18\x01 \x01(\r*\xce\x02\n\rInterfaceType\x12\x0f\n\x0bTypeUnknown\x10\x00\x12\x11\n\x0cTypeLoginReq\x10\xe8\x07\x12\x11\n\x0cTypeLoginRep\x10\xe9\x07\x12\x12\n\rTypeLogoutReq\x10\xea\x07\x12\x12\n\rTypeLogoutRep\x10\xeb\x07\x12\x1a\n\x15TypeApplyForStreamReq\x10\xec\x07\x12\x1a\n\x15TypeApplyForStreamRep\x10\xed\x07\x12\'\n\"TypeUpwardNotifyStreamPublishedReq\x10\xee\x07\x12\'\n\"TypeUpwardNotifyStreamPublishedRep\x10\xef\x07\x12)\n$TypeDownwardNotifyStreamPublishedReq\x10\xf0\x07\x12)\n$TypeDownwardNotifyStreamPublishedRep\x10\xf1\x07*/\n\nStreamType\x12\t\n\x05Video\x10\x00\x12\t\n\x05\x41udio\x10\x01\x12\x0b\n\x07\x44\x65sktop\x10\x02*.\n\x0eStreamProperty\x12\x0c\n\x08Reliable\x10\x00\x12\x0e\n\nUnreliable\x10\x01\x42\t\xf8\x01\x01\xa2\x02\x03GPBb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_INTERFACETYPE = _descriptor.EnumDescriptor(
  name='InterfaceType',
  full_name='fsp.sss.proto.InterfaceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TypeUnknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TypeLoginReq', index=1, number=1000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TypeLoginRep', index=2, number=1001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TypeLogoutReq', index=3, number=1002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TypeLogoutRep', index=4, number=1003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TypeApplyForStreamReq', index=5, number=1004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TypeApplyForStreamRep', index=6, number=1005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TypeUpwardNotifyStreamPublishedReq', index=7, number=1006,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TypeUpwardNotifyStreamPublishedRep', index=8, number=1007,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TypeDownwardNotifyStreamPublishedReq', index=9, number=1008,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TypeDownwardNotifyStreamPublishedRep', index=10, number=1009,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=687,
  serialized_end=1021,
)
_sym_db.RegisterEnumDescriptor(_INTERFACETYPE)

InterfaceType = enum_type_wrapper.EnumTypeWrapper(_INTERFACETYPE)
_STREAMTYPE = _descriptor.EnumDescriptor(
  name='StreamType',
  full_name='fsp.sss.proto.StreamType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Video', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Audio', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Desktop', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1023,
  serialized_end=1070,
)
_sym_db.RegisterEnumDescriptor(_STREAMTYPE)

StreamType = enum_type_wrapper.EnumTypeWrapper(_STREAMTYPE)
_STREAMPROPERTY = _descriptor.EnumDescriptor(
  name='StreamProperty',
  full_name='fsp.sss.proto.StreamProperty',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Reliable', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unreliable', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1072,
  serialized_end=1118,
)
_sym_db.RegisterEnumDescriptor(_STREAMPROPERTY)

StreamProperty = enum_type_wrapper.EnumTypeWrapper(_STREAMPROPERTY)
TypeUnknown = 0
TypeLoginReq = 1000
TypeLoginRep = 1001
TypeLogoutReq = 1002
TypeLogoutRep = 1003
TypeApplyForStreamReq = 1004
TypeApplyForStreamRep = 1005
TypeUpwardNotifyStreamPublishedReq = 1006
TypeUpwardNotifyStreamPublishedRep = 1007
TypeDownwardNotifyStreamPublishedReq = 1008
TypeDownwardNotifyStreamPublishedRep = 1009
Video = 0
Audio = 1
Desktop = 2
Reliable = 0
Unreliable = 1



_LOGINREQ = _descriptor.Descriptor(
  name='LoginReq',
  full_name='fsp.sss.proto.LoginReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='fsp.sss.proto.LoginReq.user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_passwd', full_name='fsp.sss.proto.LoginReq.user_passwd', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=83,
)


_LOGINREP = _descriptor.Descriptor(
  name='LoginRep',
  full_name='fsp.sss.proto.LoginRep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='fsp.sss.proto.LoginRep.error_code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_token', full_name='fsp.sss.proto.LoginRep.client_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=137,
)


_LOGOUTREP = _descriptor.Descriptor(
  name='LogoutRep',
  full_name='fsp.sss.proto.LogoutRep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='fsp.sss.proto.LogoutRep.error_code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=170,
)


_APPLYFORSTREAMREQ = _descriptor.Descriptor(
  name='ApplyForStreamReq',
  full_name='fsp.sss.proto.ApplyForStreamReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_type', full_name='fsp.sss.proto.ApplyForStreamReq.stream_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_property', full_name='fsp.sss.proto.ApplyForStreamReq.stream_property', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=295,
)


_APPLYFORSTREAMREP = _descriptor.Descriptor(
  name='ApplyForStreamRep',
  full_name='fsp.sss.proto.ApplyForStreamRep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='fsp.sss.proto.ApplyForStreamRep.error_code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='fsp.sss.proto.ApplyForStreamRep.stream_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_publish_token', full_name='fsp.sss.proto.ApplyForStreamRep.stream_publish_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=385,
)


_UPWARDNOTIFYSTREAMPUBLISHEDREQ = _descriptor.Descriptor(
  name='UpwardNotifyStreamPublishedReq',
  full_name='fsp.sss.proto.UpwardNotifyStreamPublishedReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='fsp.sss.proto.UpwardNotifyStreamPublishedReq.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=438,
)


_UPWARDNOTIFYSTREAMPUBLISHEDREP = _descriptor.Descriptor(
  name='UpwardNotifyStreamPublishedRep',
  full_name='fsp.sss.proto.UpwardNotifyStreamPublishedRep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='fsp.sss.proto.UpwardNotifyStreamPublishedRep.error_code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=492,
)


_DOWNWARDNOTIFYSTREAMPUBLISHEDREQ = _descriptor.Descriptor(
  name='DownwardNotifyStreamPublishedReq',
  full_name='fsp.sss.proto.DownwardNotifyStreamPublishedReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='fsp.sss.proto.DownwardNotifyStreamPublishedReq.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_type', full_name='fsp.sss.proto.DownwardNotifyStreamPublishedReq.stream_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_subscribe_token', full_name='fsp.sss.proto.DownwardNotifyStreamPublishedReq.stream_subscribe_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=628,
)


_DOWNWARDNOTIFYSTREAMPUBLISHEDREP = _descriptor.Descriptor(
  name='DownwardNotifyStreamPublishedRep',
  full_name='fsp.sss.proto.DownwardNotifyStreamPublishedRep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='fsp.sss.proto.DownwardNotifyStreamPublishedRep.error_code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=630,
  serialized_end=684,
)

_APPLYFORSTREAMREQ.fields_by_name['stream_type'].enum_type = _STREAMTYPE
_APPLYFORSTREAMREQ.fields_by_name['stream_property'].enum_type = _STREAMPROPERTY
_DOWNWARDNOTIFYSTREAMPUBLISHEDREQ.fields_by_name['stream_type'].enum_type = _STREAMTYPE
DESCRIPTOR.message_types_by_name['LoginReq'] = _LOGINREQ
DESCRIPTOR.message_types_by_name['LoginRep'] = _LOGINREP
DESCRIPTOR.message_types_by_name['LogoutRep'] = _LOGOUTREP
DESCRIPTOR.message_types_by_name['ApplyForStreamReq'] = _APPLYFORSTREAMREQ
DESCRIPTOR.message_types_by_name['ApplyForStreamRep'] = _APPLYFORSTREAMREP
DESCRIPTOR.message_types_by_name['UpwardNotifyStreamPublishedReq'] = _UPWARDNOTIFYSTREAMPUBLISHEDREQ
DESCRIPTOR.message_types_by_name['UpwardNotifyStreamPublishedRep'] = _UPWARDNOTIFYSTREAMPUBLISHEDREP
DESCRIPTOR.message_types_by_name['DownwardNotifyStreamPublishedReq'] = _DOWNWARDNOTIFYSTREAMPUBLISHEDREQ
DESCRIPTOR.message_types_by_name['DownwardNotifyStreamPublishedRep'] = _DOWNWARDNOTIFYSTREAMPUBLISHEDREP
DESCRIPTOR.enum_types_by_name['InterfaceType'] = _INTERFACETYPE
DESCRIPTOR.enum_types_by_name['StreamType'] = _STREAMTYPE
DESCRIPTOR.enum_types_by_name['StreamProperty'] = _STREAMPROPERTY

LoginReq = _reflection.GeneratedProtocolMessageType('LoginReq', (_message.Message,), dict(
  DESCRIPTOR = _LOGINREQ,
  __module__ = 'as_proto_pb2'
  # @@protoc_insertion_point(class_scope:fsp.sss.proto.LoginReq)
  ))
_sym_db.RegisterMessage(LoginReq)

LoginRep = _reflection.GeneratedProtocolMessageType('LoginRep', (_message.Message,), dict(
  DESCRIPTOR = _LOGINREP,
  __module__ = 'as_proto_pb2'
  # @@protoc_insertion_point(class_scope:fsp.sss.proto.LoginRep)
  ))
_sym_db.RegisterMessage(LoginRep)

LogoutRep = _reflection.GeneratedProtocolMessageType('LogoutRep', (_message.Message,), dict(
  DESCRIPTOR = _LOGOUTREP,
  __module__ = 'as_proto_pb2'
  # @@protoc_insertion_point(class_scope:fsp.sss.proto.LogoutRep)
  ))
_sym_db.RegisterMessage(LogoutRep)

ApplyForStreamReq = _reflection.GeneratedProtocolMessageType('ApplyForStreamReq', (_message.Message,), dict(
  DESCRIPTOR = _APPLYFORSTREAMREQ,
  __module__ = 'as_proto_pb2'
  # @@protoc_insertion_point(class_scope:fsp.sss.proto.ApplyForStreamReq)
  ))
_sym_db.RegisterMessage(ApplyForStreamReq)

ApplyForStreamRep = _reflection.GeneratedProtocolMessageType('ApplyForStreamRep', (_message.Message,), dict(
  DESCRIPTOR = _APPLYFORSTREAMREP,
  __module__ = 'as_proto_pb2'
  # @@protoc_insertion_point(class_scope:fsp.sss.proto.ApplyForStreamRep)
  ))
_sym_db.RegisterMessage(ApplyForStreamRep)

UpwardNotifyStreamPublishedReq = _reflection.GeneratedProtocolMessageType('UpwardNotifyStreamPublishedReq', (_message.Message,), dict(
  DESCRIPTOR = _UPWARDNOTIFYSTREAMPUBLISHEDREQ,
  __module__ = 'as_proto_pb2'
  # @@protoc_insertion_point(class_scope:fsp.sss.proto.UpwardNotifyStreamPublishedReq)
  ))
_sym_db.RegisterMessage(UpwardNotifyStreamPublishedReq)

UpwardNotifyStreamPublishedRep = _reflection.GeneratedProtocolMessageType('UpwardNotifyStreamPublishedRep', (_message.Message,), dict(
  DESCRIPTOR = _UPWARDNOTIFYSTREAMPUBLISHEDREP,
  __module__ = 'as_proto_pb2'
  # @@protoc_insertion_point(class_scope:fsp.sss.proto.UpwardNotifyStreamPublishedRep)
  ))
_sym_db.RegisterMessage(UpwardNotifyStreamPublishedRep)

DownwardNotifyStreamPublishedReq = _reflection.GeneratedProtocolMessageType('DownwardNotifyStreamPublishedReq', (_message.Message,), dict(
  DESCRIPTOR = _DOWNWARDNOTIFYSTREAMPUBLISHEDREQ,
  __module__ = 'as_proto_pb2'
  # @@protoc_insertion_point(class_scope:fsp.sss.proto.DownwardNotifyStreamPublishedReq)
  ))
_sym_db.RegisterMessage(DownwardNotifyStreamPublishedReq)

DownwardNotifyStreamPublishedRep = _reflection.GeneratedProtocolMessageType('DownwardNotifyStreamPublishedRep', (_message.Message,), dict(
  DESCRIPTOR = _DOWNWARDNOTIFYSTREAMPUBLISHEDREP,
  __module__ = 'as_proto_pb2'
  # @@protoc_insertion_point(class_scope:fsp.sss.proto.DownwardNotifyStreamPublishedRep)
  ))
_sym_db.RegisterMessage(DownwardNotifyStreamPublishedRep)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001\242\002\003GPB'))
# @@protoc_insertion_point(module_scope)