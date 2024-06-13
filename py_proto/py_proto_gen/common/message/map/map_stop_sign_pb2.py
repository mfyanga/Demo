# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/map/map_stop_sign.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.message.map import map_id_pb2 as common_dot_message_dot_map_dot_map__id__pb2
from common.message.map import map_geometry_pb2 as common_dot_message_dot_map_dot_map__geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/map/map_stop_sign.proto',
  package='citibot.common.hdmap',
  syntax='proto2',
  serialized_pb=_b('\n&common/message/map/map_stop_sign.proto\x12\x14\x63itibot.common.hdmap\x1a\x1f\x63ommon/message/map/map_id.proto\x1a%common/message/map/map_geometry.proto\"\xa2\x02\n\x08StopSign\x12$\n\x02id\x18\x01 \x01(\x0b\x32\x18.citibot.common.hdmap.Id\x12.\n\tstop_line\x18\x02 \x03(\x0b\x32\x1b.citibot.common.hdmap.Curve\x12,\n\noverlap_id\x18\x03 \x03(\x0b\x32\x18.citibot.common.hdmap.Id\x12\x35\n\x04type\x18\x04 \x01(\x0e\x32\'.citibot.common.hdmap.StopSign.StopType\"[\n\x08StopType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07ONE_WAY\x10\x01\x12\x0b\n\x07TWO_WAY\x10\x02\x12\r\n\tTHREE_WAY\x10\x03\x12\x0c\n\x08\x46OUR_WAY\x10\x04\x12\x0b\n\x07\x41LL_WAY\x10\x05')
  ,
  dependencies=[common_dot_message_dot_map_dot_map__id__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__geometry__pb2.DESCRIPTOR,])



_STOPSIGN_STOPTYPE = _descriptor.EnumDescriptor(
  name='StopType',
  full_name='citibot.common.hdmap.StopSign.StopType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONE_WAY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWO_WAY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THREE_WAY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOUR_WAY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALL_WAY', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=336,
  serialized_end=427,
)
_sym_db.RegisterEnumDescriptor(_STOPSIGN_STOPTYPE)


_STOPSIGN = _descriptor.Descriptor(
  name='StopSign',
  full_name='citibot.common.hdmap.StopSign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='citibot.common.hdmap.StopSign.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_line', full_name='citibot.common.hdmap.StopSign.stop_line', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlap_id', full_name='citibot.common.hdmap.StopSign.overlap_id', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='citibot.common.hdmap.StopSign.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STOPSIGN_STOPTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=427,
)

_STOPSIGN.fields_by_name['id'].message_type = common_dot_message_dot_map_dot_map__id__pb2._ID
_STOPSIGN.fields_by_name['stop_line'].message_type = common_dot_message_dot_map_dot_map__geometry__pb2._CURVE
_STOPSIGN.fields_by_name['overlap_id'].message_type = common_dot_message_dot_map_dot_map__id__pb2._ID
_STOPSIGN.fields_by_name['type'].enum_type = _STOPSIGN_STOPTYPE
_STOPSIGN_STOPTYPE.containing_type = _STOPSIGN
DESCRIPTOR.message_types_by_name['StopSign'] = _STOPSIGN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StopSign = _reflection.GeneratedProtocolMessageType('StopSign', (_message.Message,), dict(
  DESCRIPTOR = _STOPSIGN,
  __module__ = 'common.message.map.map_stop_sign_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.StopSign)
  ))
_sym_db.RegisterMessage(StopSign)


# @@protoc_insertion_point(module_scope)
