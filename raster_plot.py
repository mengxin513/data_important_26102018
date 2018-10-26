
import numpy as np
import matplotlib.pyplot as plt
import h5py
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages

if __name__ == "__main__":

    with PdfPages("raster_snake.pdf") as pdf:

        print ("Loading data...")

        df = h5py.File("raster.hdf5", mode = "r")
        for i in range(len(df)):
            group = df["raster%03d" % i]
            subgroup = group["snake_raster000"]
            n = len(subgroup)
            data = np.zeros([n, 6])
            for i in range(n):
                dset = subgroup["data%03d" % i]
                data[i, 0:3] = dset["cam_position"]
                data[i, 3:6] = dset["stage_position"]

            matplotlib.rcParams.update({'font.size': 12})

            microns_per_pixel = 2.16

            t = data[:, 0]
            cam_x = data[:, 1] * microns_per_pixel
            cam_x -= np.mean(cam_x)
            cam_y = data[:, 2] * microns_per_pixel
            cam_y -= np.mean(cam_y)
            stage_x = data[:, 3] * 0.012
            stage_x -= np.mean(stage_x)
            stage_y = data[:, 5] * 0.0088
            stage_y -= np.mean(stage_y)

            fig, ax = plt.subplots(1, 1)
            ax.plot(cam_x, cam_y, "+")
            ax.set_aspect(1)
            xmin, xmax = ax.get_xlim()
            ymin, ymax = ax.get_ylim()
            r = max(xmax - xmin, ymax - ymin)
            ax.set_xlim((xmax + xmin)/2 - r/2, (xmax + xmin)/2 + r/2)
            ax.set_ylim((ymax + ymin)/2 - r/2, (ymax + ymin)/2 + r/2)
            ax.set_xlabel('Camera X Position [$\mathrm{\mu m}$]')
            ax.set_ylabel('Camera Y Position [$\mathrm{\mu m}$]')
            fig.suptitle(group.name[1:])

            plt.tight_layout()

            pdf.savefig(fig)
            plt.close(fig)

            fig, ax = plt.subplots(1, 1)
            ax.plot(stage_x, cam_x, "+")
            ax.set_aspect(1)
            xmin, xmax = ax.get_xlim()
            ymin, ymax = ax.get_ylim()
            r = max(xmax - xmin, ymax - ymin)
            ax.set_xlim((xmax + xmin)/2 - r/2, (xmax + xmin)/2 + r/2)
            ax.set_ylim((ymax + ymin)/2 - r/2, (ymax + ymin)/2 + r/2)
            ax.set_xlabel('Stage X Position [$\mathrm{\mu m}$]')
            ax.set_ylabel('Camera X Position [$\mathrm{\mu m}$]')
            fig.suptitle(group.name[1:])

            plt.tight_layout()

            pdf.savefig(fig)
            plt.close(fig)

            fig, ax = plt.subplots(1, 1)
            ax.plot(stage_y, cam_y, "+")
            ax.set_aspect(1)
            xmin, xmax = ax.get_xlim()
            ymin, ymax = ax.get_ylim()
            r = max(xmax - xmin, ymax - ymin)
            ax.set_xlim((xmax + xmin)/2 - r/2, (xmax + xmin)/2 + r/2)
            ax.set_ylim((ymax + ymin)/2 - r/2, (ymax + ymin)/2 + r/2)
            ax.set_xlabel('Stage Y Position [$\mathrm{\mu m}$]')
            ax.set_ylabel('Camera Y Position [$\mathrm{\mu m}$]')
            fig.suptitle(group.name[1:])

            plt.tight_layout()

            pdf.savefig(fig)
            plt.close(fig)
    df.close()
