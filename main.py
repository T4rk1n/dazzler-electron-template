from dazzler.system import Page
from dazzler.components.core import Container, Text
from dazzler.electron import ElectronWindowSettings

layout = Container([
    Text('Main window')
])

page = Page(
    __name__,
    layout,
    electron_window=ElectronWindowSettings(
        width=1280,
        height=1024,
    )
)
