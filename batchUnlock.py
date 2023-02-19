import maya.cmds as cmds

objs = cmds.ls(sl=True)
axis = ['x', 'y', 'z']
attrs = ['t', 'r', 's']
for ax in axis:
    for attr in attrs:
    	for obj in objs:
    		cmds.setAttr(obj+'.'+attr+ax, lock=0, keyable=True)