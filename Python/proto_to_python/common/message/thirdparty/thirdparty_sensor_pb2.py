# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/thirdparty/thirdparty_sensor.proto

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


from common.message.dispatch import cloud_message_pb2 as common_dot_message_dot_dispatch_dot_cloud__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/thirdparty/thirdparty_sensor.proto',
  package='citibot.common',
  syntax='proto2',
  serialized_pb=_b('\n1common/message/thirdparty/thirdparty_sensor.proto\x12\x0e\x63itibot.common\x1a+common/message/dispatch/cloud_message.proto\"\xcc\x01\n\x15ThirdPartySensorProto\x12\x44\n\x11\x64ispatch_obstacle\x18\x01 \x03(\x0b\x32).citibot.common.dispatch.DispatchObstacle\x12<\n\rtraffic_light\x18\x02 \x01(\x0b\x32%.citibot.common.dispatch.TrafficLight\x12/\n\x0brain_status\x18\x03 \x01(\x0e\x32\x1a.citibot.common.RainStatus\"/\n\x0cPoint3dProto\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"\x91\x03\n\x17PerceptionObstacleProto\x12\n\n\x02id\x18\x01 \x01(\x05\x12.\n\x08position\x18\x02 \x01(\x0b\x32\x1c.citibot.common.Point3dProto\x12\r\n\x05theta\x18\x03 \x01(\x01\x12.\n\x08velocity\x18\x04 \x01(\x0b\x32\x1c.citibot.common.Point3dProto\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x06 \x01(\x01\x12\x0e\n\x06height\x18\x07 \x01(\x01\x12\x15\n\rtracking_time\x18\x08 \x01(\x01\x12.\n\x04type\x18\t \x01(\x0e\x32 .citibot.common.ObstacleTypePoto\x12.\n\x08sub_type\x18\n \x01(\x0e\x32\x1c.citibot.common.SubTypeProto\x12\x15\n\rgps_timestamp\x18\x0b \x01(\x01\x12\x12\n\nconfidence\x18\x0c \x01(\x01\x12\x17\n\x0ftype_confidence\x18\r \x01(\x01\x12\x11\n\tsensor_id\x18\x0e \x01(\t\"C\n\x13HaiKangObstacleInfo\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.citibot.common.HKObstacleType\"\x9e\x01\n\x0eRainSensorInfo\x12\x16\n\x0esunshine_value\x18\x01 \x01(\x05\x12\x12\n\nrain_value\x18\x02 \x01(\x05\x12\x18\n\x10\x62ig_lamp_request\x18\x03 \x01(\x08\x12\x1a\n\x12small_lamp_request\x18\x04 \x01(\x08\x12\x1a\n\x12\x61uto_wiper_control\x18\x05 \x01(\x05\x12\x0e\n\x06status\x18\x06 \x01(\x05\"\xea\x01\n\x16\x43\x61nThirdPartyInfoProto\x12;\n\nobsttacles\x18\x01 \x03(\x0b\x32\'.citibot.common.PerceptionObstacleProto\x12\x38\n\x10rain_sensor_info\x18\x02 \x01(\x0b\x32\x1e.citibot.common.RainSensorInfo\x12\x39\n\x0chk_obstacles\x18\x03 \x03(\x0b\x32#.citibot.common.HaiKangObstacleInfo\x12\x1e\n\x16under_car_obstacle_num\x18\x04 \x01(\x05*N\n\nRainStatus\x12\r\n\tNONE_RAIN\x10\x00\x12\x0e\n\nLIGHT_RAIN\x10\x01\x12\x11\n\rMODERATE_RAIN\x10\x02\x12\x0e\n\nHEAVY_RAIN\x10\x03*\xc7\x01\n\x10ObstacleTypePoto\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fUNKNOWN_MOVABLE\x10\x01\x12\x15\n\x11UNKNOWN_UNMOVABLE\x10\x02\x12\x0e\n\nPEDESTRIAN\x10\x03\x12\x0b\n\x07\x42ICYCLE\x10\x04\x12\x0b\n\x07VEHICLE\x10\x05\x12\x12\n\x0eWARING_THROUGH\x10\x06\x12\x0c\n\x08TOLL_BAR\x10\x07\x12\x11\n\rWARING_UNSAFE\x10\x08\x12\x0c\n\x08PLATFORM\x10\t\x12\r\n\tSUSPENDED\x10\n*\xd5\x02\n\x0cSubTypeProto\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\x16\n\x12ST_UNKNOWN_MOVABLE\x10\x01\x12\x18\n\x14ST_UNKNOWN_UNMOVABLE\x10\x02\x12\r\n\tST_PERSON\x10\x03\x12\x0c\n\x08ST_RIDER\x10\x04\x12\x0e\n\nST_CYCLIST\x10\x05\x12\x13\n\x0fST_MOTORCYCLIST\x10\x06\x12\n\n\x06ST_CAR\x10\x07\x12\n\n\x06ST_BUS\x10\x08\x12\x0c\n\x08ST_TRUCK\x10\t\x12\x0c\n\x08ST_TRAIN\x10\n\x12\x13\n\x0fST_TRAFFIC_CONE\x10\x0b\x12\x14\n\x10ST_TRAFFIC_FENCE\x10\x0c\x12\x14\n\x10ST_TRAFFIC_LIGHT\x10\r\x12\x13\n\x0fST_TRAFFIC_SIGN\x10\x0e\x12\x15\n\x11ST_MAN_HOLE_COVER\x10\x0f\x12\x0f\n\x0bST_TOLL_BAR\x10\x10\x12\x0f\n\x0bST_PLATFORM\x10\x11*\xb3\x01\n\x0eHKObstacleType\x12\x0c\n\x08NO_EVENT\x10\x00\x12\x06\n\x02IO\x10\x01\x12\x07\n\x03TMA\x10\x02\x12\x08\n\x04TMPA\x10\x03\x12\x12\n\x0eREGION_EXITING\x10\x04\x12\x11\n\rSHELTER_ALARM\x10\x05\x12\x12\n\x0e\x46IRE_DETECTION\x10\x06\x12\x13\n\x0fSMOKE_DETECTION\x10\x07\x12\x07\n\x03VMD\x10\x08\x12\x13\n\x0f\x46IELD_DETECTION\x10\t\x12\n\n\x06UNKNOW\x10\n')
  ,
  dependencies=[common_dot_message_dot_dispatch_dot_cloud__message__pb2.DESCRIPTOR,])

