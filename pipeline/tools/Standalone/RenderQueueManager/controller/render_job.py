from enum import Enum
import os
from typing import Optional


class Status(Enum):
    """
    Enum used to describe the status of a job

    Attributes:
        READY (int): The job didn't stated yet but is ready to process
        RUNNING (int): The job is currently rendering frames
        PAUSED (int): The job has stated but have been stopped
        SUCCESS (int): The job has started and finished successfully. you can archive it
        FAILED (int): The job stated but an error happened. The job didn't finished successfully.
    """
    READY = 1
    RUNNING = 2
    PAUSED = 3
    SUCCESS = 4
    FAILED = 5

    @classmethod
    def _missing_(cls, value):
        # Return the default value if the value doesn't match any member
        return cls.READY


class RenderJob():
    def __init__(self, job_id: str, queue_number: int, scene_path: str, out_path: str,
                 status: Optional[Status] = Status.READY,
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
            status (Status): Curent status of the job, see Status class for the different value
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
        self._job_id = job_id
        self._queue_number = queue_number
        self._scene_path = scene_path
        self._out_path = out_path
        self._status = status
        self._render_config = render_config
        self._asset_datas = asset_datas

    @property
    def job_id(self):
        return self._job_id

    @property
    def queue_nb(self):
        return self._queue_number

    @property
    def scene_path(self):
        return self._scene_path

    @property
    def out_path(self):
        return self._out_path

    @property
    def status(self):
        return self._status

    @property
    def render_config(self):
        return self._render_config

    @property
    def asset_datas(self):
        return self._asset_datas

    @property
    def scene_name(self):
        return os.path.basename(self._scene_path)

    def to_dict(self):
        """Serialize the Job to be recorded in a JSON"""
        return {"job_id": self._job_id, "queue_number": self._queue_number, "scene_path": self._scene_path,
                "out_path": self._out_path, "status": self._status, "render_config": self._render_config,
                "asset_datas": self._asset_datas}

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
        parsed_status = datas.get("render_config", "READY")
        # smelly but got no time. problem is when the json is corrupet and status exist but is "null"
        if not parsed_status:
            parsed_status = "READY"
        return cls(datas.get("job_id"), datas.get("queue_number"), datas.get("scene_path"), datas.get("out_path"),
                   Status[parsed_status], datas.get("render_config"), datas.get("asset_datas"))
