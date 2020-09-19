"""
A demonstration script showing how to parent a QDialog to the Blender main window.
Yes, this could be done with QtWidgets.QMessageBox more easily.
The point is to show how to parent a window to the Blender application.

**Author:**

    Jeff Hanna, jeff.b.hanna@gmail.com, June 1, 2020
"""

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QDialog, QHBoxLayout, QLabel, QPushButton


class HelloWorldDialog(QDialog):
    """
    A sample 'Hello World!' QDialog.

    **Arguments:**

        None

    **Keyword Arguments:**

        None

    **Author:**

        Jeff Hanna, jeff.b.hanna@gmail.com, June 1, 2020
    """

    def __init__(self, parent):
        super().__init__(parent, Qt.WindowCloseButtonHint | Qt.WindowSystemMenuHint | Qt.WindowTitleHint)

        self.resize(200, 50)
        self.setWindowTitle('Qt for Python in Blender')

        lbl_hw = QLabel('Hello World!')
        btn_fbx = QPushButton('FBX Export')
        btn_fbx.clicked.connect(export_fbx)

        main_layout = QHBoxLayout()
        main_layout.addWidget(lbl_hw)
        main_layout.addWidget(btn_fbx)
        self.setLayout(main_layout)


def export_fbx():
    import bpy
    ctx = bpy.context.copy()
    stop = False
    for screen in bpy.data.screens:
        if stop:
            break
        for area in screen.areas:
            if stop:
                break
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if stop:
                        break
                    if region.type == 'WINDOW':
                        ctx['area'] = area
                        ctx['screen'] = screen
                        ctx['region'] = region
                        ctx['workspace'] = bpy.data.workspaces[screen.name]
                        ctx['space_data'] = area.spaces[0]
                        ctx['scene'] = bpy.data.scenes[0]
                        ctx['window'] = bpy.data.window_managers[0].windows[0]
                        ctx['window_manager'] = bpy.data.window_managers[0]
                        ctx['active_object'] = bpy.data.objects['Cube']
                        print(screen.name)
                        try:
                            bpy.ops.object.mode_set(ctx)
                            print('succeeded')
                            stop = True
                        except RuntimeError:
                            print('failed')
    location = "C:\\users\\Frieder\\desktop\\test.fbx"
    bpy.ops.export_scene.fbx(ctx, filepath=location)


def demo():
    main_window = QApplication.instance().blender_widget
    dlg = HelloWorldDialog(main_window)
    dlg.show()


if __name__ == '__main__':
    demo()
