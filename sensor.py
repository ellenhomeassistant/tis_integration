from __future__ import annotations
from TISControlProtocol import *
_J=alpha__("bWRpOmN1cnJlbnQtYWM=")
_I=alpha__("bWRpOnRoZXJtb21ldGVy")
_H=alpha__("aGVhbHRoX3NlbnNvcg==")
_G=alpha__("dGVtcF9zZW5zb3I=")
_F=alpha__("YmlsbF9lbmVyZ3lfc2Vuc29y")
_E=alpha__("bW9udGhseV9lbmVyZ3lfc2Vuc29y")
_D=alpha__("YW5hbG9nX3NlbnNvcg==")
_C=None
_B=alpha__("ZmVlZGJhY2tfdHlwZQ==")
_A=alpha__("ZW5lcmd5X3NlbnNvcg==")
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
from.const import ENERGY_SENSOR_TYPES
from datetime import datetime
class TISSensorEntity:
    def __init__(A,device_id,api,gateway,channel_number):A.device_id=device_id;A.api=api;A.gateway=gateway;A.channel_number=channel_number
async def async_setup_entry(hass,entry,async_add_devices):
    B=hass;A=entry.runtime_data.api;await A.get_bill_configs();I=[]
    for(J,D)in RELEVANT_TYPES.items():
        K=await A.get_entities(platform=J)
        if K and len(K)>0:
            L=[(C,next(iter(A[alpha__("Y2hhbm5lbHM=")][0].values())),A[alpha__("ZGV2aWNlX2lk")],A[alpha__("aXNfcHJvdGVjdGVk")],A[alpha__("Z2F0ZXdheQ==")],A[alpha__("bWlu")],A[alpha__("bWF4")])for B in K for(C,A)in B.items()];C=[]
            for(E,F,G,P,H,min,max)in L:
                if J==_D:C.append(D(hass=B,tis_api=A,gateway=H,name=E,device_id=G,channel_number=F,min=min,max=max))
                elif J==_A:
                    for(M,N)in ENERGY_SENSOR_TYPES.items():C.append(D(hass=B,tis_api=A,gateway=H,name=beta__("e19fdmFyMH0ge19fdmFyMX0=", __var0=N, __var1=E),device_id=G,channel_number=F,key=M,sensor_type=_A))
                    C.append(D(hass=B,tis_api=A,gateway=H,name=beta__("TW9udGhseSBFbmVyZ3kge19fdmFyMH0=", __var0=E),device_id=G,channel_number=F,sensor_type=_E));C.append(D(hass=B,tis_api=A,gateway=H,name=beta__("QmlsbCB7X192YXIwfQ==", __var0=E),device_id=G,channel_number=F,sensor_type=_F))
                else:C.append(D(hass=B,tis_api=A,gateway=H,name=E,device_id=G,channel_number=F))
            I.extend(C)
    O=CPUTemperatureSensor(B);I.append(O);async_add_devices(I)
def get_coordinator(hass,tis_api,device_id,gateway,coordinator_type,channel_number):
    G=channel_number;F=tis_api;D=device_id;A=coordinator_type;E=beta__("e19fdmFyMH1fe19fdmFyMX0=", __var0=tuple(D), __var1=A)if _A not in A else beta__("e19fdmFyMH1fe19fdmFyMX1fe19fdmFyMn0=", __var0=tuple(D), __var1=A, __var2=G)
    if E not in coordinators:
        B=TISSensorEntity(D,F,gateway,G)
        if A==_G:C=protocol_handler.generate_temp_sensor_update_packet(entity=B)
        elif A==_H:C=protocol_handler.generate_health_sensor_update_packet(entity=B)
        elif A==_D:C=protocol_handler.generate_update_analog_packet(entity=B)
        elif A==_A:C=protocol_handler.generate_update_energy_packet(entity=B)
        elif A==_E:C=protocol_handler.generate_update_monthly_energy_packet(entity=B)
        elif A==_F:C=protocol_handler.generate_update_monthly_energy_packet(entity=B)
        coordinators[E]=SensorUpdateCoordinator(hass,F,timedelta(seconds=30),D,C)
    return coordinators[E]
protocol_handler=TISProtocolHandler()
_LOGGER=logging.getLogger(__name__)
coordinators={}
class CoordinatedTemperatureSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_G,C);super().__init__(D,name,B);A._attr_icon=_I;A.name=name;A.device_id=B;A.channel_number=C;A._attr_unique_id=beta__("c2Vuc29yX3tfX3ZhcjB9", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_B]==alpha__("dGVtcF9mZWVkYmFjaw=="):A._state=B.data[alpha__("dGVtcA==")]
                A.async_write_ha_state()
            except Exception as C:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgdGVtcGVyYXR1cmU6IHtfX3ZhcjB9", __var0=B.data))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
    @property
    def unit_of_measurement(self):return UnitOfTemperature.CELSIUS
class CoordinatedLUXSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_H,C);super().__init__(D,name,B);A._attr_icon=alpha__("bWRpOmJyaWdodG5lc3MtNg==");A.name=name;A.device_id=B;A.channel_number=C;A._attr_unique_id=beta__("c2Vuc29yX3tfX3ZhcjB9", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            B=event
            try:
                if B.data[_B]==alpha__("aGVhbHRoX2ZlZWRiYWNr"):A._state=int(B.data[alpha__("bHV4")])
                A.async_write_ha_state()
            except Exception as C:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgbHV4OiB7X192YXIwfQ==", __var0=B.data))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CoordinatedAnalogSensor(BaseSensorEntity,SensorEntity):
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number,min=0,max=100):C=channel_number;B=device_id;D=get_coordinator(hass,tis_api,B,gateway,_D,C);super().__init__(D,name,B);A._attr_icon=_J;A.name=name;A.device_id=B;A.channel_number=C;A.min=min;A.max=max;A._attr_unique_id=beta__("c2Vuc29yX3tfX3ZhcjB9", __var0=A.name)
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            C=event
            try:
                if C.data[_B]==alpha__("YW5hbG9nX2ZlZWRiYWNr"):D=int(C.data[alpha__("YW5hbG9n")][A.channel_number-1]);B=(D-A.min)/(A.max-A.min);B=max(0,min(1,B));A._state=int(B*100)
                A.async_write_ha_state()
            except Exception as E:logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgYW5hbG9nIHNlbnNvcjoge19fdmFyMH0gXG4gZXJyb3I6IHtfX3ZhcjF9", __var0=C.data, __var1=E))
            B=(D-A.min)/(A.max-A.min);B=max(0,min(1,B));return int(B*100)
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
class CPUTemperatureSensor(SensorEntity):
    def __init__(A,hass):A._cpu=CPUTemperature();A._state=A._cpu.temperature;A._hass=hass;A._attr_name=alpha__("Q1BVIFRlbXBlcmF0dXJlIFNlbnNvcg==");A._attr_icon=_I;A._attr_update_interval=timedelta(seconds=10);A._attr_unique_id=beta__("c2Vuc29yX3tfX3ZhcjB9", __var0=A.name);async_track_time_interval(A._hass,A.async_update,A._attr_update_interval)
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
    def __init__(A,hass,tis_api,gateway,name,device_id,channel_number,key=_C,sensor_type=_C):E=sensor_type;D=channel_number;C=tis_api;B=device_id;F=get_coordinator(hass,C,B,gateway,E,D);super().__init__(F,name,B);A._attr_icon=_J;A.api=C;A.name=name;A.device_id=B;A.channel_number=D;A._attr_unique_id=beta__("ZW5lcmd5X3tfX3ZhcjB9", __var0=A.name);A._key=key;A.sensor_type=E;A._attr_state_class=alpha__("bWVhc3VyZW1lbnQ=")
    async def async_added_to_hass(A):
        await super().async_added_to_hass()
        @callback
        def B(event):
            I=alpha__("cHJpY2VfcGVyX2t3");H=alpha__("bW9udGhseV9lbmVyZ3lfZmVlZGJhY2s=");F=alpha__("ZW5lcmd5");E=alpha__("Y2hhbm5lbF9udW0=");B=event
            try:
                if B.data[_B]==alpha__("ZW5lcmd5X2ZlZWRiYWNr")and A.sensor_type==_A:
                    if B.data[E]==A.channel_number:A._state=float(B.data[F].get(A._key,_C))
                elif B.data[_B]==H and A.sensor_type==_E:
                    if B.data[E]==A.channel_number:A._state=B.data[F]
                elif B.data[_B]==H and A.sensor_type==_F:
                    if B.data[E]==A.channel_number:
                        J=datetime.now().month;K=J in[6,7,8,9];C=A.api.bill_configs.get(alpha__("c3VtbWVyX3JhdGVz"),{})if K else A.api.bill_configs.get(alpha__("d2ludGVyX3JhdGVz"),{});G=B.data[F];D=_C
                        for(L,M)in enumerate(C):
                            if G<M[alpha__("bWluX2t3")]:D=C[L-1][I];break
                        if D is _C and len(C)>0:D=C[-1][I]
                        A._state=int(D*G)
                A.async_write_ha_state()
            except Exception as N:logging.error(beta__("ZXJyb3IgaW4gc2VsZi5uYW1lOiB7X192YXIwfSwgc2VsZi5fa2V5OiB7X192YXIxfSwgc2VsZi5zZW5zb3JfdHlwZToge19fdmFyMn0=", __var0=A.name, __var1=A._key, __var2=A.sensor_type));logging.error(beta__("ZXZlbnQgZGF0YSBlcnJvciBmb3IgZW5lcmd5IHNlbnNvcjoge19fdmFyMH0gXG4gZXJyb3I6IHtfX3ZhcjF9", __var0=B.data, __var1=N))
        A.hass.bus.async_listen(str(A.device_id),B)
    def _update_state(A,data):0
    @property
    def native_value(self):return self.state
RELEVANT_TYPES={alpha__("bHV4X3NlbnNvcg=="):CoordinatedLUXSensor,alpha__("dGVtcGVyYXR1cmVfc2Vuc29y"):CoordinatedTemperatureSensor,_D:CoordinatedAnalogSensor,_A:CoordinatedEnergySensor}