import bpy


class GMT_IMPORT_OT( bpy.types.Operator ):
    """Import fbx file downloaded from Mixamo"""
    bl_idname = "object.import_fbx"
    bl_label = "Import"
    bl_description = "Import .fbx file downloaded from Mixamo"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.import_scene.fbx("INVOKE_REGION_WIN")
        # While loop to wait for import?

        return {'FINISHED'}



### MOVED TO gmt_init_character.py!
#
# class RENAME_BONES_OT(bpy.types.Operator):
#     """ Renames bones to Godot friendly. Armature must have names that are straight from mixamo.
#         Both mixamo model and custom models that have been rigged in mixamo works.
#      """
#     bl_idname = "object.rename_bones"
#     bl_label = "Rename Bones"
#     bl_description = "Rename bones in armature"
#     bl_options = {'REGISTER', 'UNDO'}
#
#     def execute(self, context):
#
#         # Checks
#         is_target = False
#         # Convenience assign
#         rig = bpy.context.object
#
#         if rig is not 'ARMATURE':
#             print("Please Select an ARMATURE")
#             return {'CANCELLED'}
#
#         # target_armature cannot be edited so must cache it during operations
#         # TODO: make a functions for this..
#         if rig not in bpy.context.editable_objects:
#             bpy.context.scene.target_armature = None
#             is_target = True
#             print("Armature was not editable so it probably was 'target_armature'")
#
#         # Operations
#         for mesh in rig.children:
#             for vg in mesh.vertex_groups:
#
#                 if ':' not in vg.name:
#                     continue
#                 new_name = vg.name.split(":")[1]
#                 vg.name = new_name
#         for bone in rig.pose.bones:
#             print("Bone name: {}".format(bone.name))
#             if ':' not in bone.name:
#                 continue
#             new_name = bone.name.split(":")[1]
#             bone.name = new_name
#             pass
#
#         # put target_armature back to its place
#         if is_target:
#             bpy.context.scene.target_armature = rig
#
#         return {'FINISHED'}


