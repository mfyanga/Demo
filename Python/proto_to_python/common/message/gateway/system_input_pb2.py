# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/message/gateway/system_input.proto

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


from common.message import header_pb2 as common_dot_message_dot_header__pb2
from common.message.function_manage import evaluation_pb2 as common_dot_message_dot_function__manage_dot_evaluation__pb2
from common.message.function_manage import manage_info_pb2 as common_dot_message_dot_function__manage_dot_manage__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/message/gateway/system_input.proto',
  package='citibot.common.message',
  syntax='proto2',
  serialized_pb=_b('\n)common/message/gateway/system_input.proto\x12\x16\x63itibot.common.message\x1a\x1b\x63ommon/message/header.proto\x1a/common/message/function_manage/evaluation.proto\x1a\x30\x63ommon/message/function_manage/manage_info.proto\"\x80\x01\n\nDrivingCmd\x12\x35\n\x06\x61\x63tion\x18\x01 \x02(\x0e\x32%.citibot.common.message.DrivingAction\x12;\n\x0c\x64riving_conf\x18\x02 \x01(\x0b\x32%.citibot.common.message.DrivingConfig\"\x81\x06\n\x0bSystemInput\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x1e.citibot.common.message.Header\x12\r\n\x05token\x18\x02 \x01(\x04\x12\x37\n\x04type\x18\x03 \x01(\x0e\x32).citibot.common.message.SystemMissionType\x12\x37\n\x0bmode_switch\x18\x04 \x01(\x0e\x32\".citibot.common.message.SystemMode\x12\x37\n\x0b\x64riving_cmd\x18\x05 \x01(\x0b\x32\".citibot.common.message.DrivingCmd\x12\x33\n\x08usr_conf\x18\x06 \x01(\x0b\x32!.citibot.common.message.UsrConfig\x12:\n\x0cpara_setting\x18\x07 \x01(\x0b\x32$.citibot.common.message.ParameterCmd\x12\x35\n\ndevice_cmd\x18\x08 \x01(\x0b\x32!.citibot.common.message.DeviceCmd\x12\x44\n\x12\x63loud_mission_type\x18\t \x01(\x0e\x32(.citibot.common.message.CloudMissionType\x12\x37\n\x0b\x64\x61ta_record\x18\x14 \x01(\x0b\x32\".citibot.common.message.DataRecord\x12\x36\n\nrelocation\x18\x15 \x01(\x0b\x32\".citibot.common.message.InitPosCmd\x12\x41\n\x0e\x65valuation_req\x18\x16 \x01(\x0b\x32).citibot.common.message.EvaluationRequest\x12\x42\n\x11parking_cali_type\x18\x17 \x01(\x0e\x32\'.citibot.common.message.ParkingCaliType\x12\x13\n\x0b\x64\x65scription\x18\x64 \x01(\t\x12\r\n\x04\x64\x61ta\x18\xc8\x01 \x01(\x0c*\xbb\x03\n\x11SystemMissionType\x12\x14\n\x10WORK_MODE_SWITCH\x10\x01\x12\x11\n\rDRIVING_ORDER\x10\x02\x12\x0f\n\x0bUSR_SETTING\x10\x03\x12\x10\n\x0cPARA_SETTING\x10\x04\x12\x11\n\rSYSTEM_UPDATE\x10\x05\x12\x12\n\x0eSYSTEM_RESTART\x10\x06\x12\x12\n\x0e\x44\x45VICE_CONTROL\x10\x07\x12\x17\n\x13START_WATER_FILLING\x10\x08\x12\x16\n\x12STOP_WATER_FILLING\x10\t\x12\x10\n\x0c\x41UTO_DUMPING\x10\n\x12\x10\n\x0cSTOP_DUMPING\x10\x0b\x12\x10\n\x0cSTART_RECORD\x10\x64\x12\x0f\n\x0bSTOP_RECORD\x10\x65\x12\x10\n\x0bROUTING_REQ\x10\x90\x03\x12\x0f\n\nSTART_NAVI\x10\x91\x03\x12\r\n\x08\x45ND_NAVI\x10\x92\x03\x12\x12\n\rCLOUD_MISSION\x10\xa4\x03\x12\x0f\n\nRELOCATION\x10\xd8\x04\x12\x11\n\x0cSET_INIT_POS\x10\xd9\x04\x12\x12\n\rLOCATION_INIT\x10\xda\x04\x12\x0f\n\nEVALUATION\x10\xdb\x04\x12\x18\n\x13PARKING_CALIBRATION\x10\xdc\x04*L\n\rDrivingAction\x12\x12\n\x0e\x45XIT_AUTOMATIC\x10\x00\x12\x13\n\x0f\x45NTER_AUTOMATIC\x10\x01\x12\x12\n\x0e\x45MERGENCY_STOP\x10\x02*\xa3\x01\n\x10\x43loudMissionType\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x12\n\x0eMISSION_CANCEL\x10\x01\x12\x14\n\x10MISSION_COMPLETE\x10\x02\x12\x15\n\x11\x42REAKPOINT_CANCEL\x10\x03\x12\x08\n\x04MOVE\x10\n\x12\t\n\x05\x43LEAN\x10\x0b\x12\n\n\x06\x43HARGE\x10\x0c\x12\x11\n\rWATER_FILLING\x10\r\x12\x08\n\x04\x44UMP\x10\x0e*H\n\x0fParkingCaliType\x12\x11\n\rCHARGING_CALI\x10\x00\x12\x10\n\x0cGARBAGE_CALI\x10\x01\x12\x10\n\x0cUNKNOWN_CALI\x10\x14')
  ,
  dependencies=[common_dot_message_dot_header__pb2.DESCRIPTOR,common_dot_message_dot_function__manage_dot_evaluation__pb2.DESCRIPTOR,common_dot_message_dot_function__manage_dot_manage__info__pb2.DESCRIPTOR,])

