import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(2);n=120
# build a fake 3D backbone with two compact domains
xyz=np.cumsum(rng.normal(0,1,(n,3)),axis=0)
xyz[:60]*=0.3;xyz[60:]=xyz[60:]*0.3+8  # two clusters
d=np.sqrt(((xyz[:,None]-xyz[None])**2).sum(-1))
cm=(d<8).astype(float)
plt.figure(figsize=(6,6));plt.imshow(cm,cmap="Greys",origin="lower")
plt.xlabel("residue");plt.ylabel("residue");plt.title("Contact map (demo data)")
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"contacts: {int(cm.sum())}\n");print("ok")