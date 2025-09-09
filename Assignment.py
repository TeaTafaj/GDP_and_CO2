import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/refs/heads/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

df.head()
print(
    df.loc[
        :,
        [
            "Mortality rate, infant (per 1,000 live births)",
            "GDP per capita (constant 2010 US$)",
            "Country Name",
        ],
    ]
)

x = df["GDP per capita (constant 2010 US$)"]
y = df["Mortality rate, infant (per 1,000 live births)"]

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.7)

plt.xlabel("GDP per capita (constant 2010 US$)")
plt.ylabel("Infant Mortality (per 1,000 live births)")
plt.title("Infant Mortality vs GDP per Capita (2015)")

plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
