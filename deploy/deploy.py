from git import Repo

git_url = 'https://github.com/fabianopetroni/assetManager.git'

mayaApps = 'D:/server/apps/maya/'

app = 'assetManager'

app_dir = '{0}{1}'.format(mayaApps, app)

release = 'major'

if not os.path.isdir(app_dir):
    os.makedirs(app_dir)
    
listDir = os.listdir(app_dir)

listDir.sort()
newRelease = None

deploy_dir = None
if not listDir:
    if release == 'patch':
        deploy_dir = '{0}/{1}-0.0.1'.format(app_dir, app)
    elif release == 'minor':
        deploy_dir = '{0}/{1}-0.1.0'.format(app_dir, app)
    elif release == 'major':
        deploy_dir = '{0}/{1}-1.0.0'.format(app_dir, app)
else:
    latestRelease = listDir[-1]
    versionList = latestRelease.split('-')[-1].split('.')

    if release == 'patch':
        next = str(int(versionList[-1]) + 1)
        versionList[-1] = nextPatch
    
    elif release == 'minor':
        next = str(int(versionList[-2]) + 1)
        versionList[-1] = '0'
        versionList[-2] = nextPatch
        
    elif release == 'major':
        next = str(int(versionList[-3]) + 1)
        versionList[-1] = '0'
        versionList[-2] = '0'
        versionList[-3] = nextPatch
    
    newRelease = app + '-{0}.{1}.{2}'.format(versionList[0], versionList[1], versionList[2])
        
    deploy_dir = '{0}/{1}'.format(app_dir, newRelease)

Repo.clone_from(git_url, deploy_dir)