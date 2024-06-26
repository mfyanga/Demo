# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/map/map_mark_point.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.message import geometry_pb2 as common_dot_message_dot_geometry__pb2
from common.message.map import map_id_pb2 as common_dot_message_dot_map_dot_map__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/map/map_mark_point.proto',
  package='citibot.common.hdmap',
  syntax='proto2',
  serialized_pb=_b('\n\'common/message/map/map_mark_point.proto\x12\x14\x63itibot.common.hdmap\x1a\x1d\x63ommon/message/geometry.proto\x1a\x1f\x63ommon/message/map/map_id.proto\"\xbc\x02\n\tMarkPoint\x12$\n\x02id\x18\x01 \x01(\x0b\x32\x18.citibot.common.hdmap.Id\x12\x32\n\x04type\x18\x02 \x01(\x0e\x32$.citibot.common.hdmap.MarkPoint.Type\x12\x32\n\x08position\x18\x03 \x01(\x0b\x32 .citibot.common.message.PointENU\x12,\n\noverlap_id\x18\x04 \x03(\x0b\x32\x18.citibot.common.hdmap.Id\"s\n\x04Type\x12\x11\n\rENTRANCE_RAMP\x10\x01\x12\x10\n\x0cTOLL_GATE_IN\x10\x02\x12\x11\n\rTOLL_GATE_OUT\x10\x03\x12\r\n\tTUNNEL_IN\x10\x04\x12\x0e\n\nTUNNEL_OUT\x10\x05\x12\x14\n\x10RAMP_ENTRY_POINT\x10\x06')
  ,
  dependencies=[common_dot_message_dot_geometry__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__id__pb2.DESCRIPTOR,])



_MARKPOINT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='citibot.common.hdmap.MarkPoint.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENTRANCE_RAMP', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOLL_GATE_IN', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOLL_GATE_OUT', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TUNNEL_IN', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TUNNEL_OUT', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAMP_ENTRY_POINT', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=331,
  serialized_end=446,
)
_sym_db.RegisterEnumDescriptor(_MARKPOINT_TYPE)


_MARKPOINT = _descriptor.Descriptor(
  name='MarkPoint',
  full_name='citibot.common.hdmap.MarkPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='citibot.common.hdmap.MarkPoint.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='citibot.common.hdmap.MarkPoint.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='citibot.common.hdmap.MarkPoint.position', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlap_id', full_name='citibot.common.hdmap.MarkPoint.overlap_id', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MARKPOINT_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=446,
)

_MARKPOINT.fields_by_name['id'].message_type = common_dot_message_dot_map_dot_map__id__pb2._ID
_MARKPOINT.fields_by_name['type'].enum_type = _MARKPOINT_TYPE
_MARKPOINT.fields_by_name['position'].message_type = common_dot_message_dot_geometry__pb2._POINTENU
_MARKPOINT.fields_by_name['overlap_id'].message_type = common_dot_message_dot_map_dot_map__id__pb2._ID
_MARKPOINT_TYPE.containing_type = _MARKPOINT
DESCRIPTOR.message_types_by_name['MarkPoint'] = _MARKPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MarkPoint = _reflection.GeneratedProtocolMessageType('MarkPoint', (_message.Message,), dict(
  DESCRIPTOR = _MARKPOINT,
  __module__ = 'common.message.map.map_mark_point_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.hdmap.MarkPoint)
  ))
_sym_db.RegisterMessage(MarkPoint)


# @@protoc_insertion_point(module_scope)
