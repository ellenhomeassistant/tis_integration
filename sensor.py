from __future__ import annotations
from TISControlProtocol import *
_J=alpha__("bWRpOnRoZXJtb21ldGVy")
_I=alpha__("aGVhbHRoX3NlbnNvcg==")
_H=alpha__("dGVtcF9zZW5zb3I=")
_G=alpha__("YW5hbG9nX3NlbnNvcg==")
_F=alpha__("ZW5lcmd5")
_E=alpha__("Y2hhbm5lbF9udW0=")
_D=alpha__("ZW5lcmd5X2ZlZWRiYWNr")
_C=alpha__("bWRpOmN1cnJlbnQtYWM=")
_B=alpha__("ZW5lcmd5X3NlbnNvcg==")
_A=alpha__("ZmVlZGJhY2tfdHlwZQ==")
from datetime import timedelta
import logging
from gpiozero import CPUTemperature
from TISControlProtocol.api import TISApi
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISProtocolHandler
from homeassistant.components.sensor import SensorEntity,UnitOfTemperature
from homeassistant.core import Event,HomeAssistant,callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval
from.import TISConfigEntry
from.coordinator import SensorUpdateCoordinator
from.entities import BaseSensorEntity
class TISSensorEntity:
    def __init__(A,device_id,api,gateway,channel_number):A.device_id=device_id;A.api=api;A.gateway=gateway;A.channel_number=channel_number
async def async_setup_entry(hass,entry,async_add_devices):
    A=hass;B=entry.runtime_data.api;C=[]
    for(F,L)in RELEVANT_TYPES.items():
        for G in L:
            D=await B.get_entities(platform=F)
            if D and len(D)>0:
                M=[(C,next(iter(A[alpha__("Y2hhbm5lbHM=")][0].values())),A[alpha__("ZGV2aWNlX2lk")],A[alpha__("aXNfcHJvdGVjdGVk")],A[alpha__("Z2F0ZXdheQ==")],A[alpha__("bWlu")],A[alpha__("bWF4")])for B in D for(C,A)in B.items()];E=[]
                for(H,I,J,O,K,min,max)in M:
                    if F==_G:E.append(G(hass=A,tis_api=B,gateway=K,name=H,device_id=J,channel_number=I,min=min,max=max))
                    else:E.append(G(hass=A,tis_api=B,gateway=K,name=H,device_id=J,channel_number=I))
                C.extend(E)
    N=CPUTemperatureSensor(A);C.append(N);async_add_devices(C)
def get_coordinator(hass,tis_api,device_id,gateway,coordinator_type,channel_number):
    F=tis_api;D=device_id;A=coordinator_type;E=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=tuple(D), __var1=A)
    if E not in coordinators:
        logging.info(alpha__("Y3JlYXRpbmcgbmV3IGNvb3JkaW5hdG9y"));B=TISSensorEntity(D,F,gateway,channel_number)
        if A==_H:C=protocol_handler.generate_temp_sensor_update_packet(entity=B)
        elif A==_I:C=protocol_handler.generate_health_sensor_update_packet(entity=B)
        elif A==_G:C=protocol_handler.generate_update_analog_packet(entity=B)
        elif A==_B:C=protocol_handler.generate_update_energy_packet(entity=B)
        coordinators[E]=SensorUpdateCoordinator(hass,F,timedelta(seconds=30),D,C)
    return coordinators[E]
protocol_handler=TISProtocolHandler()
_LOGGER=logging.getLogger(__name__)
coordinators={}
class CoordinatedTemperatureSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_H,C);super().__init__(D,name,B);A._attr_icon=_J;A.name=name;A.device_id=B;A.channel_number=C;A._attr_unique_id=beta__("c2Vuc29yX3tfX3ZhcjB9", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_A]==alpha__("dGVtcF9mZWVkYmFjaw=="):A._state=B.data[alpha__("dGVtcA==")]
                A.async_write_ha_state()
            except Exception as C:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgdGVtcGVyYXR1cmU6IHtfX3ZhcjB9", __var0=B.data))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
    @property
    def unit_of_measurement(self):return UnitOfTemperature.CELSIUS
class CoordinatedLUXSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_I,C);super().__init__(D,name,B);A._attr_icon=alpha__("bWRpOmJyaWdodG5lc3MtNg==");A.name=name;A.device_id=B;A.channel_number=C;A._attr_unique_id=beta__("c2Vuc29yX3tfX3ZhcjB9", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_A]==alpha__("aGVhbHRoX2ZlZWRiYWNr"):A._state=int(B.data[alpha__("bHV4")])
                A.async_write_ha_state()
            except Exception as C:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgbHV4OiB7X192YXIwfQ==", __var0=B.data))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CoordinatedAnalogSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number,min=0,max=100):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_G,C);super().__init__(D,name,B);A._attr_icon=_C;A.name=name;A.device_id=B;A.channel_number=C;A.min=min;A.max=max;A._attr_unique_id=beta__("c2Vuc29yX3tfX3ZhcjB9", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            C=event
            try:
                if C.data[_A]==alpha__("YW5hbG9nX2ZlZWRiYWNr"):D=int(C.data[alpha__("YW5hbG9n")][A.channel_number-1]);B=(D-A.min)/(A.max-A.min);B=max(0,min(1,B));A._state=int(B*100)
                A.async_write_ha_state()
            except Exception as E:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgYW5hbG9nIHNlbnNvcjoge19fdmFyMH0gXG4gZXJyb3I6IHtfX3ZhcjF9", __var0=C.data, __var1=E))
            B=(D-A.min)/(A.max-A.min);B=max(0,min(1,B));return int(B*100)
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CPUTemperatureSensor(SensorEntity):
    def __init__(A,hass):A._cpu=CPUTemperature();A._state=A._cpu.temperature;A._hass=hass;A._attr_name=alpha__("Q1BVIFRlbXBlcmF0dXJlIFNlbnNvcg==");A._attr_icon=_J;A._attr_update_interval=timedelta(seconds=10);A._attr_unique_id=beta__("c2Vuc29yX3tfX3ZhcjB9", __var0=A.name);async_track_time_interval(A._hass,A.async_update,A._attr_update_interval)
    async def async_update(A,event_time):A._state=A._cpu.temperature;A.hass.bus.async_fire(alpha__("Y3B1X3RlbXBlcmF0dXJl"),{alpha__("dGVtcGVyYXR1cmU="):int(A._state)});A.async_write_ha_state()
    @property
    def should_poll(self):return False
    @property
    def state(self):return self._state
    @property
    def unit_of_measurement(self):return UnitOfTemperature.CELSIUS
    @property
    def name(self):return self._attr_name
class CoordinatedEnergySensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_B,C);super().__init__(D,name,B);A._attr_icon=_C;A.name=beta__("TGl2ZSB7X192YXIwfQ==", __var0=name);A.device_id=B;A.channel_number=C;A._attr_unique_id=beta__("ZW5lcmd5X3tfX3ZhcjB9", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_A]==_D:
                    if B.data[_E]==A.channel_number:C=int(B.data[_F][0]);A._state=C
                A.async_write_ha_state()
            except Exception as D:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgZW5lcmd5IHNlbnNvcjoge19fdmFyMH0gXG4gZXJyb3I6IHtfX3ZhcjF9", __var0=B.data, __var1=D))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CoordinatedPowerSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_B,C);super().__init__(D,name,B);A._attr_icon=_C;A.name=beta__("TW9udGhseSB7X192YXIwfQ==", __var0=name);A.device_id=B;A.channel_number=C;A._attr_unique_id=beta__("cG93ZXJfe19fdmFyMH0=", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_A]==_D:
                    if B.data[_E]==A.channel_number:C=int(B.data[_F][1]);A._state=C
                A.async_write_ha_state()
            except Exception as D:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgcG93ZXIgc2Vuc29yOiB7X192YXIwfSBcbiBlcnJvcjoge19fdmFyMX0=", __var0=B.data, __var1=D))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CoordinatedPhase1Sensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_B,C);super().__init__(D,name,B);A._attr_icon=_C;A.name=beta__("Vm9sdGFnZSAxIHtfX3ZhcjB9", __var0=name);A.device_id=B;A.channel_number=C;A._attr_unique_id=beta__("cGhhc2UxX3tfX3ZhcjB9", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_A]==_D:
                    if B.data[_E]==A.channel_number:C=int(B.data[_F][2]);A._state=C
                A.async_write_ha_state()
            except Exception as D:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgcGhhc2UxIHNlbnNvcjoge19fdmFyMH0gXG4gZXJyb3I6IHtfX3ZhcjF9", __var0=B.data, __var1=D))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CoordinatedPhase2Sensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_B,C);super().__init__(D,name,B);A._attr_icon=_C;A.name=beta__("Vm9sdGFnZSAyIHtfX3ZhcjB9", __var0=name);A.device_id=B;A.channel_number=C;A._attr_unique_id=beta__("cGhhc2UyX3tfX3ZhcjB9", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_A]==_D:
                    if B.data[_E]==A.channel_number:C=int(B.data[_F][3]);A._state=C
                A.async_write_ha_state()
            except Exception as D:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgcGhhc2UyIHNlbnNvcjoge19fdmFyMH0gXG4gZXJyb3I6IHtfX3ZhcjF9", __var0=B.data, __var1=D))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CoordinatedPhase3Sensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_B,C);super().__init__(D,name,B);A._attr_icon=_C;A.name=beta__("Vm9sdGFnZSAzIHtfX3ZhcjB9", __var0=name);A.device_id=B;A.channel_number=C;A._attr_unique_id=beta__("cGhhc2UzX3tfX3ZhcjB9", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_A]==_D:
                    if B.data[_E]==A.channel_number:C=int(B.data[_F][4]);A._state=C
                A.async_write_ha_state()
            except Exception as D:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgcGhhc2UzIHNlbnNvcjoge19fdmFyMH0gXG4gZXJyb3I6IHtfX3ZhcjF9", __var0=B.data, __var1=D))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
RELEVANT_TYPES={alpha__("bHV4X3NlbnNvcg=="):[CoordinatedLUXSensor],alpha__("dGVtcGVyYXR1cmVfc2Vuc29y"):[CoordinatedTemperatureSensor],_G:[CoordinatedAnalogSensor],_B:[CoordinatedEnergySensor,CoordinatedPowerSensor,CoordinatedPhase1Sensor,CoordinatedPhase2Sensor,CoordinatedPhase3Sensor]}