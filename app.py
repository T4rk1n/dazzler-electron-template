from dazzler import Dazzler
from dazzler.electron import is_compiled
import main

app = Dazzler(__name__)
app.add_page(main.page)


if __name__ == '__main__':
    if is_compiled():
        app.start()
    else:
        app.start('--reload -v')
