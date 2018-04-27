from biclustering.functions import SSVD_python
from biclustering.functions import plotClusters
import pandas as pd

OutData = pd.read_csv('data/BreastCancerData.txt', sep=' ', header=0)
X_Out = np.array(OutData.T)
u, s, v, niter = SSVD_python(X_Out)
groups = pd.read_csv('data/BreastCancerLabels.txt', sep=' ', header = -1)
groups = np.delete(np.array(groups)[0],9)
plotClusters(u, s, v, groups, 0)
