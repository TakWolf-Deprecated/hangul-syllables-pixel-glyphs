import os

project_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

assets_dir = os.path.join(project_root_dir, 'assets')
jamos_dir = os.path.join(assets_dir, 'jamos')

build_dir = os.path.join(project_root_dir, 'build')
tmp_dir = os.path.join(build_dir, 'tmp')
jamos_tmp_dir = os.path.join(tmp_dir, 'jamos')
glyphs_dir = os.path.join(build_dir, 'glyphs')
