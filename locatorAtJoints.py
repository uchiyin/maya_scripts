# Creates a locator for each selected joint at the joint's world position.
# Freezes locator transforms and centers pivot; parent constrains each joint to locator.

from maya import cmds

jnts = cmds.ls(typ = 'joint', sl=True)

if jnts:
    for obj in jnts:
        # get absolute (world) position of joint
        jntPos = cmds.xform(obj,q=True,t=True,ws=True)
        # name locator according to joint name
        objNameSplit = obj.split('_')
        nameLen = len(objNameSplit);
        objName = '_'.join(objNameSplit[:nameLen-1])
        loc = cmds.spaceLocator(p=jntPos, n=objName + '_loc')
        cmds.makeIdentity(loc, apply=True, t=1, r=1, s=1, n=0)
        cmds.xform(loc, centerPivots = True)
        
        ### constrain joints to locators
        cmds.parentConstraint(loc, obj, mo = True);
        
else:
    print('no joints selected');

