import unittest
from pipeline.pipeline_config import Config

class TestPipelineConfig(unittest.TestCase):

    def test_default_project_directory_is_correct(self):
        """test that the project directory is correctly set to D:/Prod/03_WORK_PIPE/01_ASSET_3D"""
        conf = Config("default")
        self.assertEqual(conf.project_directory.pattern,"D:/Prod/03_WORK_PIPE/01_ASSET_3D")


