# Ve bieu do

import matplotlib.pyplot as plt

def plot_top_ips(df, n=10):
    df['ip'].value_counts().head(n).plot(kind='bar')
    plt.title(f"Top {n} IP thực hiện request")
    plt.xlabel("IP")
    plt.ylabel("Số lượng")
    plt.tight_layout()
    plt.show()

def plot_http_methods(df):
    df['method'].value_counts().plot(kind='bar')
    plt.title("Tần suất HTTP Methods")
    plt.xlabel("Method")
    plt.ylabel("Số lượng")
    plt.tight_layout()
    plt.show()
