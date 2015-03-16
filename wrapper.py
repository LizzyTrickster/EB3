#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

import EB3IRC

bots = dict()

GlobalData = dict()

if __name__ == "__main__":
	bID = 1
	for IRCBot in config.IRC:
		# { srv="localhost", prt=6667, useSSL=False, sPass="", nName="EB3", rName="EB3"}
		bots[ bID ] = EB3IRC.EB3( GlobalData, IRCBot )
		bID = bID + 1