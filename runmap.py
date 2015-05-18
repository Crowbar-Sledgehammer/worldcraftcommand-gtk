#!/usr/bin/env python

import window
import os

class RunmapWindow(window.Window):
    """
        Gui application interface.
    """

    GLADE_FILE = os.path.splitext(__file__)[0] + '.glade'
    WINDOW_NORMAL = 'window_normal'
    WINDOW_EXPERT = 'window_expert'

    ROOT_WINDOW = WINDOW_NORMAL

    def __init__(self):
        super(RunmapWindow, self).__init__()

    class Handler(window.Window.BaseHandler):
        """
            Main Window Event Handler
        """

        def on_normal(self, widget):
            self.parent.window.hide()
            self.parent.change_window(self.parent.WINDOW_NORMAL)

        def on_expert(self, widget):
            self.parent.window.hide()
            self.parent.change_window(self.parent.WINDOW_EXPERT)

        def _resolve_radio(self, name):
            radio = next((
                radio for radio in
                self.parent.builder.get_object(name).get_group()
                if radio.get_active()
            ))
            return radio

        def on_execute_normal(self, widget):
            bsp = self._resolve_radio('normal_bsp').get_label()
            vis = self._resolve_radio('normal_vis').get_label()
            rad = self._resolve_radio('normal_rad').get_label()
            import pdb; pdb.set_trace()


if __name__ == '__main__':
    exit(RunmapWindow().main())
