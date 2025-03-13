from importlib import reload
import json
import logging
import os
import time
from typing import Optional

from PySide2.QtCore import QObject, QProcess, Signal

from pipeline.tools.Standalone.RenderQueueManager.controller import render_job

reload(render_job)


class RenderQueue(QObject):
    on_update_view = Signal()
    on_steam_updated = Signal(str, str)
    on_update_job_status = Signal(str)

    def __init__(self):
        super(RenderQueue, self).__init__()
        base_folder = os.path.dirname(__file__)
        self._json_job_file = os.path.join(base_folder, r"../model/render_queue.json")
        self._jobs = self.read_job_list()
        self._current_job_index = 0
        # process
        self._render_process = QProcess()
        self._render_process.readyReadStandardOutput.connect(self.read_job_stream)
        self._render_process.readyReadStandardError.connect(self.read_job_stream)
        self._render_process.finished.connect(self._on_job_finished)
        # engine
        self._blender_exe = r"C:\Program Files\Blender Foundation\Blender 4.1\blender"

    @property
    def jobs(self):
        """ getter for the list of jobs. Return List[JobRender]"""
        return self._jobs

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
        queue_nb = len(self._jobs)
        job = render_job.RenderJob(job_id, queue_nb, scene_path, out_path, render_config, asset_datas)
        self._jobs.append(job)
        self.update_json_list()

    def update_json_list(self):
        json_formatted_jobs = [job.to_dict() for job in self._jobs]
        with open(self._json_job_file, 'w') as f:
            json.dump(json_formatted_jobs, f)

    def generate_id(self):
        return "{}".format(time.time() * 10)[5:11]

    def refresh_job_list(self):
        self._jobs = self.read_job_list()
        return self._jobs

    def read_job_list(self):
        """
        reading the json file describing all the json jobs and generate all these jobs as a renderJob object from it.
        Used to load all the previous jobs that have been saved

        Returns:
            job_list (list[RenderObject]) : a list of RenderObject stored in the json file
        """
        job_list = []
        try:
            with open(self._json_job_file, "r") as f:
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
        item_to_remove = next((job for job in self._jobs if job.job_id == job_id), None)
        if item_to_remove:
            self._jobs.remove(item_to_remove)
        self._sort_jobs()
        self.update_json_list()
        self.on_update_view.emit()

    def _sort_jobs(self):
        self._jobs.sort(key=lambda job: job.queue_nb)

    def read_job_stream(self):
        output = self._render_process.readAllStandardOutput().data().decode()
        error = self._render_process.readAllStandardError().data().decode()
        self.on_steam_updated.emit(output, error)

    def _on_job_finished(self):
        self.on_update_job_status.emit(render_job.Status.SUCCESS)
        self._current_job_index += 1
        if self._current_job_index < len(self._jobs):
            self.on_steam_updated.emit(f'<span style="color: green;">STARTING NEW JOB : {self._jobs[self._current_job_index].scene_name}</span>', "")
            self.run_job(self._current_job_index)
        else:
            self.on_steam_updated.emit(f'<span style="color: green;">ALL RENDER FINISHED</span>', "")
        # increment index
        # send signal
        # start next job

    def run_job(self, index):
        job = self._jobs[index]
        self._render_process.start(self._blender_exe, ["-b", job.scene_path, "-a"])

    def execute(self):
        self._sort_jobs()
        self.run_job(self._current_job_index)
