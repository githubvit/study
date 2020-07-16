# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis([
            'main.py',
            'D:\\pyj\\st\\study\\pyside2_pyqt\\pys2\\login_register_calculate_case\\view\\calculate_btn_class.py',
            'D:\\pyj\\st\\study\\pyside2_pyqt\\pys2\\login_register_calculate_case\\view\\login_register_calculate_case_rc.py',
            'D:\\pyj\\st\\study\\pyside2_pyqt\\pys2\\login_register_calculate_case\\view\\Ui_calculate.py',
            'D:\\pyj\\st\\study\\pyside2_pyqt\\pys2\\login_register_calculate_case\\view\\Ui_login.py',
            'D:\\pyj\\st\\study\\pyside2_pyqt\\pys2\\login_register_calculate_case\\view\\Ui_register.py',
            'D:\\pyj\\st\\study\\pyside2_pyqt\\pys2\\login_register_calculate_case\\view\\view_calculate.py',
            'D:\\pyj\\st\\study\\pyside2_pyqt\\pys2\\login_register_calculate_case\\view\\view_login.py',
            'D:\\pyj\\st\\study\\pyside2_pyqt\\pys2\\login_register_calculate_case\\view\\view_register.py', 
            ],
             pathex=['D:\\pyj\\st\\study\\pyside2_pyqt\\pys2\\login_register_calculate_case'],
             binaries=[],
             datas=[('D:\\pyj\\st\\study\\pyside2_pyqt\\pys2\\login_register_calculate_case\\view\\calculate_btn.css','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
