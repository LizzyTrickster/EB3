#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

import EB3IRC

import json, sys

bots = dict()

GlobalData = dict()

class configulator( object ):
    """ Configuration Manager """
    def __init__(self, create=0, confFile="EB3.json", dataDirBase="data/"):
        self.cFile = str( confFile )
        try:
            with open(self.cFile, "r") as theFile: # My variable names are awesome, dont lie....
                self.conf = json.loads( theFile.read() )
        except ValueError:
            print( "Error: Primary config ({c}) is corrupt (or not valid JSON!)!".format( c=self.cFile ) )
            sys.exit(1)
        except FileNotFoundError:
            if bool(create):
                print( "[WARN] Config file not found but create was specified, dumping default configuration to {f}!".format( f=confFile ) )
                defD = {"IRC":{"BRTD":{"server":"thedarkirc.co","port":6697,"useSSL":True,"sPass":"","nick":"Brain","realname":"" } }, "HTTP": {}, "XMPP": {} }
                defS = json.dumps( defD, sort_keys=True, indent=2 )
                with open( self.cFile, "w" ) as theFile:
                    theFile.write( defS )
                print( "[INFO] Config written to {f}, please add in your desired configurations!".format(f=confFile) )
                sys.exit(-1)
            elif not bool(create):
                print( "[ERROR] Config file ({f}) not found! Are you sure that it's there?".format(f=confFile) )
                sys.exit(2)
    



if __name__ == "__main__":
    config = configulator( create=1 )
    print( config.conf )
#    bID = 1
#    for IRCBot in config.IRC:
#        # { srv="localhost", prt=6667, useSSL=False, sPass="", nName="EB3", rName="EB3"}
#        bots[ bID ] = EB3IRC.EB3( GlobalData, IRCBot )
#        bID = bID + 1
