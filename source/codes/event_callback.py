from boss.ui_creator import UICreator, Boss_OT_base_ui, ButtonData, RectData


def onClicked():
    print('added while creating button object')


def onClicked1(p_one, p_two, p_three):
    print(p_one, p_two, p_three)


def onClicked2(caller):
    print(caller, 'is the button instance, param =', caller.param)


def onClicked3(caller, p_one, p_two, p_three):
    print(caller.param, p_one, p_two, p_three)


def ui_elements(op: Boss_OT_base_ui):
    button = UICreator.button(
        op=op,
        rectData=RectData(10, 110, 200, 100),
        text='ButtonText',
        buttonData=ButtonData(onClick=onClicked),
        ttt='tool tip text',
        param=(1, 'two', 3.0)
    )
    # This adds callback
    button.add_onClick(onClicked1, 1, 'two', 3.0)
    button.add_onClick(onClicked2)
    button.add_onClick(onClicked3, 1, 'two', 3.0)
    button.add_onClick(lambda caller: print('lambda-', caller, caller.param))
