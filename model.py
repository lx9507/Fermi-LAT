# For P7REP_SOURCE_V15 data, ST version v9r33p0
from make2FGLxml import *
import os
import commands as cmd

srcfile = cmd.getoutput(". ./var_common.gts && echo $file_filtered_gti")
catalog_dir = os.environ.get('HOME') + '/data_Fermi/catalog'

mymodel = srcList(catalog_dir + '/gll_psc_v08.fit',
                  srcfile, 'model.xml')
pathtodiffusefiles = os.environ.get('FERMI_DIR') + '/refdata/fermi/galdiffuse'
mymodel.makeModel(pathtodiffusefiles + '/gll_iem_v05_rev1.fit',
                  'gll_iem_v05_rev1',
                  pathtodiffusefiles + '/iso_source_v05_rev1.txt',
                  'iso_source_v05',
                  extDir=catalog_dir + '/Templates')
