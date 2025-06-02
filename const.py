from __future__ import annotations
from TISControlProtocol import *


from homeassistant.components.climate import (
    ATTR_TEMPERATURE,
    FAN_AUTO,
    FAN_HIGH,
    FAN_LOW,
    FAN_MEDIUM,
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
    UnitOfTemperature,
)

DOMAIN = alpha__("dGlzX2NvbnRyb2w=")

DEVICES_DICT = {
    (0x1B, 0xBA): alpha__("UkNVLThPVVQtOElO"),
    (0x0B, 0xE9): alpha__("U0VDLVNN"),
    (0x80, 0x58): alpha__("SVAtQ09NLVBPUlQ="),
    (0x01, 0xA8): alpha__("UkxZLTRDSC0xMA=="),
    (0x23, 0x32): alpha__("TFVOQS1URlQtNDM="),
    (0x80, 0x25): alpha__("VkVOLTNTLTNSLUhDLUJVUw=="),
    (0x80, 0x38): alpha__("QlVTLUVTLUlS"),
    (0x02, 0x5A): alpha__("RElNLTJDSC02QQ=="),
    (0x02, 0x58): alpha__("RElNLTZDSC0yQQ=="),
    (0x00, 0x76): alpha__("NERJLUlO"),
    (0x80, 0x2B): alpha__("MjRSMjBa"),
    (0x20, 0x58): alpha__("RElNLTZDSC0yQQ=="),
    (0x1B, 0xB6): alpha__("VElTLVRFLURJTS00Q0gtMUE="),
    (0x80, 0x2D): alpha__("VElTLVJDVS0yME9VVC0yMElO"),
    (0x01, 0xB8): alpha__("VElTLVZMQy0xMkNILTEwQQ=="),
    (0x01, 0xAA): alpha__("VElTLVZMQy02Q0gtM0E="),
}

TEMPERATURE_RANGES = {
    HVACMode.COOL: {
        alpha__("bWlu"): (15.0, 59.0),
        alpha__("bWF4"): (26.0, 79.0),
        alpha__("dGFyZ2V0"): (20.0, 68.0),
        alpha__("cGFja2V0X21vZGVfaW5kZXg="): 0,
    },
    HVACMode.HEAT: {
        alpha__("bWlu"): (20.0, 68.0),
        alpha__("bWF4"): (35.0, 95.0),
        alpha__("dGFyZ2V0"): (28.0, 82.0),
        alpha__("cGFja2V0X21vZGVfaW5kZXg="): 1,
    },
    HVACMode.FAN_ONLY: {
        alpha__("bWlu"): (15.0, 59.0),
        alpha__("bWF4"): (26.0, 79.0),
        alpha__("dGFyZ2V0"): (20.0, 68.0),
        alpha__("cGFja2V0X21vZGVfaW5kZXg="): 2,
    },
    HVACMode.AUTO: {
        alpha__("bWlu"): (15.0, 59.0),
        alpha__("bWF4"): (35.0, 95.0),
        alpha__("dGFyZ2V0"): (25.0, 77.0),
        alpha__("cGFja2V0X21vZGVfaW5kZXg="): 3,
    },
    # off
    HVACMode.OFF: {
        alpha__("bWlu"): (15.0, 59.0),
        alpha__("bWF4"): (26.0, 79.0),
        alpha__("dGFyZ2V0"): (20.0, 68.0),
        alpha__("cGFja2V0X21vZGVfaW5kZXg="): 0,
    },
}
FAN_MODES = {
    FAN_AUTO: 0,
    FAN_HIGH: 1,
    FAN_MEDIUM: 2,
    FAN_LOW: 3,
}

ENERGY_SENSOR_TYPES = {
    alpha__("djE="): alpha__("Vm9sdGFnZSBQaGFzZSAx"),
    alpha__("djI="): alpha__("Vm9sdGFnZSBQaGFzZSAy"),
    alpha__("djM="): alpha__("Vm9sdGFnZSBQaGFzZSAz"),
    alpha__("Y3VycmVudF9wMQ=="): alpha__("Q3VycmVudCBQaGFzZSAx"),
    alpha__("Y3VycmVudF9wMg=="): alpha__("Q3VycmVudCBQaGFzZSAy"),
    alpha__("Y3VycmVudF9wMw=="): alpha__("Q3VycmVudCBQaGFzZSAz"),
    alpha__("YWN0aXZlX3Ax"): alpha__("QWN0aXZlIFBvd2VyIFBoYXNlIDE="),
    alpha__("YWN0aXZlX3Ay"): alpha__("QWN0aXZlIFBvd2VyIFBoYXNlIDI="),
    alpha__("YWN0aXZlX3Az"): alpha__("QWN0aXZlIFBvd2VyIFBoYXNlIDM="),
    alpha__("YXBwYXJlbnQx"): alpha__("QXBwYXJlbnQgUG93ZXIgUGhhc2UgMQ=="),
    alpha__("YXBwYXJlbnQy"): alpha__("QXBwYXJlbnQgUG93ZXIgUGhhc2UgMg=="),
    alpha__("YXBwYXJlbnQz"): alpha__("QXBwYXJlbnQgUG93ZXIgUGhhc2UgMw=="),
    alpha__("cmVhY3RpdmUx"): alpha__("UmVhY3RpdmUgUG93ZXIgUGhhc2UgMQ=="),
    alpha__("cmVhY3RpdmUy"): alpha__("UmVhY3RpdmUgUG93ZXIgUGhhc2UgMg=="),
    alpha__("cmVhY3RpdmUz"): alpha__("UmVhY3RpdmUgUG93ZXIgUGhhc2UgMw=="),
    alpha__("cGYx"): alpha__("UG93ZXIgRmFjdG9yIFBoYXNlIDE="),
    alpha__("cGYy"): alpha__("UG93ZXIgRmFjdG9yIFBoYXNlIDI="),
    alpha__("cGYz"): alpha__("UG93ZXIgRmFjdG9yIFBoYXNlIDM="),
    alpha__("cGEx"): alpha__("UGhhc2UgQW5nbGUgUGhhc2UgMQ=="),
    alpha__("cGEy"): alpha__("UGhhc2UgQW5nbGUgUGhhc2UgMg=="),
    alpha__("cGEz"): alpha__("UGhhc2UgQW5nbGUgUGhhc2UgMw=="),
    alpha__("YXZnX2xpdmVfdG9fbmV1dHJhbA=="): alpha__("QXZlcmFnZSBMaXZlIHRvIE5ldXRyYWwgVm9sdGFnZQ=="),
    alpha__("YXZnX2N1cnJlbnQ="): alpha__("QXZlcmFnZSBDdXJyZW50"),
    alpha__("c3VtX2N1cnJlbnQ="): alpha__("U3VtIEN1cnJlbnQ="),
    alpha__("dG90YWxfcG93ZXI="): alpha__("VG90YWwgUG93ZXI="),
    alpha__("dG90YWxfdm9sdF9hbXBz"): alpha__("VG90YWwgVm9sdCBBbXBz"),
    alpha__("dG90YWxfdmFy"): alpha__("VG90YWwgVkFS"),
    alpha__("dG90YWxfcHR4WXBVWE1LRVJ3cGt0Wm8wVG90YWwgUG93ZXIgRmFjdG9y"),
    alpha__("dG90YWxfcGE="): alpha__("VG90YWwgUGhhc2UgQW5nbGU="),
    alpha__("ZnJx"): alpha__("RnJlcXVlbmN5"),
}
