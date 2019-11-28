import bpy
from bpy.props import PointerProperty

bl_info = {
    "name": "Godot Mixamo Tools",
    "author": "janne-ha",
    "description": "Addon to streamline godot and mixamo pipeline",
    "blender": (2, 80, 0),
    "location": "View3D",
    "version": "0.0.2",
    "warning": "This addon is still in development",
    "category": "Object"
}

from . gmt_init_character import INIT_CHARACTER_OT
from . gmt_tools import GMT_IMPORT_OT
from . gmt_panel import GmtPanel


# TODO: Make a set/get to notify panel
bpy.types.Scene.target_armature = PointerProperty(name="MainCharacter", type=bpy.types.Armature)

classes = (INIT_CHARACTER_OT, GMT_IMPORT_OT, GmtPanel)

register, unregister = bpy.utils.register_classes_factory(classes)