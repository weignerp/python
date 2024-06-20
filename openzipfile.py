import os
import tarfile

odfslogs_plist = ["d:\\workspace\\clb-eclipse-workspace\\asisteam-bi-data\\src\data\\no-sync\\ares\\ares_vreo_all.tar.gz"]
f = open("d:\\workspace\\clb-eclipse-workspace\\asisteam-bi-data\\src\data\\no-sync\\ares\\filelist.txt", "a")
# f.write("Now the file has more content!")

for odfslogp_obj in odfslogs_plist:   
    tarf = tarfile.open(odfslogp_obj, 'r:gz')
    names = tarf.getnames()    
    i = 1
    curr_folder = None
    for name in names:
        try:
            if i % 5000 == 0: 
                curr_folder = os.path.join('d:/workspace/clb-eclipse-workspace/asisteam-bi-data/src/data/no-sync/ares_export/', str(i).zfill(5))
            l = name.split('/')
            n = l[len(l)-1]
       
            f.write('{0}\t{1}\t{2}\n'.format(i, name, curr_folder))
       
            if not os.path.exists(curr_folder):
                os.makedirs(curr_folder)       
            
            tarf.extract(name, curr_folder) 
            i += 1
            
            if i > 10000:
                print ('\nDone: %d\n' % i) 
        except Exception as e:
            print(f'An exception occurred: {e}')
            # handle the exception accordingly
    tarf.close()         
f.close()
