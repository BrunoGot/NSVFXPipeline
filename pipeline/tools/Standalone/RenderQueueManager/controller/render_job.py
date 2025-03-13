import os
from typing import Optional

class RenderJob():
    def __init__(self, job_id: str, queue_number: int, scene_path: str, out_path: str,
                 render_config: Optional[dict] = None,
                 asset_datas: Optional[dict] = None):
        """
        Object that is encapsulate a scene and will be processed for rendering.
        Here are the different datas that it's handeling
        Args:
            job_id (str): A unique ID for the job
            queue_number (int): used to define the order of the job in a queue. Must be unique number
            scene_path (str): path of the scene to render
            out_path (str): output path of the job to write in
            render_config (dict[str, object]): Dictionary containing parameters about the render itself.
            Can be used for overriding:
                - "pixel_size" (tuple[int,int]): size X and Y of the frame to render in pixel
                - "frame_sequence" (tuple[int,int,int]): first frame, last frame and frame step to render
                - "file_format" (str): output file formet, "png","jpg","mov"
            asset_datas (dict[str,str]): Dictionary containing information about the asset.
            The keys values is depending of the Config file the user is setting up.
                - Key (str): Asset node like "Project", "Asset_name", "Task", "Subtask", "Version"
                - Value (str): Node Value like "test_project, "test_asset", "anim", "blocking", "001"
        """

        if asset_datas is None:
            asset_datas = {}
        self.__job_id = job_id
        self.__queue_number = queue_number
        self.__scene_path = scene_path
        self.__out_path = out_path
        self.__render_config = render_config
        self.__asset_datas = asset_datas

    @property
    def job_id(self):
        return self.__job_id

    @property
    def queue_nb(self):
        return self.__queue_number

    @property
    def scene_path(self):
        return self.__scene_path

    @property
    def out_path(self):
        return self.__out_path

    @property
    def render_config(self):
        return self.__render_config

    @property
    def asset_datas(self):
        return self.__asset_datas

    @property
    def scene_name(self):
        return os.path.basename(self.__scene_path)

    def to_dict(self):
        """Serialize the Job to be recorded in a JSON"""
        return {"job_id": self.__job_id, "queue_number": self.__queue_number, "scene_path": self.__scene_path,
                "out_path": self.__out_path, "render_config": self.__render_config, "asset_datas": self.__asset_datas}

    @classmethod
    def from_dic(cls, datas: dict):
        """
        deserialize the class and return an instance from the input datas. Use to instance an object from a json file
        Args:
            - datas(dict[str, object]): dictionary containing the job datas to instantiate it :
                - "job_id" (str): A unique ID for the job
                - "queue_number" (int): used to define the order of the job in a queue. Must be unique number
                - "scene_path" (str): path of the scene to render
                - "out_path" (str): output path of the job to write in
                - "render_config" (dict[str, object]) : refer to RenderJob constructor docstring
                - "asset_datas" (dict[str, str]) : refer to RenderJob constructor docstring

        returns:
            RenderJob: a brand new RenderJob ready to go :)
        """
        return cls(datas["job_id"], datas["queue_number"], datas["scene_path"], datas["out_path"],
                   datas["render_config"], datas["asset_datas"])
