from __future__ import annotations
from TISControlProtocol import *
_H=alpha__("Y2hhbm5lbF9udW1iZXI=")
_G=alpha__("b2ZmbGluZV9kZXZpY2U=")
_F=alpha__("dXBkYXRlX3Jlc3BvbnNl")
_E=True
_D=alpha__("YWRkaXRpb25hbF9ieXRlcw==")
_C=False
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
    def __init__(A,tis_api,gateway,light_name,channel_number,device_id):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.channel_number=int(channel_number);A._attr_name=light_name;A._attr_state=_C;A._attr_brightness=_A;A.listener=_A;A.broadcast_channel=255;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=A.name, __var1=A.channel_number);A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={ColorMode.BRIGHTNESS};A._attr_color_mode=ColorMode.BRIGHTNESS;A._attr_supported_features=LightEntityFeature.TRANSITION;A.generate_light_packet=handler.generate_light_control_packet;A.update_packet=handler.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            B=event
            if B.event_type==str(A.device_id):
                if B.data[_B]==alpha__("Y29udHJvbF9yZXNwb25zZQ=="):
                    logging.info(beta__("Y2hhbm5lbCBudW1iZXIgZm9yIGxpZ2h0OiB7X192YXIwfQ==", __var0=A.channel_number));C=B.data[_D][2];D=B.data[_H]
                    if int(D)==A.channel_number:A._attr_state=int(C)!=0;A._attr_brightness=int(C/100*255)
                    A.async_write_ha_state()
                elif A.channel_number!=A.broadcast_channel:
                    if B.data[_B]==alpha__("YmluYXJ5X2ZlZWRiYWNr"):
                        E=ceil(B.data[_D][0]/8);F=alpha__("").join(int_to_8_bit_binary(B.data[_D][A])for A in range(1,E+1))
                        if F[A.channel_number-1]==alpha__("MA=="):A._attr_state=_C
                        A.async_write_ha_state()
                    elif B.data[_B]==_F:G=B.data[_D];A._attr_brightness=int(G[A.channel_number]/100*255);A._attr_state=STATE_ON if A._attr_brightness>0 else STATE_OFF
                elif B.data[_B]==_G:A._attr_state=STATE_UNKNOWN
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
        if E:A._attr_state=_E;A._attr_brightness=B.get(ATTR_BRIGHTNESS,255)
        else:A._attr_state=_A;A._attr_brightness=_A
        A.async_write_ha_state()
    async def async_turn_off(A,**D):
        B=A.generate_light_packet(A,0);C=await A.api.protocol.sender.send_packet_with_ack(B)
        if C:A._attr_brightness=0;A._attr_state=_C
        else:A._attr_state=_A;A._attr_brightness=_A
        A.async_write_ha_state()
