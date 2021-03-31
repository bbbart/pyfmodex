from enum import Enum
from .enums import DSP_TYPE
from .dsp import DSP


class REVERB_PRESET(Enum):
    OFF = (1000, 7, 11, 5000, 100, 100, 100, 250, 0, 20, 96, -80.0)
    GENERIC = (1500, 7, 11, 5000, 83, 100, 100, 250, 0, 14500, 96, -8.0)
    PADDEDCELL = (170, 1, 2, 5000, 10, 100, 100, 250, 0, 160, 84, -7.8)
    ROOM = (400, 2, 3, 5000, 83, 100, 100, 250, 0, 6050, 88, -9.4)
    BATHROOM = (1500, 7, 11, 5000, 54, 100, 60, 250, 0, 2900, 83, -0.5)
    LIVINGROOM = (500, 3, 4, 5000, 10, 100, 100, 250, 0, 160, 58, -19.0)
    STONEROOM = (2300, 12, 17, 5000, 64, 100, 100, 250, 0, 7800, 71, -8.5)
    AUDITORIUM = (4300, 20, 30, 5000, 59, 100, 100, 250, 0, 5850, 64, -11.7)
    CONCERTHALL = (3900, 20, 29, 5000, 70, 100, 100, 250, 0, 5650, 80, -9.8)
    CAVE = (2900, 15, 22, 5000, 100, 100, 100, 250, 0, 20000, 59, -11.3)
    ARENA = (7200, 20, 30, 5000, 33, 100, 100, 250, 0, 4500, 80, -9.6)
    HANGAR = (10000, 20, 30, 5000, 23, 100, 100, 250, 0, 3400, 72, -7.4)
    CARPETTEDHALLWAY = (
        300,
        2,
        30,
        5000,
        10,
        100,
        100,
        250,
        0,
        500,
        56,
        -24.0,
    )
    HALLWAY = (1500, 7, 11, 5000, 59, 100, 100, 250, 0, 7800, 87, -5.5)
    STONECORRIDOR = (
        270,
        13,
        20,
        5000,
        79,
        100,
        100,
        250,
        0,
        9000,
        86,
        -6.0,
    )
    ALLEY = (1500, 7, 11, 5000, 86, 100, 100, 250, 0, 8300, 80, -9.8)
    FOREST = (1500, 162, 88, 5000, 54, 79, 100, 250, 0, 760, 94, -12.3)
    CITY = (1500, 7, 11, 5000, 67, 50, 100, 250, 0, 4050, 66, -26.0)
    MOUNTAINS = (1500, 300, 100, 5000, 21, 27, 100, 250, 0, 1220, 82, -24.0)
    QUARRY = (1500, 61, 25, 5000, 83, 100, 100, 250, 0, 3400, 100, -5.0)
    PLAIN = (1500, 179, 100, 5000, 50, 21, 100, 250, 0, 1670, 65, -28.0)
    PARKINGLOT = (1700, 8, 12, 5000, 100, 100, 100, 250, 0, 20000, 56, -19.5)
    SEWERPIPE = (2800, 14, 21, 5000, 14, 80, 60, 250, 0, 3400, 66, -1.2)
    UNDERWATER = (1500, 7, 11, 5000, 10, 100, 100, 250, 0, 500, 92, -7.0)


def set_reverb_preset(reverb, preset):
    if type(reverb) != DSP:
        raise Exception("Parameter must be a DSP instance")
    if reverb.type != DSP_TYPE.SFXREVERB:
        raise Exception("Type of Dsp instance must be of SFXREVERB type")
    if type(preset) != REVERB_PRESET:
        raise Exception("Preset not valid")
    for index, value in enumerate(preset.value):
        reverb.set_parameter_float(index, value)
