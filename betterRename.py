from maya import cmds

sel = cmds.ls(sl=True)
    
appendText = cmds.promptDialog(
    title='Rename',
    message='Enter text to append:',
    button=['Prefix','Suffix','Cancel'],
    defaultButton='Prefix',
    cancelButton='Cancel',
    dismissString='Cancel')
textToAdd = cmds.promptDialog(query=True, text=True)
for obj in sel:
    print(sel)
    if appendText == 'Prefix':
        try:
            cmds.rename(obj, textToAdd + obj)
        except:
            cmds.error('Invalid text entered.')
    elif appendText == 'Suffix':
        try:
            cmds.rename(obj, obj + textToAdd)
        except:
            cmds.error('Invalid text entered.')
    else:
        print('rename failed');