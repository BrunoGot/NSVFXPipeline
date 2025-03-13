from importlib import reload
import json
import logging
import os
import time
from typing import Optional

from PySide2.QtCore import QObject, Signal

from pipeline.tools.Standalone.RenderQueueManager.controller import render_job

reload(render_job)


class RenderQueue(QObject):
    on_update_view = Signal()

    def __init__(self):
        super(RenderQueue, self).__init__()
        base_folder = os.path.dirname(__file__)
        self.__json_job_file = os.path.join(base_folder, r"../model/render_queue.json")
        self.__jobs = self.read_job_list()

    @property
    def jobs(self):
        """ getter for the list of jobs. Return List[JobRender]"""
        return self.__jobs

    def register_job(self, scene_path: str, out_path: str,
                     render_config: Optional[dict] = None,
                     asset_datas: Optional[dict] = None):
        """
        Create a JobRender Object and add it in the json file as a job to render
        Args:
            scene_path (str): the scene file to render
            out_path (str): the output path to render on
            render_config (dict[str,object]): the configuration of the render to process.
                See more info in the RenderObject about render_config
            asset_datas (dict[str,str]): the informations about the asset itself,
                see more info in the renderObject class about it
        """

        job_id = self.generate_id()
        queue_nb = len(self.__jobs)
        job = render_job.RenderJob(job_id, queue_nb, scene_path, out_path, render_config, asset_datas)
        self.__jobs.append(job)
        self.update_json_list()

    def update_json_list(self):
        json_formatted_jobs = [job.to_dict() for job in self.__jobs]
        with open(self.__json_job_file, 'w') as f:
            json.dump(json_formatted_jobs, f)

    def generate_id(self):
        return "{}".format(time.time() * 10)[5:11]

    def refresh_job_list(self):
        self.__jobs = self.read_job_list()
        return self.__jobs

    def read_job_list(self):
        """
        reading the json file describing all the json jobs and generate all these jobs as a renderJob object from it.
        Used to load all the previous jobs that have been saved

        Returns:
            job_list (list[RenderObject]) : a list of RenderObject stored in the json file
        """
        job_list = []
        try:
            with open(self.__json_job_file, "r") as f:
                json_jobs = json.load(f)
            for job_datas in json_jobs:
                job = render_job.RenderJob.from_dic(job_datas)
                job_list.append(job)
        except json.decoder.JSONDecodeError as e:
            logging.warning("json file haven't been loaded correctly. Maybe empty or corrumpted.\n"
                            f"error : {e}")
        return job_list

    def remove_job(self, job_id):
        print(f"remove job : {job_id}")
        # using next avoid to iterate over all the list
        item_to_remove = next((job for job in self.__jobs if job.job_id == job_id), None)
        if item_to_remove:
            self.__jobs.remove(item_to_remove)
        self.__jobs.sort(key=lambda job:job.queue_nb)
        self.update_json_list()
        self.on_update_view.emit()

    def execute(self):
        pass
