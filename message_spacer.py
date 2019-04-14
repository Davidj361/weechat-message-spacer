# Message Spacer - Adds newlines/separators between messages of different users
# Copyright (C) 2019  davidj361 <david.j.361@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import weechat

SCRIPT_NAME    = "message_spacer"
SCRIPT_AUTHOR  = "davidj361 <david.j.361@gmail.com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPL"
SCRIPT_DESC    = "Adds spaces/separators between messages of different users"

bufLastNick = {}

def separate(data, line):
    buf = line['buffer']
    nick = line['prefix']
    if buf in bufLastNick and nick != bufLastNick[buf]:
        weechat.prnt(buf, '\t\t')
    bufLastNick[buf] = nick
    return {}

if __name__ == "__main__":
    if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", ""):
        weechat.hook_line('', '', 'irc_privmsg', 'separate', '')
