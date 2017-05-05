df_num = df2.sample(frac=0.1)
axs = pd.scatter_matrix(df_num, figsize=(12, 12));

# Rotate axis labels and remove axis ticks
n = len(df_num.columns)
for i in range(n):
    v = axs[i, 0]
    v.yaxis.label.set_rotation(0)
    v.yaxis.label.set_ha('right')
    v.set_yticks(())
    h = axs[n-1, i]
    h.xaxis.label.set_rotation(90)
    h.set_xticks(())
