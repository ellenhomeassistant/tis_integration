from __future__ import annotations
from TISControlProtocol import *
_H=alpha__("b2ZmbGluZV9kZXZpY2U=")
_G=alpha__("dXBkYXRlX3Jlc3BvbnNl")
_F=alpha__("Y29udHJvbF9yZXNwb25zZQ==")
_E=alpha__("Y2hhbm5lbF9udW1iZXI=")
_D=False
_C=alpha__("YWRkaXRpb25hbF9ieXRlcw==")
_B=alpha__("ZmVlZGJhY2tfdHlwZQ==")
_A=None
import logging
from math import ceil
from typing import Any
from TISControlProtocol.api import TISApi
from TISControlProtocol.BytesHelper import int_to_8_bit_binary
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISPacket,TISProtocolHandler
from homeassistant.components.light import ATTR_BRIGHTNESS,ATTR_RGB_COLOR,ATTR_RGBW_COLOR,ColorMode,LightEntity,LightEntityFeature
from homeassistant.const import STATE_OFF,STATE_ON,STATE_UNKNOWN
from homeassistant.core import Event,HomeAssistant,callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from.import TISConfigEntry
handler=TISProtocolHandler()
async def async_setup_entry(hass,entry,async_add_devices):
    F=alpha__("Z2F0ZXdheQ==");E=alpha__("aXNfcHJvdGVjdGVk");D=alpha__("ZGV2aWNlX2lk");C=async_add_devices;B=alpha__("Y2hhbm5lbHM=");A=entry.runtime_data.api;G=await A.get_entities(platform=alpha__("ZGltbWVy"))
    if G:J=[(C,next(iter(A[B][0].values())),A[D],A[E],A[F])for A in G for(C,A)in A.items()];K=[TISLight(tis_api=A,light_name=B,device_id=D,channel_number=C,gateway=E)for(B,C,D,F,E)in J];C(K)
    H=await A.get_entities(platform=alpha__("cmdi"))
    if H:L=[(C,next(iter(A[B][0].values())),next(iter(A[B][1].values())),next(iter(A[B][2].values())),A[D],A[E],A[F])for A in H for(C,A)in A.items()];M=[TISRGBLight(tis_api=A,light_name=B,r_channel=C,g_channel=D,b_channel=E,device_id=F,gateway=G)for(B,C,D,E,F,H,G)in L];C(M)
    I=await A.get_entities(platform=alpha__("cmdidw=="))
    if I:N=[(C,next(iter(A[B][0].values())),next(iter(A[B][1].values())),next(iter(A[B][2].values())),next(iter(A[B][3].values())),A[D],A[E],A[F])for A in I for(C,A)in A.items()];O=[TISRGBWLight(tis_api=A,light_name=B,r_channel=C,g_channel=D,b_channel=E,w_channel=F,device_id=G,gateway=H)for(B,C,D,E,F,G,I,H)in N];C(O)
class TISLight(LightEntity):
    def __init__(A,tis_api,gateway,light_name,channel_number,device_id):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.channel_number=int(channel_number);A._attr_name=light_name;A._attr_state=_D;A._attr_brightness=_A;A.listener=_A;A.broadcast_channel=255;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=A.name, __var1=A.channel_number);A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={ColorMode.BRIGHTNESS};A._attr_color_mode=ColorMode.BRIGHTNESS;A._attr_supported_features=LightEntityFeature.TRANSITION;A.generate_light_packet=handler.generate_light_control_packet;A.update_packet=handler.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            B=event
            if B.event_type==str(A.device_id):
                if B.data[_B]==_F:
                    logging.info(beta__("Y2hhbm5lbCBudW1iZXIgZm9yIGxpZ2h0OiB7X192YXIwfQ==", __var0=A.channel_number));C=B.data[_C][2];D=B.data[_E]
                    if int(D)==A.channel_number:A._attr_state=int(C)!=0;A._attr_brightness=int(C/100*255)
                    A.async_write_ha_state()
                elif A.channel_number!=A.broadcast_channel:
                    if B.data[_B]==alpha__("YmluYXJ5X2ZlZWRiYWNr"):
                        E=ceil(B.data[_C][0]/8);F=alpha__("").join(int_to_8_bit_binary(B.data[_C][A])for A in range(1,E+1))
                        if F[A.channel_number-1]==alpha__("MA=="):A._attr_state=_D
                        A.async_write_ha_state()
                    elif B.data[_B]==_G:G=B.data[_C];A._attr_brightness=int(G[A.channel_number]/100*255);A._attr_state=STATE_ON if A._attr_brightness>0 else STATE_OFF
                elif B.data[_B]==_H:A._attr_state=STATE_UNKNOWN
        A.listener=A.hass.bus.async_listen(str(A.device_id),B);C=await A.api.protocol.sender.send_packet(A.update_packet)
    @property
    def brightness(self):return self._attr_brightness
    @property
    def color_mode(self):return self._attr_color_mode
    @property
    def supported_color_modes(self):return self._attr_supported_color_modes
    @property
    def supported_features(self):return self._attr_supported_features
    @property
    def is_on(self):return self._attr_brightness>0 if self._attr_brightness is not _A else _A
    @property
    def name(self):return self._attr_name
    async def async_turn_on(A,**B):
        try:C=B[ATTR_BRIGHTNESS]
        except KeyError:C=255
        D=A.generate_light_packet(A,int(C/255*100));E=await A.api.protocol.sender.send_packet_with_ack(D)
        if E:A._attr_state=True;A._attr_brightness=B.get(ATTR_BRIGHTNESS,255)
        else:A._attr_state=_A;A._attr_brightness=_A
        A.async_write_ha_state()
    async def async_turn_off(A,**D):
        B=A.generate_light_packet(A,0);C=await A.api.protocol.sender.send_packet_with_ack(B)
        if C:A._attr_brightness=0;A._attr_state=_D
        else:A._attr_state=_A;A._attr_brightness=_A
        A.async_write_ha_state()
