from pipeline.tools.engine import engine

def save_asset(path):
    return engine.save_asset(path, "blend")

if __name__ == "__main__":
    p = save_asset(r"D:\\Prod/03_WORK_PIPE/01_ASSET_3D\\Save_as\\Pipeline_Test\\Blender\\Deployment_Test\\001\\MandalaPower_007.blend")
    print("p = "+p)