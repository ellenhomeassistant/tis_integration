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
from.import tis_configuration_dashboard
import aiofiles,ruamel.yaml,io
@dataclass
class TISData:api:TISApi
PLATFORMS=[Platform.LIGHT,Platform.SENSOR,Platform.BINARY_SENSOR,Platform.SWITCH,Platform.COVER,Platform.CLIMATE,Platform.SELECT,Platform.LOCK,Platform.FAN]
type TISConfigEntry=ConfigEntry[TISData]
protocol_handler=TISProtocolHandler()
async def async_setup_entry(hass,entry):
    A=alpha__("aHR0cA==");tis_configuration_dashboard.create();current_dir=os.path.dirname(__file__);base_dir=os.path.abspath(os.path.join(current_dir,alpha__("Li4vLi4v")));config_path=os.path.join(base_dir,alpha__("Y29uZmlndXJhdGlvbi55YW1s"));yaml=ruamel.yaml.YAML()
    async with aiofiles.open(config_path,alpha__("cg=="))as f:contents=await f.read()
    config_data=await hass.async_add_executor_job(yaml.load,contents);http_settings={alpha__("dXNlX3hfZm9yd2FyZGVkX2Zvcg=="):True,alpha__("dHJ1c3RlZF9wcm94aWVz"):[alpha__("MTcyLjMwLjMzLjAvMjQ=")]}
    if A not in config_data or config_data[A]!=http_settings:
        logging.warning(alpha__("QWRkaW5nIEhUVFAgY29uZmlndXJhdGlvbiB0byBjb25maWd1cmF0aW9uLnlhbWw="));config_data[A]=http_settings;buffer=io.StringIO();await hass.async_add_executor_job(yaml.dump,config_data,buffer)
        async with aiofiles.open(config_path,alpha__("dw=="))as f:await f.write(buffer.getvalue())
    else:logging.info(alpha__("SFRUUCBjb25maWd1cmF0aW9uIGFscmVhZHkgZXhpc3RzIGluIGNvbmZpZ3VyYXRpb24ueWFtbA=="))
    tis_api=TISApi(port=int(entry.data[alpha__("cG9ydA==")]),hass=hass,domain=DOMAIN,devices_dict=DEVICES_DICT,display_logo=alpha__("Li9jdXN0b21fY29tcG9uZW50cy90aXNfaW50ZWdyYXRpb24vaW1hZ2VzL2xvZ28ucG5n"));entry.runtime_data=TISData(api=tis_api);hass.data.setdefault(DOMAIN,{alpha__("c3VwcG9ydGVkX3BsYXRmb3Jtcw=="):PLATFORMS})
    try:await tis_api.connect()
    except ConnectionError as e:logging.error(alpha__("ZXJyb3IgY29ubmVjdGluZyB0byBUSVMgYXBpICVz"),e);return False
    await hass.config_entries.async_forward_entry_setups(entry,PLATFORMS);return True
async def async_unload_entry(hass,entry):
    if(unload_ok:=await hass.config_entries.async_unload_platforms(entry,PLATFORMS)):return unload_ok
    return False