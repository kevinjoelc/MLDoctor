import os
import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer:
    def __init__(self, df):
        self.df = df
        os.makedirs("report_assets", exist_ok=True)

    def correlation_heatmap(self):
        plt.figure(figsize=(14, 10))

        sns.heatmap(
            self.df.select_dtypes(include="number").corr(),
            annot=True,
            cmap="coolwarm",
            linewidths=0.5,
            square=True
        )

        plt.title("Correlation Heatmap", fontsize=16)
        plt.tight_layout()
        plt.savefig("report_assets/correlation.png", dpi=250)
        plt.close()

    def missing_chart(self):
        missing = self.df.isnull().sum()

        plt.figure(figsize=(10, 6))

        missing.plot(kind="bar")

        plt.title("Missing Values", fontsize=16)
        plt.ylabel("Count")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.savefig("report_assets/missing.png", dpi=250)
        plt.close()

    def histograms(self):
        numeric = self.df.select_dtypes(include="number")

        numeric.hist(
            figsize=(18, 14),
            bins=20
        )

        plt.tight_layout()
        plt.savefig("report_assets/histograms.png", dpi=250)
        plt.close()

    def boxplots(self):
        numeric = self.df.select_dtypes(include="number")

        plt.figure(figsize=(18, 10))

        numeric.boxplot(rot=45)

        plt.title("Boxplots", fontsize=16)

        plt.tight_layout()
        plt.savefig("report_assets/boxplots.png", dpi=250)
        plt.close()

    def generate(self):
        self.correlation_heatmap()
        self.missing_chart()
        self.histograms()
        self.boxplots()