# The MIT License (MIT)
#
# Copyright (c) 2019 Kevin J. Walters
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_midi.channel_pressure`
================================================================================

Channel Pressure MIDI message.


* Author(s): Kevin J. Walters

Implementation Notes
--------------------

"""

from .midi_message import MIDIMessage

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_MIDI.git"


class ChannelPressure(MIDIMessage):
    """Channel Pressure MIDI message.

    :param int pressure: The pressure, 0-127.
    """

    _STATUS = 0xD0
    _STATUSMASK = 0xF0
    LENGTH = 2

    def __init__(self, pressure, *, channel=None):
        self.pressure = pressure
        super().__init__(channel=channel)
        if not 0 <= self.pressure <= 127:
            raise self._EX_VALUEERROR_OOR

    def __bytes__(self):
        return bytes([self._STATUS | (self.channel & self.CHANNELMASK), self.pressure])

    @classmethod
    def from_bytes(cls, msg_bytes):
        return cls(msg_bytes[1], channel=msg_bytes[0] & cls.CHANNELMASK)


ChannelPressure.register_message_type()
