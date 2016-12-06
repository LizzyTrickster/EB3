# EB3
EB3, generation 3 (first iteration) of my IRC Bot

The code here is not complete at all and will most likely not work, I am working on a newer version so this is just here for legacy purposes.

How this was planned to work:

Wrapper will load configuration file and analyse it. It will work out what modules it has to load (IRC only for now) and then load them passing them their config and global data.
The modules will then do their stuff and manage themselves. 
When there's an update the wrapper will call a function in the modules which contacts the owner (me) saying there's an update and listing what files changed.
If a *master* module needs updating, when the update command is ran for it it will tell the wrapper and the wrapper will reload it, calling unload functions as neccessary.
