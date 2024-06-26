# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/routing/navigation_response.proto

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
from common.message.map import map_parking_space_pb2 as common_dot_message_dot_map_dot_map__parking__space__pb2
from common.message.routing import routing_pb2 as common_dot_message_dot_routing_dot_routing__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/routing/navigation_response.proto',
  package='citibot.common.routing',
  syntax='proto2',
  serialized_pb=_b('\n0common/message/routing/navigation_response.proto\x12\x16\x63itibot.common.routing\x1a\x1d\x63ommon/message/geometry.proto\x1a*common/message/map/map_parking_space.proto\x1a$common/message/routing/routing.proto\"P\n\x08NaviPath\x12\x12\n\npath_index\x18\x01 \x02(\x04\x12\x30\n\x06points\x18\x02 \x03(\x0b\x32 .citibot.common.message.PointLLH\"d\n\tNaviRoute\x12\x13\n\x0broute_index\x18\x01 \x02(\x04\x12\x11\n\tnum_paths\x18\x02 \x02(\x04\x12/\n\x05paths\x18\x03 \x03(\x0b\x32 .citibot.common.routing.NaviPath\"\xb7\x02\n\rNaviRoutePlan\x12\x18\n\x10route_plan_index\x18\x01 \x02(\x04\x12\x12\n\nnum_routes\x18\x02 \x02(\x04\x12\x31\n\x06routes\x18\x03 \x03(\x0b\x32!.citibot.common.routing.NaviRoute\x12\x38\n\x0bmeasurement\x18\x04 \x01(\x0b\x32#.citibot.common.routing.Measurement\x12:\n\x0eparking_spaces\x18\x05 \x03(\x0b\x32\".citibot.common.hdmap.ParkingSpace\x12O\n\x18\x63\x61ndidate_parking_spaces\x18\x06 \x01(\x0b\x32-.citibot.common.routing.CandidateParkingSpace\"\xbf\x01\n\x0eNaviRoutePlans\x12/\n\x05start\x18\x01 \x02(\x0b\x32 .citibot.common.message.PointLLH\x12-\n\x03\x65nd\x18\x02 \x02(\x0b\x32 .citibot.common.message.PointLLH\x12\x11\n\tnum_plans\x18\x03 \x02(\x04\x12:\n\x0broute_plans\x18\x04 \x03(\x0b\x32%.citibot.common.routing.NaviRoutePlan\"X\n\x12NavigationResponse\x12\x0b\n\x03msg\x18\x01 \x02(\t\x12\x35\n\x05plans\x18\x02 \x01(\x0b\x32&.citibot.common.routing.NaviRoutePlans')
  ,
  dependencies=[common_dot_message_dot_geometry__pb2.DESCRIPTOR,common_dot_message_dot_map_dot_map__parking__space__pb2.DESCRIPTOR,common_dot_message_dot_routing_dot_routing__pb2.DESCRIPTOR,])




_NAVIPATH = _descriptor.Descriptor(
  name='NaviPath',
  full_name='citibot.common.routing.NaviPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path_index', full_name='citibot.common.routing.NaviPath.path_index', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='points', full_name='citibot.common.routing.NaviPath.points', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=269,
)


_NAVIROUTE = _descriptor.Descriptor(
  name='NaviRoute',
  full_name='citibot.common.routing.NaviRoute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route_index', full_name='citibot.common.routing.NaviRoute.route_index', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_paths', full_name='citibot.common.routing.NaviRoute.num_paths', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paths', full_name='citibot.common.routing.NaviRoute.paths', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=271,
  serialized_end=371,
)


_NAVIROUTEPLAN = _descriptor.Descriptor(
  name='NaviRoutePlan',
  full_name='citibot.common.routing.NaviRoutePlan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route_plan_index', full_name='citibot.common.routing.NaviRoutePlan.route_plan_index', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_routes', full_name='citibot.common.routing.NaviRoutePlan.num_routes', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='routes', full_name='citibot.common.routing.NaviRoutePlan.routes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='measurement', full_name='citibot.common.routing.NaviRoutePlan.measurement', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parking_spaces', full_name='citibot.common.routing.NaviRoutePlan.parking_spaces', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candidate_parking_spaces', full_name='citibot.common.routing.NaviRoutePlan.candidate_parking_spaces', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=685,
)


