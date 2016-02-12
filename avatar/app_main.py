import wpf

from System.Windows import Window

class app_main(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'app_main.xaml')
