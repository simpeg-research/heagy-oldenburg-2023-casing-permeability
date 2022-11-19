import numpy as np
import matplotlib.pyplot as plt


def plot_pos_neg_log(x, y, ax, plot_type="semilogy", color=None, label=None):
    if plot_type == "plot":
        return ax.plot(x, y, color=color, label=label)
    else:
        inds_pos = (y > 0)
        inds_neg = (y < 0)
        getattr(ax, plot_type)(x[inds_pos], y[inds_pos], color=color, label=label) 
        return getattr(ax, plot_type)(x[inds_pos], y[inds_pos], "--", color=color)

    
def get_casing_inds(mesh, casing_a, casing_b, casing_l):
    inds_casing_x = (
        (mesh.cell_centers[:, 0] > casing_a) & 
        (mesh.cell_centers[:, 0] < casing_b)
    )
    inds_casing_z = (
        (mesh.cell_centers[:, 2] < 0) &
        (mesh.cell_centers[:, 2] > -casing_l)
    )
    inds_casing = inds_casing_x & inds_casing_z
    return inds_casing


def load_fields(filepath, sim, conductivity, permeability):
    solution = np.load(f"{filepath}.npy")
    sim.model = conductivity
    sim.mu = permeability
    f = sim.fieldsPair(sim)
    f[:, sim._fieldType + "Solution", :] = solution
    return f

