from __future__ import annotations
from TISControlProtocol import *
import logging,os
from ruamel.yaml import YAML
from attr import dataclass
from TISControlProtocol.api import*
from TISControlProtocol.Protocols.udp.ProtocolHandler import TISProtocolHandler
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from.const import DEVICES_DICT,DOMAIN
@dataclass
class TISData:api:TISApi
PLATFORMS=[Platform.LIGHT,Platform.SENSOR,Platform.BINARY_SENSOR,Platform.SWITCH,Platform.COVER,Platform.CLIMATE,Platform.SELECT,Platform.LOCK,Platform.FAN]
type TISConfigEntry=ConfigEntry[TISData]
protocol_handler=TISProtocolHandler()
async def async_setup_entry(hass,entry):
    G=alpha__("bWRpOmxvY2s=");F=alpha__("aWNvbg==");E=alpha__("c2VjdXJpdHktbG9jay1zZXR0aW5ncw==");D=alpha__("dGl0bGU=");C=True;B=alpha__("ZGFzaGJvYXJkcw==");A=alpha__("bG92ZWxhY2U=")
    try:
        current_directory=os.getcwd();os.chdir(alpha__("L2NvbmZpZy9jdXN0b21fY29tcG9uZW50cy90aXNfaW50ZWdyYXRpb24="));reset=os.system(alpha__("Z2l0IHJlc2V0IC0taGFyZCBIRUFE"));fetch=os.system(alpha__("Z2l0IGZldGNoIC0tZGVwdGggMSBvcmlnaW4gbWFpbg=="));reset_to_origin=os.system(alpha__("Z2l0IHJlc2V0IC0taGFyZCBvcmlnaW4vbWFpbg=="));os.chdir(current_directory)
        if fetch==0 and reset==0 and reset_to_origin==0:logging.warning(alpha__("VXBkYXRlZCBUSVMgSW50ZWdyYXRpb25z"))
        else:logging.warning(beta__("Q291bGQgTm90IFVwZGF0ZSBUSVMgSW50ZWdyYXRpb246IGV4aXQgZXJyb3Ige19fdmFyMH0sIHtfX3ZhcjF9LCB7X192YXIyfQ==", __var0=fetch, __var1=reset, __var2=reset_to_origin))
    except Exception as e:logging.error(beta__("Q291bGQgTm90IFVwZGF0ZSBUSVMgSW50ZWdyYXRpb246IHtfX3ZhcjB9", __var0=e))
    current_dir=os.path.dirname(__file__);base_dir=os.path.abspath(os.path.join(current_dir,alpha__("Li4vLi4v")));config_path=os.path.join(base_dir,alpha__("Y29uZmlndXJhdGlvbi55YW1s"));dashboard_filename=alpha__("c2VjdXJpdHlfbG9ja19zZXR0aW5ncy55YW1s");dashboard_path=os.path.join(base_dir,dashboard_filename)
    try:
        yaml=YAML();yaml.preserve_quotes=C
        with open(config_path,alpha__("cg=="))as f:config=yaml.load(f)
        if A not in config:config[A]={}
        if B not in config[A]:config[A][B]={}
        if E not in config[A][B]:config[A][B][E]={alpha__("bW9kZQ=="):alpha__("eWFtbA=="),D:alpha__("U2VjdXJpdHkgTG9jayBTZXR0aW5ncw=="),F:G,alpha__("c2hvd19pbl9zaWRlYmFy"):C,alpha__("ZmlsZW5hbWU="):dashboard_filename}
        with open(config_path,alpha__("dw=="))as f:yaml.dump(config,f)
        if not os.path.exists(dashboard_path):
            dashboard_content={D:alpha__("dXJsX3BhdGg=")4,alpha__("dXJsX3BhdGg=")3:[{D:alpha__("dXJsX3BhdGg=")2,alpha__("dXJsX3BhdGg=")1:alpha__("dXJsX3BhdGg=")0,alpha__("Y2FyZHM="):[{alpha__("dHlwZQ=="):alpha__("YnV0dG9u"),alpha__("bmFtZQ=="):alpha__("Q2hhbmdlIFBhc3N3b3Jk"),F:G,alpha__("dGFwX2FjdGlvbg=="):{alpha__("YWN0aW9u"):alpha__("dXJs"),alpha__("dXJsX3BhdGg="):alpha__("aHR0cDovL2hvbWVhc3Npc3RhbnQubG9jYWw6ODAwMC9hcGkvY2hhbmdlLXBhc3N3b3Jk")}}]}]}
            with open(dashboard_path,alpha__("dw=="))as f:yaml.dump(dashboard_content,f)
    except Exception as e:logging.error(beta__("Q291bGQgTm90IFNldHVwIFNlY3VyaXR5IFNldHRpbmdzIERhc2hib2FyZDoge19fdmFyMH0=", __var0=e))
    tis_api=TISApi(port=int(entry.data[alpha__("cG9ydA==")]),hass=hass,domain=DOMAIN,devices_dict=DEVICES_DICT,display_logo=alpha__("Li9jdXN0b21fY29tcG9uZW50cy90aXNfaW50ZWdyYXRpb24vaW1hZ2VzL2xvZ28ucG5n"));entry.runtime_data=TISData(api=tis_api);hass.data.setdefault(DOMAIN,{alpha__("c3VwcG9ydGVkX3BsYXRmb3Jtcw=="):PLATFORMS})
    try:await tis_api.connect()
    except ConnectionError as e:logging.error(alpha__("ZXJyb3IgY29ubmVjdGluZyB0byBUSVMgYXBpICVz"),e);return False
    await hass.config_entries.async_forward_entry_setups(entry,PLATFORMS);return C
async def async_unload_entry(hass,entry):
    if(unload_ok:=await hass.config_entries.async_unload_platforms(entry,PLATFORMS)):return unload_ok
    return False