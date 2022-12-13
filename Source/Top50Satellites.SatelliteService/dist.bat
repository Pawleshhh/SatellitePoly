rd /s /q "./dist"
py -m pip install --upgrade build
py -m build
py -m pip install --upgrade pip
py -m pip install --force-reinstall ./dist/satelliteservice-0.0.1-py3-none-any.whl
pause