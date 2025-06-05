import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def selection_per_product_group(df, product_segment):
    return df[(df["price"] > product_segment[0]) & (df["price"] <= product_segment[1])].copy()


def distribution_price_group(df, show=True):
    fig, ax = plt.subplots()
    counts, bins, _ = ax.hist(df["price"], bins=10)

    for count, left, right in zip(counts, bins[:-1], bins[1:]):
        center = (left + right) / 2
        label = f"Intervall: {int(left)}–{int(right)} SEK, {int(count)} st"
        ax.text(center, count + max(counts)*0.02, label, ha="left", fontsize=8, rotation=45)

    ax.set_title("Fördelning av prisintervall")
    ax.set_xlabel("Pris (SEK)")
    ax.set_ylabel("Antal")

    if show:
        plt.show()
    else:
        return fig

def selection_quality(df, cut, color, clarity):
    return df[df["cut"].isin(cut) & df["color"].isin(color) & df["clarity"].isin(clarity)]


def distribution_carat(df, show=True):
    counts, bins, _ = plt.hist(df["carat"], bins=10)

    for count, left, right in zip(counts, bins[:-1], bins[1:]):
        center = (left + right) / 2
        label = f"{int(count)} st"
        plt.text(center, count + 100, label, ha="center", fontsize=8)

    plt.title("distrubition karat")
    plt.xlabel("karat")
    plt.ylabel("antal")

    if show:
        plt.show()
    else:
        return


def quality_point_barchart_carat_and_price_avgs(df, show=True):

    df = df.copy()
    df["quality_score"] = df.apply(quality_point_calculator, axis=1)
    grouped_by_scores = df.groupby("quality_score")

    count_per_score = grouped_by_scores.size()
    avg_price_per_carat = grouped_by_scores.apply(lambda g: (g["price"] / g["carat"]).mean())
    avg_price = grouped_by_scores["price"].mean()

    avg_carat = grouped_by_scores["carat"].mean()
    norm = plt.Normalize(avg_carat.min(), avg_carat.max())
    cmap = plt.cm.viridis
    colors = cmap(norm(avg_carat.values))

    fig, ax1 = plt.subplots()

    ax1.bar(count_per_score.index, count_per_score.values, color=colors, label="antal")
    ax1.set_xlabel("Kvalitetspoäng(lägre poäng, bättre kvalitet)")
    ax1.set_ylabel("antal", color="skyblue")
    ax1.tick_params(axis='y', labelcolor='skyblue')
    ax1.invert_xaxis()

    ax2 = ax1.twinx()
    ax2.plot(avg_price_per_carat.index, avg_price_per_carat.values, color="darkred", marker='o', label="genomsnitt pris per karat")
    ax2.plot(avg_price.index, avg_price.values, color="green", marker="s", label="genomsnitt pris")
    ax2.set_ylabel("pris", color="black")
    ax2.tick_params(axis='y', labelcolor='black')

    patches = [
        mpatches.Patch(color=color, label=f"{score}: {carat:.2f} ct")
        for score, color, carat in zip(avg_carat.index, colors, avg_carat.values)
    ]
    legend = ax1.legend(handles=patches, title="Genomsnittlig karat", loc="upper left", bbox_to_anchor=(1.25, 1))

    line_handles, line_labels = ax2.get_legend_handles_labels()
    ax2.legend(line_handles, line_labels, loc="upper right")

    plt.title(f"genomsnitt per kvalitetsgrad")
    fig.tight_layout()

    if show:
        plt.show()
    else:
        return fig


def quality_point_calculator(row):
    cut_score = {"Ideal": 0, "Premium": 1, "Very Good": 2, "Good": 3, "Fair": 4}
    color_score = {"D": 0, "E": 1, "F": 2, "G": 3, "H": 4, "I": 5, "J": 6}
    clarity_score = {"IF": 0, "VVS1": 1, "VVS2": 2, "VS1": 3, "VS2": 4, "SI1": 5, "SI2": 6, "I1": 7}

    return cut_score.get(row["cut"]) + color_score.get(row["color"]) + clarity_score.get(row["clarity"])


def quality_piecharts(df, show=True):

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    axes[0].pie(df["cut"].value_counts(), labels=df["cut"].value_counts().index, autopct='%1.1f%%', startangle=140)
    axes[0].set_title("Fördelning av slipningsgrad")

    axes[1].pie(df["color"].value_counts(), labels=df["color"].value_counts().index, autopct='%1.1f%%', startangle=140)
    axes[1].set_title("Fördelning av färgkvalitet")

    axes[2].pie(df["clarity"].value_counts(), labels=df["clarity"].value_counts().index, autopct='%1.1f%%', startangle=140)
    axes[2].set_title("Fördelning av klarhet")

    if show:
        plt.show()
    else:
        return fig

def carat_price_interval(df, show=True):

    df = df.copy()

    carat_bins = [0, 0.5, 1.0, 1.5, 2.0, 2.5, df["carat"].max()]
    carat_labels = ["<0.5 ct", "0.5-1.0 ct", "1.0-1.5 ct", "1.5-2.0 ct", "2.0-2.5", ">2.5 ct"]
    df["carat_group"] = pd.cut(df["carat"], bins=carat_bins, labels=carat_labels)

    price_bins = np.histogram_bin_edges(df["price"], bins=10) # 10 bins to keep it readable
    df["price_bin"] = pd.cut(df["price"], bins=price_bins)

    pivot = df.pivot_table(index="price_bin", columns="carat_group", values="carat", aggfunc="count", observed=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    bottom = np.zeros(len(pivot))
    colors = plt.cm.viridis(np.linspace(0, 1, len(pivot.columns)))

    for carat_label, color in zip(pivot.columns, colors):
        values = pivot[carat_label].values
        ax.bar(pivot.index.astype(str), values, label=str(carat_label), bottom=bottom, color=color)
        bottom += values

    ax.set_title("karatgrupp per prisintervall")
    ax.set_xlabel("prisintervall")
    ax.set_ylabel("totalt antal")
    ax.legend(title="karatgrupp")
    plt.setp(ax.get_xticklabels(), rotation=45)

    if show:
        plt.show()
    else:
        return fig