_SYSTEMMISSIONTYPE = _descriptor.EnumDescriptor(
  name='SystemMissionType',
  full_name='citibot.common.message.SystemMissionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WORK_MODE_SWITCH', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRIVING_ORDER', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USR_SETTING', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARA_SETTING', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM_UPDATE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM_RESTART', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_CONTROL', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_WATER_FILLING', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_WATER_FILLING', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTO_DUMPING', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_DUMPING', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_RECORD', index=11, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_RECORD', index=12, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_REQ', index=13, number=400,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_NAVI', index=14, number=401,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_NAVI', index=15, number=402,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOUD_MISSION', index=16, number=420,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELOCATION', index=17, number=600,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_INIT_POS', index=18, number=601,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_INIT', index=19, number=602,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVALUATION', index=20, number=603,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARKING_CALIBRATION', index=21, number=604,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1101,
  serialized_end=1544,
)
_sym_db.RegisterEnumDescriptor(_SYSTEMMISSIONTYPE)

SystemMissionType = enum_type_wrapper.EnumTypeWrapper(_SYSTEMMISSIONTYPE)
_DRIVINGACTION = _descriptor.EnumDescriptor(
  name='DrivingAction',
  full_name='citibot.common.message.DrivingAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXIT_AUTOMATIC', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTER_AUTOMATIC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMERGENCY_STOP', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1546,
  serialized_end=1622,
)
_sym_db.RegisterEnumDescriptor(_DRIVINGACTION)

DrivingAction = enum_type_wrapper.EnumTypeWrapper(_DRIVINGACTION)
_CLOUDMISSIONTYPE = _descriptor.EnumDescriptor(
  name='CloudMissionType',
  full_name='citibot.common.message.CloudMissionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_CANCEL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSION_COMPLETE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BREAKPOINT_CANCEL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE', index=4, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEAN', index=5, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARGE', index=6, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WATER_FILLING', index=7, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUMP', index=8, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1625,
  serialized_end=1788,
)
_sym_db.RegisterEnumDescriptor(_CLOUDMISSIONTYPE)

CloudMissionType = enum_type_wrapper.EnumTypeWrapper(_CLOUDMISSIONTYPE)
_PARKINGCALITYPE = _descriptor.EnumDescriptor(
  name='ParkingCaliType',
  full_name='citibot.common.message.ParkingCaliType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHARGING_CALI', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GARBAGE_CALI', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_CALI', index=2, number=20,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1790,
  serialized_end=1862,
)
_sym_db.RegisterEnumDescriptor(_PARKINGCALITYPE)

ParkingCaliType = enum_type_wrapper.EnumTypeWrapper(_PARKINGCALITYPE)
WORK_MODE_SWITCH = 1
DRIVING_ORDER = 2
USR_SETTING = 3
PARA_SETTING = 4
SYSTEM_UPDATE = 5
SYSTEM_RESTART = 6
DEVICE_CONTROL = 7
START_WATER_FILLING = 8
STOP_WATER_FILLING = 9
AUTO_DUMPING = 10
STOP_DUMPING = 11
START_RECORD = 100
STOP_RECORD = 101
ROUTING_REQ = 400
START_NAVI = 401
END_NAVI = 402
CLOUD_MISSION = 420
RELOCATION = 600
SET_INIT_POS = 601
LOCATION_INIT = 602
EVALUATION = 603
PARKING_CALIBRATION = 604
EXIT_AUTOMATIC = 0
ENTER_AUTOMATIC = 1
EMERGENCY_STOP = 2
TYPE_UNKNOWN = 0
MISSION_CANCEL = 1
MISSION_COMPLETE = 2
BREAKPOINT_CANCEL = 3
MOVE = 10
CLEAN = 11
CHARGE = 12
WATER_FILLING = 13
DUMP = 14
CHARGING_CALI = 0
GARBAGE_CALI = 1
UNKNOWN_CALI = 20



