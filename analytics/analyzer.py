# Phan tich thong ke

def top_ips(df, n=10):
    return df['ip'].value_counts().head(n)

def method_distribution(df):
    return df['method'].value_counts()

def status_code_distribution(df):
    return df['status_code'].value_counts()

def top_urls(df, n=10):
    return df['url'].value_counts().head(n)
