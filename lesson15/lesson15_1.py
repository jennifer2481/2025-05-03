import yfinance as yf
from datetime import datetime
import os
import time

def download_data():
    # 在目前目錄下建立一個data的資料夾,如果已經有這個資料夾,就不建立
    data_folder = 'data'
    os.makedirs(data_folder, exist_ok=True)

    stocks = ['2330.TW', '2303.TW', '2454.TW', '2317.TW']
    start_date = '2024-01-01'
    end_date = datetime.now().strftime('%Y-%m-%d')
    today = datetime.now().date()

    for stock_symbol in stocks:
        file_name = os.path.join(data_folder, f"{stock_symbol.split('.')[0]}.csv")
        
        needs_download = False
        # 檢查檔案是否存在
        if not os.path.exists(file_name):
            needs_download = True
            print(f"檔案 {file_name} 不存在，準備下載。")
        else:
            # 檔案存在，檢查最後修改日期
            last_mod_time = os.path.getmtime(file_name)
            last_mod_date = datetime.fromtimestamp(last_mod_time).date()
            if last_mod_date < today:
                needs_download = True
                print(f"檔案 {file_name} 已過期，準備重新下載。")
            else:
                print(f"檔案 {file_name} 今日已下載，跳過。")

        if needs_download:
            max_retries = 3
            retry_delay = 5  # seconds
            for attempt in range(max_retries):
                try:
                    print(f"正在下載 {stock_symbol} 的資料 (第 {attempt + 1}/{max_retries} 次嘗試)...")
                    data = yf.download(stock_symbol, start=start_date, end=end_date, auto_adjust=True)

                    if not data.empty:
                        data.to_csv(file_name)
                        print(f"已將 {stock_symbol} 資料儲存至 {file_name}")
                        break  # 成功下載，跳出重試迴圈
                    else:
                        print(f"警告：未下載到 {stock_symbol} 的資料 (可能為假日或無交易)，檔案未更新。")
                        break  # 視為成功，避免因假日而重複嘗試

                except Exception as e:
                    print(f"下載 {stock_symbol} 時發生錯誤: {e}")
                    if attempt < max_retries - 1:
                        print(f"將在 {retry_delay} 秒後重試...")
                        time.sleep(retry_delay)
                    else:
                        print(f"下載 {stock_symbol} 失敗，已達最大重試次數。")

def main():
    download_data()

if __name__ == '__main__':
    main()
                     