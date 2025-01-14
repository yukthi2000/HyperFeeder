from abc import abstractmethod
import os
from podcastIntroPlugins.abstractPluginDefinitions.abstractIntroPlugin import (
    AbstractIntroPlugin,
)
from dotenv import load_dotenv


class BaseIntroPlugin(AbstractIntroPlugin):
    def __init__(self):
        currentFile = os.path.realpath(__file__)
        currentDirectory = os.path.dirname(currentFile)
        load_dotenv(os.path.join(currentDirectory, ".env.intro"))

    @abstractmethod
    def identify(self) -> str:
        pass

    @abstractmethod
    def writeIntro(self, stories, podcastName, typeOfPodcast) -> str:
        pass

    def writeToDisk(self, introText, fileNameIntro):
        directory = os.path.dirname(fileNameIntro)
        os.makedirs(directory, exist_ok=True)

        # Convert dict to string if necessary
        if isinstance(introText, dict):
            introText = str(introText)

        with open(fileNameIntro, "w", encoding="utf-8") as file:
            file.write(introText)

    def doesOutputFileExist(self, fileNameIntro) -> bool:
        return os.path.isfile(fileNameIntro)
