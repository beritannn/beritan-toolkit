import os
import importlib

def load_plugins():
    plugins = []
    for f in os.listdir("modules"):
        if f.endswith(".py"):
            name = f[:-3]
            plugins.append(importlib.import_module("modules."+name))
    return plugins
