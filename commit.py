from git import Repo
from tqdm import tqdm

repo = Repo('./')
headcommit = repo.head.commit

for i in tqdm(range(0, 10)):
    repo.index.commit("#"+str(i)+" 🎉", author_date=headcommit.authored_date, commit_date=headcommit.committed_date)

# origin = repo.remote('origin')
# origin.push()