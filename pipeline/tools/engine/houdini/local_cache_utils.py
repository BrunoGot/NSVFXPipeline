import shutil
from pathlib import Path
import sys

import hou


def publish_local_cache():
    """called from the publish button of a localCache HDA. must be called by a node"""
    cache_node = hou.pwd()
    src_cache = Path(cache_node.parm("basedir").eval(), cache_node.parm("basename").eval())
    dest_cache = Path(cache_node.parm("publishPath").eval(), cache_node.parm("basename").eval())
    is_optimize_on = cache_node.parm("optimizeMode").eval()
    if is_optimize_on:
        shutil.move(src_cache,dest_cache)
    else:
        shutil.copy(src_cache,dest_cache)

