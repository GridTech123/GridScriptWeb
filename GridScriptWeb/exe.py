import cx_Freeze

executables = [cx_Freeze.Executable('GridScriptWeb.py')]

cx_Freeze.setup(name = 'GridScriptWeb', version = '1.0.0', options = {'build_exe': {'packages':['sys', 'time', 'pickle']}}, executables = executables)
