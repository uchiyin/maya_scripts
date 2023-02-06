from maya import cmds

allObjects = cmds.ls(typ = 'nurbsCurve', l=True, ni=True, o=True, r=True)
sel = cmds.ls(sl=True)

if sel:
    for obj in sel:
        selChild = cmds.listRelatives(obj, path = True)
        #selList += selChild[0]
        selChild = selChild[0]
        sel[sel.index(obj)] = selChild
        print(sel)
else:
    print('nothing selected');
    sel = allObjects;
    
colorChoose = cmds.promptDialog(
    title='Override Options',
    message='Enter Override Color (index, 1-32)',
    button=['OK','Cancel'],
    defaultButton='OK',
    cancelButton='Cancel',
    dismissString='Cancel')
if colorChoose == 'OK':
    colorChoice = cmds.promptDialog(query=True, text=True)
    try:
        colorChoiceIndex = int(colorChoice)
    except:
        cmds.error('Invalid color index entered.')

for obj in sel:

    par = cmds.listRelatives(obj, parent = True, path = True)
    if par:
        # get obj from listRelatives string
        par = par[0]
    # print(par, obj) # check obj validity
    
    try:
        cmds.setAttr(par + '.overrideEnabled', 1) # 0 = disable, 1 = enable
        cmds.setAttr(par + '.overrideColor', colorChoiceIndex)
    except:
        print("Obj: %s, Shape: %s _ color override failed!" % (par, obj))
        