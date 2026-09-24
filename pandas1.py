#pivot_table()
pd.pivot_table(
    data,
    values="Survived",
    index="Sex",
    columns="Pclass",
    aggfunc="mean"
)

