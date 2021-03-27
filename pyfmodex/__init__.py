"""Fmod ex python bindings."""

from .fmodex import (
    get_disk_busy,
    set_disk_busy,
    get_memory_stats,
    initialize_debugging,
    initialize_memory,
)
from . import globalvars

# Avoid recursive import hell
from . import (
    dsp,
    dsp_connection,
    geometry,
    channel,
    channel_group,
    reverb,
    sound,
    sound_group,
    system,
)
from .utils import FmodError

# import reverb presets
from .reverb_presets import REVERB_PRESET, set_reverb_preset

# import structures to be used with Resonance Audio plugin
from .roomproperties import MaterialNames, RoomProperties

__version__ = "0.7.0"

c = {
    "DSP": dsp.DSP,
    "DSP_Connection": dsp_connection.DSPConnection,
    "Geometry": geometry.Geometry,
    "Channel": channel.Channel,
    "ChannelGroup": channel_group.ChannelGroup,
    "Reverb3D": reverb.Reverb3D,
    "Sound": sound.Sound,
    "SoundGroup": sound_group.SoundGroup,
    "System": system.System,
}

globalvars.class_list = c
from . import constants

System = c["System"]
