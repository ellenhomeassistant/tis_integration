from __future__ import annotations
from TISControlProtocol import *
_E=False
_D=alpha__("b2ZmbGluZV9kZXZpY2U=")
_C=alpha__("ZGV2aWNlX2lk")
_B=alpha__("Y2hhbm5lbF9udW1iZXI=")
_A=alpha__("ZmVlZGJhY2tfdHlwZQ==")
from collections.abc import Callable
from math import ceil
from typing import Any
from TISControlProtocol.BytesHelper import int_to_8_bit_binary
from TISControlProtocol.api import TISApi
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISPacket,TISProtocolHandler
from homeassistant.components.switch import SwitchEntity
from homeassistant.const import MATCH_ALL,STATE_OFF,STATE_ON,STATE_UNKNOWN,Platform
from homeassistant.core import Event,HomeAssistant,callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
import logging
from.import TISConfigEntry
async def async_setup_entry(hass,entry,async_add_devices):
    A=entry.runtime_data.api;B=await A.get_entities(platform=Platform.SWITCH)
    if B:
        C=[(C,next(iter(A[alpha__("Y2hhbm5lbHM=")][0].values())),A[_C],A[alpha__("aXNfcHJvdGVjdGVk")],A[alpha__("Z2F0ZXdheQ==")])for B in B for(C,A)in B.items()]
        try:D=[TISSwitch(A,B,C,D,E)for(B,C,D,F,E)in C];async_add_devices(D,update_before_add=True)
        except Exception as E:logging.error(beta__("ZXJyb3IgaGFwcGVuZWQgY3JlYXRpbmcgZW50aXRpZXMgZToge19fdmFyMH0=", __var0=E))
protocol_handler=TISProtocolHandler()
class TISSwitch(SwitchEntity):
    def __init__(A,tis_api,switch_name,channel_number,device_id,gateway):B=switch_name;A.api=tis_api;A._name=B;A._attr_unique_id=beta__("c3dpdGNoX3tfX3ZhcjB9", __var0=A.name);A._state=STATE_UNKNOWN;A._attr_is_on=None;A.name=B;A.device_id=device_id;A.gateway=gateway;A.channel_number=int(channel_number);A.listener=None;A.broadcast_channel=255;A.on_packet=protocol_handler.generate_control_on_packet(A);A.off_packet=protocol_handler.generate_control_off_packet(A);A.update_packet=protocol_handler.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            C=alpha__("YWRkaXRpb25hbF9ieXRlcw==");B=event
            if B.event_type==str(A.device_id):
                if B.data[_A]==alpha__("Y29udHJvbF9yZXNwb25zZQ=="):
                    D=B.data[C][2];E=B.data[_B]
                    if int(E)==A.channel_number:A._state=STATE_ON if int(D)==100 else STATE_OFF
                elif A.channel_number!=A.broadcast_channel:
                    if B.data[_A]==alpha__("YmluYXJ5X2ZlZWRiYWNr"):F=ceil(B.data[C][0]/8);G=alpha__("").join(int_to_8_bit_binary(B.data[C][A])for A in range(1,F+1));A._state=STATE_ON if G[A.channel_number-1]==alpha__("MQ==")else STATE_OFF
                    elif B.data[_A]==alpha__("dXBkYXRlX3Jlc3BvbnNl"):H=B.data[C];I=int(H[A.channel_number]);A._state=STATE_ON if I>0 else STATE_OFF
                elif B.data[_A]==_D:
                    if int(B.data[_B])==A.channel_number:A._state=STATE_UNKNOWN
            await A.async_update_ha_state(True)
        try:A.listener=A.hass.bus.async_listen(MATCH_ALL,B);D=await A.api.protocol.sender.send_packet(A.update_packet)
        except Exception as C:logging.error(beta__("ZXJyb3IgaW4gYXN5bmNfYWRkZWRfdG9faGFzcyBmdW4gZToge19fdmFyMH0=", __var0=C))
    async def async_will_remove_from_hass(A):A.listener=None
    async def async_turn_on(A,**E):
        try:
            B=await A.api.protocol.sender.send_packet_with_ack(A.on_packet)
            if B:A._state=STATE_ON
            elif B==_E:A._state=STATE_UNKNOWN;C={_C:A.device_id,_A:_D,_B:A.channel_number};A.hass.bus.async_fire(str(A.device_id),C)
        except Exception as D:logging.error(beta__("ZXJyb3IgaW4gYXN5bmNfdHVybl9vbiBlOiB7X192YXIwfQ==", __var0=D))
        A.schedule_update_ha_state()
    async def async_turn_off(A,**E):
        try:
            B=await A.api.protocol.sender.send_packet_with_ack(A.off_packet)
            if B:A._state=STATE_OFF
            elif B==_E:A._state=STATE_UNKNOWN;C={_C:A.device_id,_A:_D,_B:A.channel_number};A.hass.bus.async_fire(str(A.device_id),C)
        except Exception as D:logging.error(beta__("ZXJyb3IgaW4gYXN5bmNfdHVybl9vZmYgZToge19fdmFyMH0=", __var0=D))
        A.schedule_update_ha_state()
    @property
    def name(self):return self._name
    @name.setter
    def name(self,value):self._name=value
    @property
    def unique_id(self):return self._attr_unique_id
    @property
    def is_on(self):
        if self._state==STATE_ON:return True
        elif self._state==STATE_OFF:return _E
        else:return