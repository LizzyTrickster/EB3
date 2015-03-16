#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

import ssl

# To get the library this bot uses run pip3 install irc
import irc.bot, irc.connection

class EB3( irc.bot.SingleServerIRCBot ):
    """docstring for EB3"""
    def __init__( self, 
            config={ server="localhost", port=6667, useSSL=False, sPass="", nickname="EB3", realname="EB3", channel=""},
            data,
            wrSelf ):
        if config.useSSL:
            ssl_factory = irc.connection.Factory( wrapper=ssl.wrap_socket )
            irc.bot.SingleServerIRCBot.__init__( self, 
                    [(config.server, config.port)], 
                    config.nickname,
                    config.realname, 
                    connect_factory=ssl_factory)
        else:
            irc.bot.SingleServerIRCBot.__init__( self,
                [(config.server, config.port)],
                config.nickname,
                config.realname)
        self.data = data
        self.wrapper = wrSelf
