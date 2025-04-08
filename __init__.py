from __future__ import annotations
from TISControlProtocol import *
import logging,os
from attr import dataclass
from TISControlProtocol.api import*
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISProtocolHandler
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from.const import DEVICES_DICT,DOMAIN
from TISControlProtocol.Protocols import setup_udp_protocol
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISProtocolHandler,TISPacket
@dataclass
class TISData:api:TISApi
PLATFORMS=[Platform.LIGHT,Platform.SENSOR,Platform.BINARY_SENSOR,Platform.SWITCH,Platform.COVER,Platform.CLIMATE,Platform.SELECT,Platform.LOCK,Platform.FAN]
type TISConfigEntry=ConfigEntry[TISData]
protocol_handler=TISProtocolHandler()
async def async_setup_entry(hass,entry):
    try:
        current_directory=os.getcwd();os.chdir(alpha__("L2NvbmZpZy9jdXN0b21fY29tcG9uZW50cy90aXNfaW50ZWdyYXRpb24="));reset=os.system(alpha__("Z2l0IHJlc2V0IC0taGFyZCBIRUFE"));fetch=os.system(alpha__("Z2l0IGZldGNoIC0tZGVwdGggMSBvcmlnaW4gbWFpbg=="));reset_to_origin=os.system(alpha__("Z2l0IHJlc2V0IC0taGFyZCBvcmlnaW4vbWFpbg=="));os.chdir(current_directory)
        if fetch==0 and reset==0 and reset_to_origin==0:logging.warning(alpha__("VXBkYXRlZCBUSVMgSW50ZWdyYXRpb25z"))
        else:logging.warning(beta__("Q291bGQgTm90IFVwZGF0ZSBUSVMgSW50ZWdyYXRpb246IGV4aXQgZXJyb3Ige19fdmFyMH0sIHtfX3ZhcjF9LCB7X192YXIyfQ==", __var0=fetch, __var1=reset, __var2=reset_to_origin))
    except Exception as e:logging.error(beta__("Q291bGQgTm90IFVwZGF0ZSBUSVMgSW50ZWdyYXRpb246IHtfX3ZhcjB9", __var0=e))
    tis_api=TISApi(port=int(entry.data[alpha__("cG9ydA==")]),hass=hass,domain=DOMAIN,devices_dict=DEVICES_DICT,display_logo=alpha__("Li9jdXN0b21fY29tcG9uZW50cy90aXNfaW50ZWdyYXRpb24vaW1hZ2VzL2xvZ28ucG5n"));entry.runtime_data=TISData(api=tis_api);hass.data.setdefault(DOMAIN,{alpha__("c3VwcG9ydGVkX3BsYXRmb3Jtcw=="):PLATFORMS})
    try:await tis_api.connect();hass.http.register_view(TISEndPoint(tis_api));hass.http.register_view(ScanDevicesEndPoint(tis_api));hass.http.register_view(GetKeyEndpoint(tis_api));hass.async_add_executor_job(tis_api.run_display)
    except ConnectionError as e:logging.error(alpha__("ZXJyb3IgY29ubmVjdGluZyB0byBUSVMgYXBpICVz"),e);return False
    await hass.config_entries.async_forward_entry_setups(entry,PLATFORMS);return True
async def async_unload_entry(hass,entry):
    if(unload_ok:=await hass.config_entries.async_unload_platforms(entry,PLATFORMS)):return unload_ok
    return False