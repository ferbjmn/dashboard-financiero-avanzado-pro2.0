import matplotlib.pyplot as plt

def estructura_deuda(df):
    """
    Genera gráficos comparativos de Apalancamiento y Liquidez de las empresas.
    """
    # Apalancamiento
    df.plot(x='Ticker', y=['Debt/Eq', 'LTDebt/Eq'], kind='bar', figsize=(10, 6))
    plt.title('Apalancamiento: Debt-to-Equity vs Long-Term Debt-to-Equity')
    plt.ylabel('Ratio')
    plt.show()

    # Liquidez
    df.plot(x='Ticker', y=['Current Ratio', 'Quick Ratio', 'Cash Ratio'], kind='bar', figsize=(10, 6))
    plt.title('Liquidez: Ratios de Liquidez')
    plt.ylabel('Ratio')
    plt.show()
