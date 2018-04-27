from biclustering.functions import SSVD_python
from biclustering.functions import plotClusters

u_tilde = np.r_[np.arange(3,11)[::-1], 2*np.ones(17), np.zeros(75)].reshape((-1,1))
u = u_tilde/np.linalg.norm(u_tilde)
v_tilde = np.r_[np.array([10,-10,8,-8,5,-5]),3*np.ones(5),-3*np.ones(5),np.zeros(34)].reshape((-1,1))
v = v_tilde/np.linalg.norm(v_tilde)
s = 50

X_star = s*u@v.T
n, d = X_star.shape
np.random.seed(2018)
X_sim = X_star + np.random.randn(n,d)

u, s, v, niter = SSVD_python(X_sim)

groups = np.concatenate((np.ones(11-3), np.ones(17)*2, np.ones(75)*3))
plotClusters(u, s, v, groups, 0)
