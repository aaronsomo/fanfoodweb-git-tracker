# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("../../FanFood/fanfoodweb")
# Your mock repo
mock_repo = git.Repo("../fanfoodweb-git-tracker")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['aaroneight07@gmail.com', 'aaron@fanfoodapp.com', 'ronny@fanfoodapp.com'])
importer.import_repository()
