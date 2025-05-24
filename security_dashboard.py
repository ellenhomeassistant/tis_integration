from __future__ import annotations
from TISControlProtocol import *
import os
from ruamel.yaml import YAML
import logging
def create():
    M=alpha__("bWRpOmxvY2s=");L=alpha__("aWNvbg==");K=alpha__("c2VjdXJpdHktbG9jay1zZXR0aW5ncw==");F=alpha__("dGl0bGU=");E=alpha__("ZGFzaGJvYXJkcw==");B=alpha__("bG92ZWxhY2U=");N=os.path.dirname(__file__);G=os.path.abspath(os.path.join(N,alpha__("Li4vLi4v")));H=os.path.join(G,alpha__("Y29uZmlndXJhdGlvbi55YW1s"));I=alpha__("c2VjdXJpdHlfbG9ja19zZXR0aW5ncy55YW1s");J=os.path.join(G,I)
    try:
        D=YAML();D.preserve_quotes=True
        with open(H,alpha__("cg=="))as C:A=D.load(C)
        if B not in A:A[B]={}
        if E not in A[B]:A[B][E]={}
        if K not in A[B][E]:A[B][E][K]={alpha__("bW9kZQ=="):alpha__("eWFtbA=="),F:alpha__("U2VjdXJpdHkgTG9jayBTZXR0aW5ncw=="),L:M,alpha__("c2hvd19pbl9zaWRlYmFy"):True,alpha__("ZmlsZW5hbWU="):I}
        with open(H,alpha__("dw=="))as C:D.dump(A,C)
        if not os.path.exists(J):
            O={F:alpha__("dXJsX3BhdGg=")4,alpha__("dXJsX3BhdGg=")3:[{F:alpha__("dXJsX3BhdGg=")2,alpha__("dXJsX3BhdGg=")1:alpha__("dXJsX3BhdGg=")0,alpha__("Y2FyZHM="):[{alpha__("dHlwZQ=="):alpha__("YnV0dG9u"),alpha__("bmFtZQ=="):alpha__("Q2hhbmdlIFBhc3N3b3Jk"),L:M,alpha__("dGFwX2FjdGlvbg=="):{alpha__("YWN0aW9u"):alpha__("dXJs"),alpha__("dXJsX3BhdGg="):alpha__("aHR0cDovL2hvbWVhc3Npc3RhbnQubG9jYWw6ODAwMC9hcGkvY2hhbmdlLXBhc3N3b3Jk")}}]}]}
            with open(J,alpha__("dw=="))as C:D.dump(O,C)
    except Exception as P:logging.error(beta__("Q291bGQgTm90IFNldHVwIFNlY3VyaXR5IFNldHRpbmdzIERhc2hib2FyZDoge19fdmFyMH0=", __var0=P))