_DRIVINGCMD = _descriptor.Descriptor(
  name='DrivingCmd',
  full_name='citibot.common.message.DrivingCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='citibot.common.message.DrivingCmd.action', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='driving_conf', full_name='citibot.common.message.DrivingCmd.driving_conf', index=1,
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
  serialized_start=198,
  serialized_end=326,
)


_SYSTEMINPUT = _descriptor.Descriptor(
  name='SystemInput',
  full_name='citibot.common.message.SystemInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='citibot.common.message.SystemInput.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='citibot.common.message.SystemInput.token', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='citibot.common.message.SystemInput.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode_switch', full_name='citibot.common.message.SystemInput.mode_switch', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='driving_cmd', full_name='citibot.common.message.SystemInput.driving_cmd', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usr_conf', full_name='citibot.common.message.SystemInput.usr_conf', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='para_setting', full_name='citibot.common.message.SystemInput.para_setting', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_cmd', full_name='citibot.common.message.SystemInput.device_cmd', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cloud_mission_type', full_name='citibot.common.message.SystemInput.cloud_mission_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_record', full_name='citibot.common.message.SystemInput.data_record', index=9,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relocation', full_name='citibot.common.message.SystemInput.relocation', index=10,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evaluation_req', full_name='citibot.common.message.SystemInput.evaluation_req', index=11,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parking_cali_type', full_name='citibot.common.message.SystemInput.parking_cali_type', index=12,
      number=23, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='citibot.common.message.SystemInput.description', index=13,
      number=100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='citibot.common.message.SystemInput.data', index=14,
      number=200, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=329,
  serialized_end=1098,
)

_DRIVINGCMD.fields_by_name['action'].enum_type = _DRIVINGACTION
_DRIVINGCMD.fields_by_name['driving_conf'].message_type = common_dot_message_dot_function__manage_dot_manage__info__pb2._DRIVINGCONFIG
_SYSTEMINPUT.fields_by_name['header'].message_type = common_dot_message_dot_header__pb2._HEADER
_SYSTEMINPUT.fields_by_name['type'].enum_type = _SYSTEMMISSIONTYPE
_SYSTEMINPUT.fields_by_name['mode_switch'].enum_type = common_dot_message_dot_function__manage_dot_manage__info__pb2._SYSTEMMODE
_SYSTEMINPUT.fields_by_name['driving_cmd'].message_type = _DRIVINGCMD
_SYSTEMINPUT.fields_by_name['usr_conf'].message_type = common_dot_message_dot_function__manage_dot_manage__info__pb2._USRCONFIG
_SYSTEMINPUT.fields_by_name['para_setting'].message_type = common_dot_message_dot_function__manage_dot_manage__info__pb2._PARAMETERCMD
_SYSTEMINPUT.fields_by_name['device_cmd'].message_type = common_dot_message_dot_function__manage_dot_manage__info__pb2._DEVICECMD
_SYSTEMINPUT.fields_by_name['cloud_mission_type'].enum_type = _CLOUDMISSIONTYPE
_SYSTEMINPUT.fields_by_name['data_record'].message_type = common_dot_message_dot_function__manage_dot_manage__info__pb2._DATARECORD
_SYSTEMINPUT.fields_by_name['relocation'].message_type = common_dot_message_dot_function__manage_dot_manage__info__pb2._INITPOSCMD
_SYSTEMINPUT.fields_by_name['evaluation_req'].message_type = common_dot_message_dot_function__manage_dot_evaluation__pb2._EVALUATIONREQUEST
_SYSTEMINPUT.fields_by_name['parking_cali_type'].enum_type = _PARKINGCALITYPE
DESCRIPTOR.message_types_by_name['DrivingCmd'] = _DRIVINGCMD
DESCRIPTOR.message_types_by_name['SystemInput'] = _SYSTEMINPUT
DESCRIPTOR.enum_types_by_name['SystemMissionType'] = _SYSTEMMISSIONTYPE
DESCRIPTOR.enum_types_by_name['DrivingAction'] = _DRIVINGACTION
DESCRIPTOR.enum_types_by_name['CloudMissionType'] = _CLOUDMISSIONTYPE
DESCRIPTOR.enum_types_by_name['ParkingCaliType'] = _PARKINGCALITYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DrivingCmd = _reflection.GeneratedProtocolMessageType('DrivingCmd', (_message.Message,), dict(
  DESCRIPTOR = _DRIVINGCMD,
  __module__ = 'common.message.gateway.system_input_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.DrivingCmd)
  ))
_sym_db.RegisterMessage(DrivingCmd)

SystemInput = _reflection.GeneratedProtocolMessageType('SystemInput', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMINPUT,
  __module__ = 'common.message.gateway.system_input_pb2'
  # @@protoc_insertion_point(class_scope:citibot.common.message.SystemInput)
  ))
_sym_db.RegisterMessage(SystemInput)


# @@protoc_insertion_point(module_scope)
