# Phat hien tan cong

def detect_sqli(df):
    sqli_keywords = ['SELECT', 'UNION', 'DROP', '--', '\' OR 1=1', '" OR 1=1']
    df['is_sqli'] = df['payload'].fillna('').str.upper().apply(
        lambda x: any(keyword in x for keyword in sqli_keywords)
    )
    return df[df['is_sqli']]

def detect_xss(df):
    xss_keywords = ['<SCRIPT', 'ALERT(', 'ONERROR=', '<IMG', 'SRC=']
    df['is_xss'] = df['payload'].fillna('').str.upper().apply(
        lambda x: any(keyword in x for keyword in xss_keywords)
    )
    return df[df['is_xss']]

def detect_rce(df):
    rce_keywords = [';wget', ';curl', '`', '||', '&&', '$(']
    df['is_rce'] = df['payload'].fillna('').apply(
        lambda x: any(k in x for k in rce_keywords)
    )
    return df[df['is_rce']]