_RAINSTATUS = _descriptor.EnumDescriptor(
  name='RainStatus',
  full_name='citibot.common.RainStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_RAIN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIGHT_RAIN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODERATE_RAIN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEAVY_RAIN', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1241,
  serialized_end=1319,
)
_sym_db.RegisterEnumDescriptor(_RAINSTATUS)

RainStatus = enum_type_wrapper.EnumTypeWrapper(_RAINSTATUS)
_OBSTACLETYPEPOTO = _descriptor.EnumDescriptor(
  name='ObstacleTypePoto',
  full_name='citibot.common.ObstacleTypePoto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_MOVABLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_UNMOVABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEDESTRIAN', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BICYCLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VEHICLE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARING_THROUGH', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOLL_BAR', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARING_UNSAFE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUSPENDED', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1322,
  serialized_end=1521,
)
_sym_db.RegisterEnumDescriptor(_OBSTACLETYPEPOTO)

ObstacleTypePoto = enum_type_wrapper.EnumTypeWrapper(_OBSTACLETYPEPOTO)
_SUBTYPEPROTO = _descriptor.EnumDescriptor(
  name='SubTypeProto',
  full_name='citibot.common.SubTypeProto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ST_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_UNKNOWN_MOVABLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_UNKNOWN_UNMOVABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_PERSON', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_RIDER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_CYCLIST', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_MOTORCYCLIST', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_CAR', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_BUS', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRUCK', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRAIN', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRAFFIC_CONE', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRAFFIC_FENCE', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRAFFIC_LIGHT', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TRAFFIC_SIGN', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_MAN_HOLE_COVER', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_TOLL_BAR', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST_PLATFORM', index=17, number=17,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1524,
  serialized_end=1865,
)
_sym_db.RegisterEnumDescriptor(_SUBTYPEPROTO)

SubTypeProto = enum_type_wrapper.EnumTypeWrapper(_SUBTYPEPROTO)
_HKOBSTACLETYPE = _descriptor.EnumDescriptor(
  name='HKObstacleType',
  full_name='citibot.common.HKObstacleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_EVENT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TMA', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TMPA', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGION_EXITING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHELTER_ALARM', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRE_DETECTION', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SMOKE_DETECTION', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VMD', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIELD_DETECTION', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOW', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1868,
  serialized_end=2047,
)
_sym_db.RegisterEnumDescriptor(_HKOBSTACLETYPE)

