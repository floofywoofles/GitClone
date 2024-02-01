from src.git import Git

git: Git = Git()

git.add(".")
git.commit()