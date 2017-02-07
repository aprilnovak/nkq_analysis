from omnibus.scripts.omnibus_run import MultiRun


class ScalingRun(MultiRun):
	inp = "multi-state-1.omn"
	fmt = "ppc{ppc:06d}-np{cores:04d}".format 
	basedir = "."
        

	db_entries = {
        'comm_iters': ('SHIFT','DIAGNOSTICS','sensitivity_comm_iters'),
        'memory':     ('SHIFT','MEMORY','VmHWM'),
        'particles':  ('SHIFT','DIAGNOSTICS','particles_transported'),
        }

	def update(self, db, cores, ppc): 
		db['shift']['np'] = cores * ppc
		

def main():
	with ScalingRun() as run:
		for cores in [1,2,4,8]:
			for ppc in [10, 15]:
				run(cores=cores, ppc=ppc)

main()