HKObstacleType = enum_type_wrapper.EnumTypeWrapper(_HKOBSTACLETYPE)
NONE_RAIN = 0
LIGHT_RAIN = 1
MODERATE_RAIN = 2
HEAVY_RAIN = 3
UNKNOWN = 0
UNKNOWN_MOVABLE = 1
UNKNOWN_UNMOVABLE = 2
PEDESTRIAN = 3
BICYCLE = 4
VEHICLE = 5
WARING_THROUGH = 6
TOLL_BAR = 7
WARING_UNSAFE = 8
PLATFORM = 9
SUSPENDED = 10
ST_UNKNOWN = 0
ST_UNKNOWN_MOVABLE = 1
ST_UNKNOWN_UNMOVABLE = 2
ST_PERSON = 3
ST_RIDER = 4
ST_CYCLIST = 5
ST_MOTORCYCLIST = 6
ST_CAR = 7
ST_BUS = 8
ST_TRUCK = 9
ST_TRAIN = 10
ST_TRAFFIC_CONE = 11
ST_TRAFFIC_FENCE = 12
ST_TRAFFIC_LIGHT = 13
ST_TRAFFIC_SIGN = 14
ST_MAN_HOLE_COVER = 15
ST_TOLL_BAR = 16
ST_PLATFORM = 17
NO_EVENT = 0
IO = 1
TMA = 2
TMPA = 3
REGION_EXITING = 4
SHELTER_ALARM = 5
FIRE_DETECTION = 6
SMOKE_DETECTION = 7
VMD = 8
FIELD_DETECTION = 9
UNKNOW = 10



_THIRDPARTYSENSORPROTO = _descriptor.Descriptor(
  name='ThirdPartySensorProto',
  full_name='citibot.common.ThirdPartySensorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dispatch_obstacle', full_name='citibot.common.ThirdPartySensorProto.dispatch_obstacle', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_light', full_name='citibot.common.ThirdPartySensorProto.traffic_light', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rain_status', full_name='citibot.common.ThirdPartySensorProto.rain_status', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=319,
)


_POINT3DPROTO = _descriptor.Descriptor(
  name='Point3dProto',
  full_name='citibot.common.Point3dProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='citibot.common.Point3dProto.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='citibot.common.Point3dProto.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='citibot.common.Point3dProto.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=321,
  serialized_end=368,
)


_PERCEPTIONOBSTACLEPROTO = _descriptor.Descriptor(
  name='PerceptionObstacleProto',
  full_name='citibot.common.PerceptionObstacleProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='citibot.common.PerceptionObstacleProto.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='citibot.common.PerceptionObstacleProto.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='theta', full_name='citibot.common.PerceptionObstacleProto.theta', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='citibot.common.PerceptionObstacleProto.velocity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='citibot.common.PerceptionObstacleProto.length', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='citibot.common.PerceptionObstacleProto.width', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='citibot.common.PerceptionObstacleProto.height', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracking_time', full_name='citibot.common.PerceptionObstacleProto.tracking_time', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='citibot.common.PerceptionObstacleProto.type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_type', full_name='citibot.common.PerceptionObstacleProto.sub_type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gps_timestamp', full_name='citibot.common.PerceptionObstacleProto.gps_timestamp', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='citibot.common.PerceptionObstacleProto.confidence', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_confidence', full_name='citibot.common.PerceptionObstacleProto.type_confidence', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='citibot.common.PerceptionObstacleProto.sensor_id', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=371,
  serialized_end=772,
)


_HAIKANGOBSTACLEINFO = _descriptor.Descriptor(
  name='HaiKangObstacleInfo',
  full_name='citibot.common.HaiKangObstacleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='citibot.common.HaiKangObstacleInfo.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=774,
  serialized_end=841,
)


_RAINSENSORINFO = _descriptor.Descriptor(
  name='RainSensorInfo',
  full_name='citibot.common.RainSensorInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sunshine_value', full_name='citibot.common.RainSensorInfo.sunshine_value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rain_value', full_name='citibot.common.RainSensorInfo.rain_value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='big_lamp_request', full_name='citibot.common.RainSensorInfo.big_lamp_request', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='small_lamp_request', full_name='citibot.common.RainSensorInfo.small_lamp_request', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auto_wiper_control', full_name='citibot.common.RainSensorInfo.auto_wiper_control', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='citibot.common.RainSensorInfo.status', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=844,
  serialized_end=1002,
)


_CANTHIRDPARTYINFOPROTO = _descriptor.Descriptor(
  name='CanThirdPartyInfoProto',
  full_name='citibot.common.CanThirdPartyInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obsttacles', full_name='citibot.common.CanThirdPartyInfoProto.obsttacles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rain_sensor_info', full_name='citibot.common.CanThirdPartyInfoProto.rain_sensor_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hk_obstacles', full_name='citibot.common.CanThirdPartyInfoProto.hk_obstacles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='under_car_obstacle_num', full_name='citibot.common.CanThirdPartyInfoProto.under_car_obstacle_num', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1005,
  serialized_end=1239,
)

