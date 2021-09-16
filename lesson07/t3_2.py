import os

SRC_FOLDER = 'my_project'
DST_FOLDER = 'templates'

for root, _, _ in os.walk(SRC_FOLDER):
    os.makedirs(os.path.join(DST_FOLDER, os.path.relpath(root, SRC_FOLDER)), exist_ok=True)
