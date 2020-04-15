# Python PyQt
PyQt Projcts examples

```shell
rm -rf ~/Workspace/python_qt/env
File -> Open projects from File System (python_qt folder) -> Finish
```

```shell
# Create a virtualenv
cd ~/Workspace/python_qt
python3 -m venv env
Open .py file -> Project -> Properties -> Windows -> Preference -> Browse for python
```

```shell
source ~/Workspace/python_qt/env/bin/activate
```

```shell
# Libraries
pip3 install pyqt5==5.13.2
```

```shell
# Compile GUI
./gui/design/compileGUI.sh
# Run GUI
python main_ui.py
```