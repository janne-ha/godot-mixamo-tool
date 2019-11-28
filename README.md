#Godot Mixamo tool

Utility addon for Blender to help you get animations and rigged characters
from [Mixamo](https://www.Mixamo.com) to [Godot Game Engine](https://www.godotengine.org)

Tool is located in Sidebar panel ( Press 'N' to toggle it while mouse over the 3d viewport ).

This is designed for a person that is completely new to Blender to be able to get animations
and models into Godot.

At current just import of character and initialising ( Renames bones, Reset transforms and 
 scales animations ) is supported. No error checks so keep your main 'Armature' selected.
 
 Further plans:
 
    - create a list of actions(animation clip) for the character
    - ability to add/remove/disable actions
    - have a button to import animations
        - this would import fbx-file
        - hide it into a collection
        - scale its animations
        - copy its action to main characters list
    - add root motion toggle for each action
    - play/pause button for selected action to preview 
    