_THIRDPARTYSENSORPROTO.fields_by_name['dispatch_obstacle'].message_type = common_dot_message_dot_dispatch_dot_cloud__message__pb2._DISPATCHOBSTACLE
_THIRDPARTYSENSORPROTO.fields_by_name['traffic_light'].message_type = common_dot_message_dot_dispatch_dot_cloud__message__pb2._TRAFFICLIGHT
_THIRDPARTYSENSORPROTO.fields_by_name['rain_status'].enum_type = _RAINSTATUS
_PERCEPTIONOBSTACLEPROTO.fields_by_name['position'].message_type = _POINT3DPROTO
_PERCEPTIONOBSTACLEPROTO.fields_by_name['velocity'].message_type = _POINT3DPROTO
_PERCEPTIONOBSTACLEPROTO.fields_by_name['type'].enum_type = _OBSTACLETYPEPOTO
_PERCEPTIONOBSTACLEPROTO.fields_by_name['sub_type'].enum_type = _SUBTYPEPROTO
_HAIKANGOBSTACLEINFO.fields_by_name['type'].enum_type = _HKOBSTACLETYPE
_CANTHIRDPARTYINFOPROTO.fields_by_name['obsttacles'].message_type = _PERCEPTIONOBSTACLEPROTO
_CANTHIRDPARTYINFOPROTO.fields_by_name['rain_sensor_info'].message_type = _RAINSENSORINFO
_CANTHIRDPARTYINFOPROTO.fields_by_name['hk_obstacles'].message_type = _HAIKANGOBSTACLEINFO
DESCRIPTOR.message_types_by_name['ThirdPartySensorProto'] = _THIRDPARTYSENSORPROTO
DESCRIPTOR.message_types_by_name['Point3dProto'] = _POINT3DPROTO
DESCRIPTOR.message_types_by_name['PerceptionObstacleProto'] = _PERCEPTIONOBSTACLEPROTO
DESCRIPTOR.message_types_by_name['HaiKangObstacleInfo'] = _HAIKANGOBSTACLEINFO
DESCRIPTOR.message_types_by_name['RainSensorInfo'] = _RAINSENSORINFO
DESCRIPTOR.message_types_by_name['CanThirdPartyInfoProto'] = _CANTHIRDPARTYINFOPROTO
DESCRIPTOR.enum_types_by_name['RainStatus'] = _RAINSTATUS
DESCRIPTOR.enum_types_by_name['ObstacleTypePoto'] = _OBSTACLETYPEPOTO
DESCRIPTOR.enum_types_by_name['SubTypeProto'] = _SUBTYPEPROTO
DESCRIPTOR.enum_types_by_name['HKObstacleType'] = _HKOBSTACLETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ThirdPartySensorProto = _reflection.GeneratedProtocolMessageType('ThirdPartySensorProto', (_message.Message,), dict(
  DESCRIPTOR = _THIRDPARTYSENSORPROTO,
  __module__ = 'common.message.thirdparty.thirdparty_sensor_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.ThirdPartySensorProto)
  ))
_sym_db.RegisterMessage(ThirdPartySensorProto)

Point3dProto = _reflection.GeneratedProtocolMessageType('Point3dProto', (_message.Message,), dict(
  DESCRIPTOR = _POINT3DPROTO,
  __module__ = 'common.message.thirdparty.thirdparty_sensor_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.Point3dProto)
  ))
_sym_db.RegisterMessage(Point3dProto)

PerceptionObstacleProto = _reflection.GeneratedProtocolMessageType('PerceptionObstacleProto', (_message.Message,), dict(
  DESCRIPTOR = _PERCEPTIONOBSTACLEPROTO,
  __module__ = 'common.message.thirdparty.thirdparty_sensor_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.PerceptionObstacleProto)
  ))
_sym_db.RegisterMessage(PerceptionObstacleProto)

HaiKangObstacleInfo = _reflection.GeneratedProtocolMessageType('HaiKangObstacleInfo', (_message.Message,), dict(
  DESCRIPTOR = _HAIKANGOBSTACLEINFO,
  __module__ = 'common.message.thirdparty.thirdparty_sensor_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.HaiKangObstacleInfo)
  ))
_sym_db.RegisterMessage(HaiKangObstacleInfo)

RainSensorInfo = _reflection.GeneratedProtocolMessageType('RainSensorInfo', (_message.Message,), dict(
  DESCRIPTOR = _RAINSENSORINFO,
  __module__ = 'common.message.thirdparty.thirdparty_sensor_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.RainSensorInfo)
  ))
_sym_db.RegisterMessage(RainSensorInfo)

CanThirdPartyInfoProto = _reflection.GeneratedProtocolMessageType('CanThirdPartyInfoProto', (_message.Message,), dict(
  DESCRIPTOR = _CANTHIRDPARTYINFOPROTO,
  __module__ = 'common.message.thirdparty.thirdparty_sensor_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.CanThirdPartyInfoProto)
  ))
_sym_db.RegisterMessage(CanThirdPartyInfoProto)


# @@protoc_insertion_point(module_scope)