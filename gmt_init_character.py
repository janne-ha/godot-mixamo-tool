import bpy



class INIT_CHARACTER_OT(bpy.types.Operator):
    """Initializes imported model for the tool"""
    bl_idname = "object.init_character"
    bl_label = "Initialize Character"
    bl_description = "Used to mark Object as 'Main' character. Renames bones, " \
                     "applies transforms and adds a root (motion) bone."
    bl_options = {'REGISTER', 'UNDO'}

    # STEPS:
    # 1 Rename Bones
    # 2 Apply Transforms
    # 3 Add Root Bone
    # 4 Set as scene.target_armature

    target = None

    @classmethod
    def poll(cls, context):
        return bpy.context.scene.target_armature is None

    def execute(self, context):

        self.target = context.object

        # TODO: use scene.target_armature instead of bpy.context
        self._rename_bones()
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        self._add_root_bone()
        self._scale_animation()

        context.scene.target_armature = bpy.context.object.data

        return {'FINISHED'}

    def _add_root_bone(self):
        print("TODO: Add flesh to add_root_bone")
        return True

    def _scale_animation(self):
        """Scale the hips curves to correct animation curve scale"""
        "target: Object which animations to be scaled"

        action = self.target.animation_data.action

        #if not bpy.ops.armature:
        #    print("Please select the armature")

        #for action in bpy.data.actions:

        # Scale Hips Down to match the .01 scale on imported model
        fc = action.fcurves
        for f in fc:
            if f.data_path == 'pose.bones["Hips"].location':
                for keyframe in f.keyframe_points:
                    keyframe.co[1] *= .01
        return True

    def _rename_bones(self):
        """ Renames bones to Godot friendly. Armature must have names that are straight from mixamo.
            Both mixamo model and custom models that have been rigged in mixamo works.
        """

        # Checks
        is_target = False
        # Convenience assign
        armature = self.target.data

        # if self.target.type is not 'ARMATURE':
        #     print("Please Select an ARMATURE")
        #     return False

        # target_armature cannot be edited so must cache it during operations
        # TODO: make a functions for this..
        # if armature not in context.editable_objects:
        #     context.scene.target_armature = None
        #     is_target = True
        #     print("Armature was not editable so it probably was 'target_armature'")

        # Operations
        for mesh in self.target.children:
            for vg in mesh.vertex_groups:

                if ':' not in vg.name:
                    continue
                new_name = vg.name.split(":")[1]
                vg.name = new_name
        for bone in self.target.pose.bones:
            if ':' not in bone.name:
                continue
            new_name = bone.name.split(":")[1]
            bone.name = new_name
            pass

        # put target_armature back to its place
        # if is_target:
        #     context.scene.target_armature = armature

        print("Done renaming")
        return armature