class TISRGBLight(LightEntity):
    def __init__(A,tis_api,gateway,device_id,r_channel,g_channel,b_channel,light_name):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.r_channel=int(r_channel);A.g_channel=int(g_channel);A.b_channel=int(b_channel);A.rgb_value_flags=[0,0,0];A._attr_name=light_name;A._attr_state=_A;A._attr_rgb_color=_A;A.listener=_A;A.broadcast_channel=255;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn1fe19fdmFyM30=", __var0=A.name, __var1=A.r_channel, __var2=A.g_channel, __var3=A.b_channel);A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={ColorMode.RGB};A._attr_color_mode=ColorMode.RGB;A.generate_rgb_packets=handler.generate_rgb_light_control_packet;A.update_packet=handler.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            C=event
            if C.event_type==str(A.device_id):
                if C.data[_B]==_F:
                    D=C.data[_C][2];B=C.data[_E]
                    if int(B)==A.r_channel:A._attr_rgb_color=int(D/100*255),A._attr_rgb_color[1],A._attr_rgb_color[2];A.rgb_value_flags[0]=1
                    elif int(B)==A.g_channel:A._attr_rgb_color=A._attr_rgb_color[0],int(D/100*255),A._attr_rgb_color[2];A.rgb_value_flags[1]=1
                    elif int(B)==A.b_channel:A._attr_rgb_color=A._attr_rgb_color[0],A._attr_rgb_color[1],int(D/100*255);A.rgb_value_flags[2]=1
                    if A.rgb_value_flags==[1,1,1]:A.rgb_value_flags=[0,0,0];A.async_write_ha_state()
                elif A.channel_number!=A.broadcast_channel:
                    if C.data[_B]==_G:
                        E=C.data[_C];B=C.data[_E]
                        if A._attr_rgb_color is _A:A._attr_rgb_color=[0,0,0]
                        if B==A.r_channel:A._attr_rgb_color[0]=int(E[B]/100*255)
                        elif B==A.g_channel:A._attr_rgb_color[1]=int(E[B]/100*255)
                        elif B==A.b_channel:A._attr_rgb_color[2]=int(E[B]/100*255)
                        A._attr_state=bool(A.r_channel or A.g_channel or A.b_channel)
                elif C.data[_B]==_H:A._attr_state=STATE_UNKNOWN
        A.listener=A.hass.bus.async_listen(str(A.device_id),B)
        for C in range(5):
            if A._attr_rgb_color is _A:D=await A.api.protocol.sender.send_packet(A.update_packet)
        if A._attr_rgb_color is _A:A._attr_state=STATE_UNKNOWN;A._attr_rgb_color=0,0,0
    @property
    def color_mode(self):return self._attr_color_mode
    @property
    def rgb_color(self):return self._attr_rgb_color
    @property
    def supported_color_modes(self):return self._attr_supported_color_modes
    @property
    def is_on(self):return self._attr_state
    @property
    def name(self):return self._attr_name
    async def async_turn_on(A,**D):
        logging.info(beta__("a3dhcmdzOiB7X192YXIwfQ==", __var0=D))
        try:
            C=D[ATTR_RGB_COLOR];C=tuple([int(A/255*100)for A in C]);E,F,G=A.generate_rgb_packets(A,C);logging.info(beta__("Y29sb3IgKHBlcmNlbnQpOiB7X192YXIwfQ==", __var0=C));B=await A.api.protocol.sender.send_packet_with_ack(E)
            if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.r_channel))
            B=await A.api.protocol.sender.send_packet_with_ack(F)
            if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.g_channel))
            B=await A.api.protocol.sender.send_packet_with_ack(G)
            if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.b_channel))
            A._attr_state=True;C=tuple([int(A/100*255)for A in C]);A._attr_rgb_color=C
        except KeyError as H:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0=", __var0=H))
        A.async_write_ha_state()
    async def async_turn_off(A,**F):C,D,E=A.generate_rgb_packets(A,(0,0,0));B=await A.api.protocol.sender.send_packet_with_ack(D);B=await A.api.protocol.sender.send_packet_with_ack(C);B=await A.api.protocol.sender.send_packet_with_ack(E);A._attr_state=_D;A._attr_rgb_color=0,0,0;A.async_write_ha_state()
