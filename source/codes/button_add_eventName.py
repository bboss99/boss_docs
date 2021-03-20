from boss.ui_creator import UICreator, Boss_OT_base_ui, RectData


def onClicked():
    print('Button is Clicked')


def dragging(some_param):
    print(some_param)


def onWheel(caller, addby):
    caller.param += addby
    print('param is now', caller.param)


def ui_elements(op: Boss_OT_base_ui):
    button = UICreator.button(
        op=op,
        rectData=RectData(10, 110, 200, 100),
        text='ButtonText',
        buttonData=None,
        ttt='tool tip text',
        param=100
    )

    button.add_onClick(onClicked)
    button.add_onMouseEnter(lambda: print('mouse entered'))
    button.add_onMouseExit(lambda: print('mouse exited'))
    button.add_onWheelUp((onWheel, 1))
    button.add_onWheelDown((onWheel, -1))
    button.add_onDragBegin((dragging, 'dragging is started'))
    button.add_onDrag((dragging, "it's being dragged"))
    button.add_onDragEnd((dragging, 'dragging is ended'))