class TISRGBLight(LightEntity):
    def __init__(A,tis_api,gateway,device_id,r_channel,g_channel,b_channel,light_name):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.r_channel=int(r_channel);A.g_channel=int(g_channel);A.b_channel=int(b_channel);A.rgb_value_flags=[0,0,0];A._attr_name=light_name;A._attr_state=_A;A._attr_rgb_color=_A;A._attr_brightness=_A;A.listener=_A;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn1fe19fdmFyM30=", __var0=A.name, __var1=A.r_channel, __var2=A.g_channel, __var3=A.b_channel);A.default_color=0,0,0;A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={ColorMode.RGB};A._attr_color_mode=ColorMode.RGB;A.generate_rgb_packets=handler.generate_rgb_light_control_packet;A.update_packet=handler.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            C=event
            if C.event_type==str(A.device_id):
                if C.data[_B]==_F:
                    D=C.data[_D];B=C.data[_H]
                    if A._attr_rgb_color is _A:A._attr_rgb_color=[0,0,0]
                    if B==A.r_channel:A._attr_rgb_color[0]=int(D[B]/100*255)
                    elif B==A.g_channel:A._attr_rgb_color[1]=int(D[B]/100*255)
                    elif B==A.b_channel:A._attr_rgb_color[2]=int(D[B]/100*255)
                    A._attr_state=bool(A.r_channel or A.g_channel or A.b_channel)
                elif C.data[_B]==_G:A._attr_state=STATE_UNKNOWN
        A.listener=A.hass.bus.async_listen(str(A.device_id),B)
        for C in range(5):
            if A._attr_rgb_color is _A:D=await A.api.protocol.sender.send_packet(A.update_packet)
        if A._attr_rgb_color is _A:A._attr_state=STATE_UNKNOWN;A._attr_rgb_color=0,0,0
    @property
    def color_mode(self):return self._attr_color_mode
    @property
    def brightness(self):return self._attr_brightness
    @property
    def rgb_color(self):return self._attr_rgb_color
    @property
    def supported_color_modes(self):return self._attr_supported_color_modes
    @property
    def is_on(self):return self._attr_state
    @property
    def name(self):return self._attr_name
    async def async_turn_on(A,**H):
        try:
            C=H.get(ATTR_RGB_COLOR,_A);D=H.get(ATTR_BRIGHTNESS,_A);logging.info(beta__("Y29sb3I6IHtfX3ZhcjB9", __var0=C));logging.info(beta__("YnJpZ2h0bmVzczoge19fdmFyMH0=", __var0=D))
            if C is not _A:
                C=tuple([int(A/255*100)for A in C]);E,F,G=A.generate_rgb_packets(A,C);B=await A.api.protocol.sender.send_packet_with_ack(E)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.r_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(F)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.g_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(G)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.b_channel))
                A._attr_state=_E;C=tuple([int(A/100*255)for A in C]);A._attr_rgb_color=C;A.default_color=C;logging.info(beta__("bmV3IGRlZmF1bHQgY29sb3I6IHtfX3ZhcjB9", __var0=C))
            elif D is not _A:
                D=max(1,min(255,D));D/=255;C=A.default_color or(0,0,0);logging.info(beta__("ZGVmYXVsdCBjb2xvcjoge19fdmFyMH0=", __var0=C));C=tuple([int(D*A*100/255)for A in C]);E,F,G=A.generate_rgb_packets(A,C);B=await A.api.protocol.sender.send_packet_with_ack(E)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.r_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(F)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.g_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(G)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.b_channel))
                logging.info(beta__("YnJpZ2h0ZW5lZCBjb2xvcjoge19fdmFyMH0=", __var0=C))
            else:
                logging.info(alpha__("TmVpdGhlciBjb2xvciBub3IgYnJpZ2h0bmVzcyBwcm92aWRlZCwgdXNpbmcgZGVmYXVsdCBjb2xvci4="));C=A.default_color or(0,0,0);A._attr_state=_E if A.default_color and A.default_color!=(0,0,0)else _C;A._attr_rgb_color=C;C=tuple([int(A*100/255)for A in C]);E,F,G=A.generate_rgb_packets(A,C);B=await A.api.protocol.sender.send_packet_with_ack(E)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.r_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(F)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.g_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(G)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.b_channel))
        except KeyError as I:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0=", __var0=I))
        A.async_write_ha_state()
    async def async_turn_off(A,**C):logging.info(alpha__("dHVybmluZyBvZmY="));logging.info(beta__("a3dhcmdzOiB7X192YXIwfQ==", __var0=C));D,E,F=A.generate_rgb_packets(A,(0,0,0));B=await A.api.protocol.sender.send_packet_with_ack(E);B=await A.api.protocol.sender.send_packet_with_ack(D);B=await A.api.protocol.sender.send_packet_with_ack(F);A._attr_state=_C;A._attr_rgb_color=0,0,0;A.async_write_ha_state()
