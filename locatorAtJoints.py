# Creates a locator for each selected joint at the joint's world position. Locator named after joint.

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
        cmds.spaceLocator(p=jntPos, n=objName + '_loc')
else:
    print('no joints selected');

