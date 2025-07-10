import matplotlib.pyplot as plt

def analisis_valoracion(df):
    """
    Genera gráficos comparativos de P/E, P/B, P/FCF y rendimiento de dividendos.
    """
    df.plot(x='Ticker', y=['P/E', 'P/B', 'P/FCF'], kind='bar', figsize=(10, 6))
    plt.title('Comparativa de Ratios de Valoración')
    plt.ylabel('Valor')
    plt.show()

    df.plot(x='Ticker', y=['Dividendo', 'Payout Ratio'], kind='bar', figsize=(10, 6))
    plt.title('Rendimiento de Dividendos')
    plt.ylabel('Valor')
    plt.show()
