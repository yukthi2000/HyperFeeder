import unittest
import os
from podcastTextGenerator import PodcastTextGenerator


class EndToEndTests(unittest.TestCase):
    def test_appRun(self):
        # Override Environment Variables For Testing
        os.environ["PODCAST_NAME"] = "Test Podcast"
        os.environ["PODCAST_TYPE"] = "Test Podcast Type"
        os.environ["PODCAST_DATA_SOURCE_PLUGINS"] = "testerDataSourcePlugin"
        os.environ["PODCAST_INTRO_PLUGINS"] = "testerIntroPlugin"
        os.environ["PODCAST_SCRAPER_PLUGINS"] = "testerScraperPlugin"
        os.environ["PODCAST_SUMMARY_PLUGINS"] = "testerSummaryPlugin"
        os.environ["PODCAST_SEGMENT_WRITER_PLUGINS"] = "testerSegmentWriter"
        os.environ["PODCAST_OUTRO_PLUGINS"] = "testerOutroPlugin"
        os.environ["PODCAST_PRODUCER_PLUGINS"] = "producerPlugin"
        os.environ["SHOULD_PAUSE_AND_VALIDATE_STORIES_BEFORE_SCRAPING"] = "false"

        # Clear Previous Test Artifacts
        if os.path.exists("output/test-podcast"):
            os.system("rm -rf output/test-podcast")

        # Run App
        PodcastTextGenerator().run("test-podcast")
