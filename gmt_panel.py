import bpy


class GmtPanel(bpy.types.Panel):
    bl_idname = "GMT_PT_panel"
    bl_label = "GMT Panel"
    bl_category = "Test Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # bl_context = "object"

    # target_action: bpy.types.Action

    def draw(self, context):

        layout = self.layout

        column = layout.column()

        if bpy.context.scene.target_armature is None:
            column.operator('object.import_fbx', text="Import Character")
        column.operator('object.init_character')
        # INIT CHARACTER

    def on_target_armature(self):
        # Update draw!
        pass

### OLDS!
        # if bpy.context.scene.target_armature is None:
        #     column.operator('gmt.import_fbx', text="Import Character")
        # for ob in bpy.context.selected_objects:
        #     if ob.type == 'ARMATURE':
        #         column.operator('gmt.assign_target', text='Set Selected To Main Character')
        #
        # column.prop(context.scene, "target_armature")
        #
        # column.operator('gmt.rename_bones', text="Rename Bones")
        # # column.operator('gmt.apply_transforms', text="Apply Transforms")
        # # column.operator('gmt.gmt.add_root_bone', text="Add Root Bone")
        # column.label(text="Animations")
        # column.operator('gmt.scale_hips', text="Scale Animation")
        # # column.operator('gmt.apply_root_motion', text="Apply Root Motion")

