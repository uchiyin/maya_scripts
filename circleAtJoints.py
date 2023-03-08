# Creates a control curve at each of the selected joints, parenting them according if they are part of the same hierarchy.

from maya import cmds

jnts = cmds.ls(typ = 'joint', sl=True)
jntList = [];

if jnts:
    for obj in jnts:
        # get absolute (world) position of joint
        jntPos = cmds.xform(obj,q=True,t=True,ws=True)
        # get rotation of joint
        jntRot = cmds.joint(obj,q=True,o=True)
        # get radius of joint
        jntSize = cmds.joint(obj, rad=True, q = True)
        # get locator of joint
        locParent = cmds.parentConstraint(obj, tl = True, q = True)
        # name curve according to joint name
        objNameSplit = obj.split('_')
        nameLen = len(objNameSplit);
        objName = '_'.join(objNameSplit[:nameLen-1])
        
        selChildren = cmds.listRelatives(obj, typ = 'joint', c=True,path = True) # list of all child joints
        
        if selChildren: # avoid creating controls on tip joints
            childPosSumX = 0.0;
            childPosSumY = 0.0;
            childPosSumZ = 0.0;
            
            for chld in selChildren:
                chldPos = cmds.xform(chld, q=True, t=True, ws=True);
                childPosSumX += chldPos[0];
                childPosSumY += chldPos[1];
                childPosSumZ += chldPos[2];
                
            jntCount = len(selChildren);
            normX = childPosSumX / jntCount;
            normY = childPosSumY / jntCount;
            normZ = childPosSumZ / jntCount;
    
            chldNorm = [normX - jntPos[0], normY - jntPos[1], normZ - jntPos[2]]; #calculate normal from child joint to parent
            
            # create NURBS circle CTRL
            circ = cmds.circle( c=jntPos, r=jntSize[0]*3,n=objName + '_CTRL', nrx = chldNorm[0],nry = chldNorm[1], nrz = chldNorm[2]);
            cmds.makeIdentity(circ, apply=True, t=1, r=1, s=1, n=0)
            cmds.xform(circ, centerPivots = True)
            ### constrain locators to curves
            cmds.parentConstraint(circ, locParent, mo = True);
            
    for obj in jnts: # parenting after creation of controls
            
        # get list of joint parent hierarchy
        parents = cmds.ls(obj, long=True)[0].split('|')[1:-1]
        parents.reverse()
        print(parents)
        
        # check if parent curves exist; if so, parent
        for par in parents:
            
            objNameSplit = obj.split('_')
            nameLen = len(objNameSplit);
            circName = '_'.join(objNameSplit[:nameLen-1]) + '_CTRL';
        
            parNameSplit = par.split('_')
            parNameLen = len(parNameSplit);
            parName = '_'.join(parNameSplit[:parNameLen-1]) + '_CTRL';
            
            if cmds.objExists(parName) and cmds.objExists(circName):
                cmds.parent(circName, parName)
                break;
        
        
else:
    print('no joints selected');

# would be cool to know how to generate an in-view editor for curve size... will have to get into Maya API.