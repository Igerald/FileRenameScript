import os, sys, time

t0 = time.clock()
determinant = 0
pfp = primaryfilepath = "D://INDUSTRIAL ENGINEERING COURSES" if determinant == 0 else "D://PYTHONTESTFOLDER"
os.chdir(pfp)

fil = filelist = [pfp+'//'+fn for fn in os.listdir()]
cfn = corruptfilenames = []
counts = 0

SYM = '#~*&_–'

def filesearchfunction(fl):
     global cfn,SYM,counts
     while len(fl)>0:
          for temppath in fl:
               counts += 1
               try:
                    os.chdir(temppath)
                    countlist = os.listdir()
                    filerenamelist = [cfnss for cfnss in countlist if any([(sym in cfnss) for sym in SYM])]
                    filerenamelist2 = [cfnsss for cfnsss in countlist if (cfnsss.count('.')>1)]
                    cfn = cfn + [(cfns,temppath) for cfns in countlist if (cfns.count('.')>1) or any([(sym in cfns) for sym in SYM])]
                    fl = fl + [temppath+'//'+fls.translate(str.maketrans(SYM,'      ')) for fls in countlist if '.' not in fls]
                    for filnam in filerenamelist:
                         try:
                              os.rename(filnam,filnam.translate(str.maketrans(SYM,'      ')))
                         except FileExistsError:
                              os.rename(filnam,"TWO "+filnam.translate(str.maketrans(SYM,'      ')))
                    for filnam2 in filerenamelist2:
                         try:
                              filnam2 = filnam2.translate(str.maketrans(SYM,'     '))
                              os.rename(filnam2,''.join(filnam2.split('.')[:-1]+['.'+filnam2.split('.')[-1]]))
                         except FileExistsError:
                              filnam2 = "THREE "+filnam2.translate(str.maketrans(SYM,'     '))
                              os.rename(filnam2,''.join(filnam2.split('.')[:-1]+['.'+filnam2.split('.')[-1]]))
                    fl.remove(temppath)
               except NotADirectoryError:
                    fl.remove(temppath)
     return cfn


fsf = filesearchfunction(fil)
print(time.clock()-t0)

STATS = ["Time to complete = 28 seconds",
         "Number of Files = 11,015",
         "Number of Folders = 1,543",
         "Number of Files Renamed = 2503"]