_NAVIROUTEPLANS = _descriptor.Descriptor(
  name='NaviRoutePlans',
  full_name='citibot.common.routing.NaviRoutePlans',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='citibot.common.routing.NaviRoutePlans.start', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='citibot.common.routing.NaviRoutePlans.end', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_plans', full_name='citibot.common.routing.NaviRoutePlans.num_plans', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_plans', full_name='citibot.common.routing.NaviRoutePlans.route_plans', index=3,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=688,
  serialized_end=879,
)


_NAVIGATIONRESPONSE = _descriptor.Descriptor(
  name='NavigationResponse',
  full_name='citibot.common.routing.NavigationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='citibot.common.routing.NavigationResponse.msg', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plans', full_name='citibot.common.routing.NavigationResponse.plans', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=881,
  serialized_end=969,
)

_NAVIPATH.fields_by_name['points'].message_type = common_dot_message_dot_geometry__pb2._POINTLLH
_NAVIROUTE.fields_by_name['paths'].message_type = _NAVIPATH
_NAVIROUTEPLAN.fields_by_name['routes'].message_type = _NAVIROUTE
_NAVIROUTEPLAN.fields_by_name['measurement'].message_type = common_dot_message_dot_routing_dot_routing__pb2._MEASUREMENT
_NAVIROUTEPLAN.fields_by_name['parking_spaces'].message_type = common_dot_message_dot_map_dot_map__parking__space__pb2._PARKINGSPACE
_NAVIROUTEPLAN.fields_by_name['candidate_parking_spaces'].message_type = common_dot_message_dot_routing_dot_routing__pb2._CANDIDATEPARKINGSPACE
_NAVIROUTEPLANS.fields_by_name['start'].message_type = common_dot_message_dot_geometry__pb2._POINTLLH
_NAVIROUTEPLANS.fields_by_name['end'].message_type = common_dot_message_dot_geometry__pb2._POINTLLH
_NAVIROUTEPLANS.fields_by_name['route_plans'].message_type = _NAVIROUTEPLAN
_NAVIGATIONRESPONSE.fields_by_name['plans'].message_type = _NAVIROUTEPLANS
DESCRIPTOR.message_types_by_name['NaviPath'] = _NAVIPATH
DESCRIPTOR.message_types_by_name['NaviRoute'] = _NAVIROUTE
DESCRIPTOR.message_types_by_name['NaviRoutePlan'] = _NAVIROUTEPLAN
DESCRIPTOR.message_types_by_name['NaviRoutePlans'] = _NAVIROUTEPLANS
DESCRIPTOR.message_types_by_name['NavigationResponse'] = _NAVIGATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NaviPath = _reflection.GeneratedProtocolMessageType('NaviPath', (_message.Message,), dict(
  DESCRIPTOR = _NAVIPATH,
  __module__ = 'common.message.routing.navigation_response_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.routing.NaviPath)
  ))
_sym_db.RegisterMessage(NaviPath)

NaviRoute = _reflection.GeneratedProtocolMessageType('NaviRoute', (_message.Message,), dict(
  DESCRIPTOR = _NAVIROUTE,
  __module__ = 'common.message.routing.navigation_response_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.routing.NaviRoute)
  ))
_sym_db.RegisterMessage(NaviRoute)

NaviRoutePlan = _reflection.GeneratedProtocolMessageType('NaviRoutePlan', (_message.Message,), dict(
  DESCRIPTOR = _NAVIROUTEPLAN,
  __module__ = 'common.message.routing.navigation_response_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.routing.NaviRoutePlan)
  ))
_sym_db.RegisterMessage(NaviRoutePlan)

NaviRoutePlans = _reflection.GeneratedProtocolMessageType('NaviRoutePlans', (_message.Message,), dict(
  DESCRIPTOR = _NAVIROUTEPLANS,
  __module__ = 'common.message.routing.navigation_response_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.routing.NaviRoutePlans)
  ))
_sym_db.RegisterMessage(NaviRoutePlans)

NavigationResponse = _reflection.GeneratedProtocolMessageType('NavigationResponse', (_message.Message,), dict(
  DESCRIPTOR = _NAVIGATIONRESPONSE,
  __module__ = 'common.message.routing.navigation_response_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.routing.NavigationResponse)
  ))
_sym_db.RegisterMessage(NavigationResponse)


# @@protoc_insertion_point(module_scope)
