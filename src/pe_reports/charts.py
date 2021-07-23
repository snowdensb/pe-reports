"""Generate Matplotlib charts for reports."""
# Third-Party Libraries
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


class barCharts:
    """Simple class methods to create bar charts."""

    # matplotlib
    def simple_bar(
        df,
        title,
        x_label,
        y_label,
        width,
        height,
        name,
        totalDataPts,
        rotate_axis=True,
        grid=True,
    ):
        """Define bar chart attributes."""
        plt.rcParams.update({"figure.max_open_warning": 0})
        catName = df.columns[0]
        Val_1Name = df.columns[1]
        Category_column = df[catName]
        Value_column = df[df.columns[1]]
        fig, ax = plt.subplots()
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        plt.bar(Category_column, Value_column, zorder=3, color="#466fc6", width=0.4)
        plt.title(title, pad=15, fontsize=10)
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.gca().set_xlim(-1.0, len(Category_column))

        if totalDataPts == 0:
            ax.axes.set_yticks(range(len(Category_column)))
            ax.axes.set_yticklabels(range(len(Category_column)))

        if rotate_axis:
            if len(Category_column) >= 10:
                plt.xticks(rotation=30, ha="right")
            else:
                plt.xticks(rotation=15, ha="right")

        # set the labels above
        for i in range(len(df)):

            if df.loc[i, Val_1Name] > 0:
                label = df.loc[i, Val_1Name]

                plt.annotate(
                    label,  # this is the text
                    (
                        df.loc[i, catName],
                        df.loc[i, Val_1Name],
                    ),  # this is the point to label
                    textcoords="offset points",  # how to position the text
                    xytext=(0, 3),  # distance from text to points (x,y)
                    ha="center",  # horizontal alignment can be left, right or center
                    fontsize=8,
                )
        plt.xlabel(x_label, labelpad=10, fontdict={"size": 8})
        plt.ylabel(y_label, labelpad=10, fontdict={"size": 8})
        if grid:
            plt.grid(axis="y")
        plt.gcf().set_size_inches(width, height)
        plt.tight_layout()

        # plt.gca().set_ylim([0,df[Val_1Name].max() + df[Val_1Name].max()*.17])
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.savefig(name, transparent=True, dpi=500)
        plt.clf()
        return name

    def stacked_bar(
        df, x_label, y_label, width, height, name, totalDataPts, rotate_axis=True
    ):
        """Define stacked bar graph attributes."""
        plt.rcParams.update({"figure.max_open_warning": 0})
        catName = df.columns[0]
        Val_1Name = df.columns[1]
        Category_column = df[catName]
        Value_column = df[df.columns[1]]
        Value_column2 = df[df.columns[2]]
        Val_2Name = df.columns[2]
        bar_width = 0.4
        fig, ax = plt.subplots()
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.grid(axis="y")
        plt.bar(
            df.index - 0.2,
            Value_column,
            bar_width,
            label=Val_1Name,
            zorder=3,
            color="#466fc6",
        )
        plt.bar(
            df.index + 0.2,
            Value_column2,
            bar_width,
            label=Val_2Name,
            zorder=3,
            color="#e17c40",
        )

        if totalDataPts == 0:
            ax.axes.set_yticks(range(len(Category_column)))
            ax.axes.set_yticklabels(range(len(Category_column)))
        # df.plot(x=catName,kind='bar',stacked=False,)

        plt.xticks(ticks=df.index, labels=Category_column)
        if rotate_axis:
            plt.xticks(rotation=30, ha="right")
        for i in range(len(df)):

            if df.loc[i, Val_1Name] > 0:
                label = int(df.loc[i, Val_1Name])

                plt.annotate(
                    label,  # this is the text
                    (i - 0.2, df.loc[i, Val_1Name]),  # this is the point to label
                    textcoords="offset points",  # how to position the text
                    xytext=(0, 3),  # distance from text to points (x,y)
                    ha="center",  # horizontal alignment can be left, right or center
                    fontsize=8,
                )

            if df.loc[i, Val_2Name] > 0:
                label = int(df.loc[i, Val_2Name])

                plt.annotate(
                    label,  # this is the text
                    (i + 0.2, df.loc[i, Val_2Name]),  # this is the point to label
                    textcoords="offset points",  # how to position the text
                    xytext=(0, 3),  # distance from text to points (x,y)
                    ha="center",  # horizontal alignment can be left, right or center
                    fontsize=8,
                )
        plt.legend(loc=9, ncol=2, framealpha=0, fontsize=8, bbox_to_anchor=(0.5, 1.25))
        plt.xlabel(x_label, labelpad=10, fontdict={"size": 8})
        plt.ylabel(y_label, labelpad=10, fontdict={"size": 8})
        plt.gcf().set_size_inches(width, height)
        plt.tight_layout()
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.savefig(name, transparent=True, dpi=500)
        plt.clf()
        return name

    def h_bar(df, x_label, y_label, width, height, name, totalDataPts):
        """Define H bar chart attributes."""
        plt.rcParams.update({"figure.max_open_warning": 0})
        catName = df.columns[0]
        Val_1Name = df.columns[1]
        Category_column = df[catName].str.replace("Vulnerable Product - ", "")
        Value_column = df[df.columns[1]]
        bar_width = 0.6
        fig, ax = plt.subplots()
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        plt.barh(df.index, Value_column, bar_width, align="center", color="#466fc6")
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        plt.gca().set_ylim(-1.0, len(Category_column))
        plt.gca().set_yticks(df.index)
        plt.gca().set_yticklabels(Category_column)
        plt.gca().set_xlabel(x_label, fontdict={"size": 8})
        plt.gca().set_ylabel(y_label)
        plt.gcf().set_size_inches(width, height)
        plt.tight_layout()

        if totalDataPts == 0:
            ax.axes.set_xticks(range(len(Category_column)))
            ax.axes.set_xticklabels(range(len(Category_column)))

        # plt.gca().set_ylim([0,df[Val_1Name].max() + df[Val_1Name].max()*.17])
        # plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        # ax.tick_params(axis='both', which='major', labelsize=4)
        for i in range(len(df)):

            if df.loc[i, Val_1Name] > 0:
                label = df.loc[i, Val_1Name]

                plt.annotate(
                    label,  # this is the text
                    (df.loc[i, Val_1Name], i),  # this is the point to label
                    textcoords="offset points",  # how to position the text
                    xytext=(7, -3),  # distance from text to points (x,y)
                    ha="center",  # horizontal alignment can be left, right or center
                    fontsize=8,
                )
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.savefig(name, transparent=True, dpi=500, bbox_inches="tight")
        plt.clf()
        return name

    def line_chart(df1, df2, width, height, name, showAxis, small):
        """Define line chart attributes."""
        Value_column = df1[df1.columns[1]]
        Value_column2 = df2[df2.columns[1]]
        fig, ax = plt.subplots()
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)

        plt.plot(df1.index, Value_column, label="Web only")
        plt.plot(df2.index, Value_column2, label="Dark Web")
        if small:
            pad = 1.4
        else:
            pad = -0.5
        plt.legend(loc=9, ncol=2, framealpha=0, fontsize=8, bbox_to_anchor=(0.5, pad))
        plt.gcf().set_size_inches(width, height)
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        if showAxis:
            plt.gca().set_ylabel("Mentions count", labelpad=10, fontdict={"size": 8})
        plt.xticks(rotation=30, ha="right")
        plt.grid(axis="y")
        plt.tight_layout()

        for i, j in df1[df1.columns[1]].items():
            ax.annotate(
                str(j),
                xy=(i, j),
                textcoords="offset points",  # how to position the text
                xytext=(0, 5),  # distance from text to points (x,y)
                ha="center",  # horizontal alignment can be left, right or center
                fontsize=7,
            )
        for i, j in df2[df2.columns[1]].items():
            ax.annotate(
                str(j),
                xy=(i, j),
                textcoords="offset points",  # how to position the text
                xytext=(5, 5),  # distance from text to points (x,y)
                ha="center",  # horizontal alignment can be left, right or center
                fontsize=7,
            )

        plt.savefig(name, transparent=True, dpi=500, bbox_inches="tight")

        plt.clf()
        return name
