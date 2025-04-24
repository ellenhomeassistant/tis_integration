from __future__ import annotations
from TISControlProtocol import *
_G=alpha__("Y2hhbm5lbF9udW1iZXI=")
_F=alpha__("Y29udHJvbF9yZXNwb25zZQ==")
_E=alpha__("YWRkaXRpb25hbF9ieXRlcw==")
_D=alpha__("ZmVlZGJhY2tfdHlwZQ==")
_C=False
_B=True
_A=None
import logging
from math import ceil
from typing import Any
import json
from TISControlProtocol.api import TISApi
from TISControlProtocol.BytesHelper import int_to_8_bit_binary
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISPacket,TISProtocolHandler
from homeassistant.components.cover import ATTR_POSITION,CoverDeviceClass,CoverEntity,CoverEntityFeature
from homeassistant.const import STATE_CLOSING,STATE_OPENING,STATE_UNKNOWN,Platform
from homeassistant.core import Event,HomeAssistant,callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from.import TISConfigEntry
handler=TISProtocolHandler()
async def async_setup_entry(hass,entry,async_add_devices):
    I=alpha__("Z2F0ZXdheQ==");H=alpha__("ZGV2aWNlX2lk");E=async_add_devices;D=alpha__("Y2hhbm5lbHM=");A=entry.runtime_data.api;F=await A.get_entities(platform=alpha__("bW90b3I="));G=await A.get_entities(platform=alpha__("c2h1dHRlcg=="))
    if F:B=[(B,next(iter(A[D][0].values())),A[H],A[I],A[alpha__("c2V0dGluZ3M=")])for A in F for(B,A)in A.items()];C=[TISCoverWPos(tis_api=A,cover_name=B,channel_number=C,device_id=D,gateway=E,settings=json.loads(F))for(B,C,D,E,F)in B];E(C,update_before_add=_B)
    if G:B=[(B,next(iter(A[D][0].values())),next(iter(A[D][1].values())),A[H],A[I])for A in G for(B,A)in A.items()];C=[TISCoverNoPos(tis_api=A,cover_name=B,up_channel_number=C,down_channel_number=D,device_id=E,gateway=F)for(B,C,D,E,F)in B];E(C,update_before_add=_B)
class TISCoverWPos(CoverEntity):
    def __init__(A,tis_api,gateway,cover_name,channel_number,device_id,settings):A.exchange_command=settings[alpha__("ZXhjaGFuZ2VfY29tbWFuZA==")];A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.channel_number=int(channel_number);A._attr_name=cover_name;A._attr_is_closed=_A;A._attr_current_cover_position=_A;A._attr_device_class=CoverDeviceClass.SHUTTER;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=A._attr_name, __var1=A.channel_number);A.listener=_A;A.update_packet=handler.generate_control_update_packet(A);A.generate_cover_packet=handler.generate_light_control_packet
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            B=event
            if B.event_type==str(A.device_id):
                if B.data[_D]==_F:
                    logging.info(beta__("Y2hhbm5lbCBudW1iZXIgZm9yIGNvdmVyOiB7X192YXIwfQ==", __var0=A.channel_number));D=B.data[_E][2];E=B.data[_G]
                    if int(E)==A.channel_number:
                        C=D
                        if A.exchange_command==alpha__("MQ=="):C=100-C
                        A._attr_is_closed=C==0;A._attr_current_cover_position=C
                    A.async_write_ha_state()
                elif B.data[_D]==alpha__("YmluYXJ5X2ZlZWRiYWNr"):
                    F=ceil(B.data[_E][0]/8);G=alpha__("").join(int_to_8_bit_binary(B.data[_E][A])for A in range(1,F+1))
                    if G[A.channel_number-1]==alpha__("MA=="):A._attr_is_closed=_B
                    A.async_write_ha_state()
                elif B.data[_D]==alpha__("dXBkYXRlX3Jlc3BvbnNl"):
                    H=B.data[_E];C=H[A.channel_number]
                    if A.exchange_command==alpha__("MQ=="):C=100-C
                    A._attr_current_cover_position=C;A._attr_is_closed=A._attr_current_cover_position==0;A._attr_state=STATE_CLOSING if A._attr_is_closed else STATE_OPENING
                elif B.data[_D]==alpha__("b2ZmbGluZV9kZXZpY2U="):A._attr_state=STATE_UNKNOWN;A._attr_is_closed=_A;A._attr_current_cover_position=_A
            await A.async_update_ha_state(_B)
        A.listener=A.hass.bus.async_listen(str(A.device_id),B);C=await A.api.protocol.sender.send_packet(A.update_packet)
    def _convert_position(B,position):
        A=position
        if B.exchange_command==alpha__("MQ=="):return 100-A
        return A
    @property
    def name(self):return self._attr_name
    @property
    def is_closed(self):return self._attr_is_closed
    @property
    def supported_features(self):return CoverEntityFeature.SET_POSITION
    @property
    def current_cover_position(self):return self._attr_current_cover_position
    @property
    def unique_id(self):return self._attr_unique_id
    async def async_open_cover(A,**E):
        B=A._convert_position(100);C=A.generate_cover_packet(A,B);D=await A.api.protocol.sender.send_packet_with_ack(C)
        if D:A._attr_is_closed=A.exchange_command==alpha__("MQ==");A._attr_current_cover_position=B
        else:A._attr_is_closed=_A;A._attr_current_cover_position=_A
        A.async_write_ha_state()
    async def async_close_cover(A,**E):
        B=A._convert_position(0);C=A.generate_cover_packet(A,B);D=await A.api.protocol.sender.send_packet_with_ack(C)
        if D:A._attr_is_closed=A.exchange_command!=alpha__("MQ==");A._attr_current_cover_position=B
        else:A._attr_is_closed=_C;A._attr_current_cover_position=_A
        A.async_write_ha_state()
    async def async_set_cover_position(A,**D):
        B=D[ATTR_POSITION];C=A._convert_position(B);E=A.generate_cover_packet(A,C);F=await A.api.protocol.sender.send_packet_with_ack(E)
        if F:A._attr_is_closed=B==100 if A.exchange_command==alpha__("MQ==")else B==0;A._attr_current_cover_position=C
        else:A._attr_is_closed=_A;A._attr_current_cover_position=_A
        A.async_write_ha_state()
