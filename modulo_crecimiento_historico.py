import matplotlib.pyplot as plt

def crecimiento_historico(df):
    """
    Genera gráficos de las tasas de crecimiento anual (Revenue, EPS y FCF).
    """
    df.plot(x='Ticker', y=['Revenue Growth', 'EPS Growth', 'FCF Growth'], kind='bar', figsize=(10, 6))
    plt.title('Crecimiento Anual: Revenue, EPS y FCF')
    plt.ylabel('Crecimiento %')
    plt.show()
