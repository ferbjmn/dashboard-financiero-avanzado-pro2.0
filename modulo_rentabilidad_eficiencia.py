import matplotlib.pyplot as plt

def rentabilidad_eficiencia(df):
    """
    Genera gráficos comparativos de Rentabilidad y Eficiencia.
    """
    # ROE vs ROA
    df.plot(x='Ticker', y=['ROE', 'ROA'], kind='bar', figsize=(10, 6))
    plt.title('Rentabilidad: ROE vs ROA')
    plt.ylabel('Porcentaje')
    plt.show()

    # WACC vs ROIC
    df.plot(x='Ticker', y=['WACC', 'ROIC'], kind='bar', figsize=(10, 6))
    plt.title('Eficiencia: WACC vs ROIC')
    plt.ylabel('Porcentaje')
    plt.show()
