import os

project_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

assets_dir = os.path.join(project_root_dir, 'assets')
fragments_dir = os.path.join(assets_dir, 'fragments')
templates_dir = os.path.join(assets_dir, 'templates')

build_dir = os.path.join(project_root_dir, 'build')
