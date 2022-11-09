from urllib import request
from project import Project
import toml



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        parsed_cont = toml.loads(content)


        depend = []
        for i in parsed_cont["tool"]["poetry"]["dependencies"]:
            depend.append(i)

        devdepend = []
        for i in parsed_cont["tool"]["poetry"]["dev-dependencies"]:
            devdepend.append(i)



        #print(parsed_cont)
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(parsed_cont["tool"]["poetry"]["name"], parsed_cont["tool"]["poetry"]["description"], depend, devdepend)
