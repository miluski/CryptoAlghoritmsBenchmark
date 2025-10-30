import matplotlib.pyplot as plt

class Plotter:
    def plot_results(self, suite_name, results, sizes):
        fig, axs = plt.subplots(2, 3, figsize=(24, 12))
        fig.suptitle(f"{suite_name} Algorithm Benchmark", fontsize=16)
        operations = ['encrypt', 'decrypt']
        metrics = [("time", "Time", "Time (s)"), ("cpu", "CPU Usage", "CPU (%)"), ("mem", "RAM Usage", "RAM (MB)")]
        markers = ['o', 's', '^', 'D', 'v', '*', 'p', 'h']
        for i, op in enumerate(operations):
            for j, (metric, title, ylabel) in enumerate(metrics):
                ax = axs[i, j]
                for idx, (alg, data) in enumerate(results.items()):
                    marker = markers[idx % len(markers)]
                    ax.plot(sizes, data[f"{op}_{metric}"], marker=marker, label=alg)
                ax.set_title(f"{op.capitalize()} {title}")
                ax.set_xlabel("Data Size [chars]")
                ax.set_ylabel(ylabel)
                ax.legend()
                ax.grid(True, which="both", ls="--")
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.savefig(f"results/benchmark_{suite_name.lower().replace(' ', '_')}.png")
        plt.show()
