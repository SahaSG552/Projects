TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, *args):
        obj = None
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
        else:
            obj = super().__new__(DialogLinux)
        obj.name = args[0]
        return obj


dlg_win = Dialog("pupupup")
print(type(dlg_win), dlg_win.name_class, dlg_win.name)
TYPE_OS = 2
dlg_lin = Dialog("ohohoho")
print(type(dlg_lin), dlg_lin.name_class, dlg_lin.name)