class TISRGBWLight(LightEntity):
    def __init__(A,tis_api,gateway,device_id,r_channel,g_channel,b_channel,w_channel,light_name):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.r_channel=int(r_channel);A.g_channel=int(g_channel);A.b_channel=int(b_channel);A.w_channel=int(w_channel);A._attr_name=light_name;A._attr_state=_A;A._attr_brightness=_A;A._attr_rgbw_color=_A;A.rgbw_value_flags=[0,0,0,0];A.listener=_A;A.broadcast_channel=255;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn1fe19fdmFyM31fe19fdmFyNH0=", __var0=A.name, __var1=A.r_channel, __var2=A.g_channel, __var3=A.b_channel, __var4=A.w_channel);A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={ColorMode.RGBW};A._attr_color_mode=ColorMode.RGBW;A._attr_supported_features=LightEntityFeature.TRANSITION;A.generate_rgbw_packets=handler.generate_rgbw_light_control_packet;A.update_packet=handler.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            B=event
            if B.event_type==str(A.device_id):
                if B.data[_B]==_F:
                    C=B.data[_C][2];D=B.data[_E]
                    if int(D)==A.r_channel:A._attr_rgbw_color=int(C/100*255),A._attr_rgbw_color[1],A._attr_rgbw_color[2],A._attr_rgbw_color[3];A.rgbw_value_flags[0]=1
                    elif int(D)==A.g_channel:A._attr_rgbw_color=A._attr_rgbw_color[0],int(C/100*255),A._attr_rgbw_color[2],A._attr_rgbw_color[3];A.rgbw_value_flags[1]=1
                    elif int(D)==A.b_channel:A._attr_rgbw_color=A._attr_rgbw_color[0],A._attr_rgbw_color[1],int(C/100*255),A._attr_rgbw_color[3];A.rgbw_value_flags[2]=1
                    elif int(D)==A.w_channel:A._attr_rgbw_color=A._attr_rgbw_color[0],A._attr_rgbw_color[1],A._attr_rgbw_color[2],int(C/100*255);A.rgbw_value_flags[3]=1
                    if A.rgbw_value_flags==[1,1,1,1]:A.async_write_ha_state()
                elif A.channel_number!=A.broadcast_channel:
                    if B.data[_B]==_G:E=B.data[_C];F=E[A.r_channel]/100*255;G=E[A.g_channel]/100*255;H=E[A.b_channel]/100*255;I=E[A.w_channel]/100*255;A._attr_rgbw_color=F,G,H,I;A._attr_state=bool(F or G or H or I)
                elif B.data[_B]==_H:A._attr_state=STATE_UNKNOWN
        A.listener=A.hass.bus.async_listen(str(A.device_id),B)
        for C in range(5):
            if A._attr_rgbw_color is _A:D=await A.api.protocol.sender.send_packet(A.update_packet)
        if A._attr_rgbw_color is _A:A._attr_state=STATE_UNKNOWN;A._attr_rgbw_color=0,0,0,0
    @property
    def brightness(self):return self._attr_brightness
    @property
    def color_mode(self):return self._attr_color_mode
    @property
    def rgbw_color(self):return self._attr_rgbw_color
    @property
    def supported_color_modes(self):return self._attr_supported_color_modes
    @property
    def supported_features(self):return self._attr_supported_features
    @property
    def is_on(self):return self._attr_state
    @property
    def name(self):return self._attr_name
    async def async_turn_on(A,**D):
        logging.info(beta__("a3dhcmdzOiB7X192YXIwfQ==", __var0=D))
        try:
            C=D[ATTR_RGBW_COLOR];C=tuple([int(A/255*100)for A in C]);E,F,G,H=A.generate_rgbw_packets(A,C);logging.info(beta__("Y29sb3IgKHBlcmNlbnQpOiB7X192YXIwfQ==", __var0=C));B=await A.api.protocol.sender.send_packet_with_ack(E)
            if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.r_channel))
            B=await A.api.protocol.sender.send_packet_with_ack(F)
            if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.g_channel))
            B=await A.api.protocol.sender.send_packet_with_ack(G)
            if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.b_channel))
            B=await A.api.protocol.sender.send_packet_with_ack(H)
            if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.w_channel))
            A._attr_state=True;C=tuple([int(A/100*255)for A in C]);A._attr_rgbw_color=C
        except KeyError as I:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0=", __var0=I))
        A.async_write_ha_state()
    async def async_turn_off(A,**G):C,D,E,F=A.generate_rgbw_packets(A,(0,0,0,0));B=await A.api.protocol.sender.send_packet_with_ack(C);B=await A.api.protocol.sender.send_packet_with_ack(D);B=await A.api.protocol.sender.send_packet_with_ack(E);B=await A.api.protocol.sender.send_packet_with_ack(F);A._attr_state=_D;A._attr_rgbw_color=0,0,0,0;A.async_write_ha_state()