class TISRGBWLight(LightEntity):
    def __init__(A,tis_api,gateway,device_id,r_channel,g_channel,b_channel,w_channel,light_name):A.api=tis_api;A.gateway=gateway;A.device_id=device_id;A.r_channel=int(r_channel);A.g_channel=int(g_channel);A.b_channel=int(b_channel);A.w_channel=int(w_channel);A._attr_name=light_name;A._attr_state=_A;A._attr_brightness=_A;A._attr_rgbw_color=_A;A.rgbw_value_flags=[0,0,0,0];A.listener=_A;A._attr_unique_id=beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn1fe19fdmFyM31fe19fdmFyNH0=", __var0=A.name, __var1=A.r_channel, __var2=A.g_channel, __var3=A.b_channel, __var4=A.w_channel);A.default_color=0,0,0,0;A.setup_light()
    def setup_light(A):A._attr_supported_color_modes={ColorMode.RGBW};A._attr_color_mode=ColorMode.RGBW;A._attr_supported_features=LightEntityFeature.TRANSITION;A.generate_rgbw_packets=handler.generate_rgbw_light_control_packet;A.update_packet=handler.generate_control_update_packet(A)
    async def async_added_to_hass(A):
        @callback
        async def B(event):
            B=event
            if B.event_type==str(A.device_id):
                if B.data[_B]==_F:logging.info(beta__("UkdCVyBldmVudCBkYXRhOiB7X192YXIwfQ==", __var0=B.data));C=B.data[_D];D=C[A.r_channel]/100*255;E=C[A.g_channel]/100*255;F=C[A.b_channel]/100*255;G=C[A.w_channel]/100*255;A._attr_rgbw_color=D,E,F,G;A._attr_state=bool(D or E or F or G)
                elif B.data[_B]==_G:A._attr_state=STATE_UNKNOWN
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
    async def async_turn_on(A,**E):
        try:
            C=E.get(ATTR_RGBW_COLOR,_A);D=E.get(ATTR_BRIGHTNESS,_A);logging.warning(beta__("a3dhcmdzOiB7X192YXIwfQ==", __var0=E))
            if C is not _A:
                C=tuple([int(A/255*100)for A in C]);F,G,H,I=A.generate_rgbw_packets(A,C);logging.info(beta__("Y29sb3IgKHBlcmNlbnQpOiB7X192YXIwfQ==", __var0=C));B=await A.api.protocol.sender.send_packet_with_ack(F)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.r_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(G)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.g_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(H)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.b_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(I)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.w_channel))
                A._attr_state=_E;C=tuple([int(A/100*255)for A in C]);A._attr_rgbw_color=C;A.default_color=C
            elif D is not _A:
                D=max(1,min(255,D));logging.warning(beta__("YnJpZ2h0bmVzczoge19fdmFyMH0sIHNlbGYuX2F0dHJfYnJpZ2h0bmVzczoge19fdmFyMX0=", __var0=D, __var1=A._attr_brightness));A._attr_brightness=D;D/=255;C=A.default_color or(0,0,0,0);logging.info(beta__("ZGVmYXVsdCBjb2xvcjoge19fdmFyMH0=", __var0=C));C=tuple([int(D*A*100/255)for A in C]);F,G,H,I=A.generate_rgbw_packets(A,C);B=await A.api.protocol.sender.send_packet_with_ack(F)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.r_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(G)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.g_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(H)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.b_channel))
                B=await A.api.protocol.sender.send_packet_with_ack(I)
                if not B:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0sIGNoYW5uZWw6IHtfX3ZhcjF9", __var0=B, __var1=A.w_channel))
                A._attr_state=_E;C=tuple([int(A/100*255)for A in C]);A._attr_rgbw_color=C
        except KeyError as J:logging.error(beta__("ZXJyb3IgdHVybmluZyBvbiBsaWdodDoge19fdmFyMH0=", __var0=J))
        A.async_write_ha_state()
    async def async_turn_off(A,**G):C,D,E,F=A.generate_rgbw_packets(A,(0,0,0,0));B=await A.api.protocol.sender.send_packet_with_ack(C);B=await A.api.protocol.sender.send_packet_with_ack(D);B=await A.api.protocol.sender.send_packet_with_ack(E);B=await A.api.protocol.sender.send_packet_with_ack(F);A._attr_state=_C;A._attr_rgbw_color=0,0,0,0;A.async_write_ha_state()