import yfinance as yf
import pandas as pd
import time

def obtener_datos_acciones(tickers):
    """
    Obtiene las métricas clave de las acciones usando Yahoo Finance y las muestra en una tabla comparativa.
    """
    datos = []
    
    for ticker in tickers:
        try:
            empresa = yf.Ticker(ticker)
            time.sleep(1)  # Evitar bloqueos

            # Obtener datos clave
            info = empresa.info
            wacc, roic, diferencia_roic_wacc, creando_valor = calcular_wacc_y_roic(ticker)

            datos.append({
                'Ticker': ticker,
                'Compañía': info.get('longName', 'N/A'),
                'Sector': info.get('sector', 'N/A'),
                'Industria': info.get('industry', 'N/A'),
                'País': info.get('country', 'N/A'),
                'P/E': info.get('trailingPE', 'N/A'),
                'P/B': info.get('priceToBook', 'N/A'),
                'P/FCF': info.get('priceToFreeCashFlows', 'N/A'),
                'Dividendo': info.get('dividendRate', 'N/A'),
                'Payout Ratio': info.get('payoutRatio', 'N/A'),
                'ROA': info.get('returnOnAssets', 'N/A'),
                'ROE': info.get('returnOnEquity', 'N/A'),
                'Current Ratio': info.get('currentRatio', 'N/A'),
                'LTDebt/Eq': info.get('longTermDebtToEquity', 'N/A'),
                'Debt/Eq': info.get('debtToEquity', 'N/A'),
                'Oper Margin': info.get('operatingMargins', 'N/A'),
                'Profit Margin': info.get('profitMargins', 'N/A'),
                'WACC': wacc,
                'ROIC': roic,
                'Creación de Valor (WACC vs ROIC)': 'Creando valor' if creando_valor else 'No creando valor'
            })
        except Exception as e:
            print(f"Error al obtener datos para {ticker}: {e}")
    
    return pd.DataFrame(datos)
