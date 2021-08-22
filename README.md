# Dazzler Electron Template

Electron application built with dazzler.

## Getting started

- Create a venv :`python -m venv venv`.
- Activate: `. venv/bin/activate`.
- Install dependencies: `pip install -r requirements.txt`.
- Install Electron globally to run in dev mode: `npm i -g electron`.
- Start a dev instance: `dazzler electron app.py`.
- Build executable for the current platform: `dazzler electron-build app.py`.
    - Find the executable in `electron/dist/<platform>_unpacked`.
- Change the build target:
    - build with NSIS on Windows: `dazzler electron-build app.pu --target NSIS`
    - build AppImage for Linux: `dazzler electron-build app.py --target AppImage`    

## Customizing the application

### Configuration

Rename application for packaging in `dazzler.toml`:

```toml
[electron.metadata]
app_name = "AppName"
```

### Code

Rename window title in `main.py`:

```python
...
page = Page(
    title='Window title',
    ...
)
```

Change layout, window settings, etc...
