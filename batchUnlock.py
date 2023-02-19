# functions as the opposite "lock and hide all" function in the channel box, instead unlocking and showing all channels. Works for multiple objects.
import maya.cmds as cmds

objs = cmds.ls(sl=True)
axis = ['x', 'y', 'z']
attrs = ['t', 'r', 's']
for ax in axis:
    for attr in attrs:
    	for obj in objs:
    		cmds.setAttr(obj+'.'+attr+ax, lock=0, keyable=True)