class TISCoverNoPos(CoverEntity):
    def __init__(A,tis_api,gateway,cover_name,up_channel_number,down_channel_number,device_id):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.up_channel_number=int(up_channel_number);A.down_channel_number=int(down_channel_number);A._attr_name=cover_name;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn0=", __var0=A._attr_name, __var1=A.up_channel_number, __var2=A.down_channel_number);A.channel_number=A.up_channel_number;A._attr_is_closed=_A;A._attr_device_class=CoverDeviceClass.WINDOW;A.last_state=STATE_OPENING;A.listener=_A
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            B=event
            if B.event_type==str(A.device_id):
                if B.data[_D]==_F:
                    C=B.data[_E][2];D=B.data[_G]
                    if int(D)==A.up_channel_number:
                        if C!=0:A._attr_is_closed=_C;A.last_state=STATE_OPENING;A._attr_state=STATE_OPENING;logging.info(beta__("dXAgY2hhbm5lbCB2YWx1ZToge19fdmFyMH0gJ29wZW5pbmcn", __var0=C))
                    elif int(D)==A.down_channel_number:
                        if C!=0:A._attr_is_closed=_B;A._attr_state=STATE_CLOSING;A.last_state=STATE_CLOSING;logging.info(beta__("ZG93biBjaGFubmVsIHZhbHVlOiB7X192YXIwfSAnY2xvc2luZyc=", __var0=C))
                    else:logging.info(beta__("Y2hhbm5lbCBudW1iZXI6IHtfX3ZhcjB9ICdzdG9wcGluZyc=", __var0=D));A._attr_state=A.last_state;A._attr_is_closed=_C if A.last_state==STATE_OPENING else _B
            await A.async_update_ha_state(_B);A.schedule_update_ha_state()
        A.listener=A.hass.bus.async_listen(str(A.device_id),B)
    @property
    def name(self):return self._attr_name
    @property
    def is_closed(self):
        if self._attr_is_closed==_B:return _B
        elif self._attr_is_closed==_C:return _C
        else:return
    @property
    def supported_features(self):return CoverEntityFeature.OPEN|CoverEntityFeature.STOP|CoverEntityFeature.CLOSE
    @property
    def unique_id(self):return self._attr_unique_id
    async def async_open_cover(A,**D):
        B,E=handler.generate_no_pos_cover_packet(A,alpha__("b3Blbg=="));C=await A.api.protocol.sender.send_packet_with_ack(B)
        if C:logging.info(alpha__("dXAgcGFja2V0IHNlbnQgJ29wZW5pbmcn"));A._attr_is_closed=_C;A._attr_state=STATE_OPENING;A.last_state=STATE_OPENING
        else:logging.info(alpha__("dXAgcGFja2V0IG5vdCBzZW50ICdOb25lJw=="));A._attr_is_closed=_A;A._attr_state=_A
        A.async_write_ha_state()
    async def async_close_cover(A,**D):
        E,B=handler.generate_no_pos_cover_packet(A,alpha__("Y2xvc2U="));C=await A.api.protocol.sender.send_packet_with_ack(B)
        if C:logging.info(alpha__("ZG93biBwYWNrZXQgc2VudCAnY2xvc2luZyc="));A._attr_is_closed=_B;A._attr_state=STATE_CLOSING;A.last_state=STATE_CLOSING
        else:logging.info(alpha__("ZG93biBwYWNrZXQgbm90IHNlbnQgJ05vbmUn"));A._attr_is_closed=_A;A._attr_state=_A
        A.async_write_ha_state()
    async def async_stop_cover(A,**E):
        C,D=handler.generate_no_pos_cover_packet(A,alpha__("c3RvcA=="))
        if A._attr_is_closed:
            B=await A.api.protocol.sender.send_packet_with_ack(D)
            if B:logging.info(alpha__("ZG93biBwYWNrZXQgc2VudCAnc3RvcHBpbmcn"));A._attr_state=A.last_state;A._attr_is_closed=_C if A.last_state==STATE_OPENING else _B
            else:logging.info(alpha__("ZG93biBwYWNrZXQgbm90IHNlbnQgJ3N0b3BwaW5nJw=="));A._attr_state=_A;A._attr_is_closed=_A
        elif not A._attr_is_closed:
            B=await A.api.protocol.sender.send_packet_with_ack(C)
            if B:logging.info(alpha__("dXAgcGFja2V0IHNlbnQgJ3N0b3BwaW5nJw=="));A._attr_state=A.last_state;A._attr_is_closed=_C if A.last_state==STATE_OPENING else _B
            else:logging.info(alpha__("dXAgcGFja2V0IG5vdCBzZW50ICdzdG9wcGluZyc="));A._attr_state=_A;A._attr_is_closed=_A
        A.async_write_ha_state()