#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

# Standard library imports
import ssl

# To get the library this bot uses run pip3 install irc
import irc.bot, irc.connection

class EB3( irc.bot.SingleServerIRCBot ):
    """Usage: EB3( config=dict, data=dict, wrSelf=self ) """
    def __init__( self, 
            wrSelf,
            config,
            data ):
        if config.useSSL: #Whether to use SSL or not
            ssl_factory = irc.connection.Factory( wrapper=ssl.wrap_socket )
            irc.bot.SingleServerIRCBot.__init__( self, 
                    [(config.server, config.port)], 
                    config.nickname, config.realname, 
                    connect_factory=ssl_factory)
        else:
            irc.bot.SingleServerIRCBot.__init__( self,
                [(config.server, config.port)],
                config.nickname, config.realname)
        self.data = data
        self.config = config
        self.wrapper = wrSelf # Allows bot module to call / contact wrapper
