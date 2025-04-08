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
