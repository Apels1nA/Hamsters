#!./env/bin/python3
import os
import bjoern

from app import app


pid = os.getpid()
print('[Run] Bjeorn on pid '+str(pid))
bjoern.run(app, '127.0.0.1', 8000, reuse_port=True)
