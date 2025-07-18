# 台股歷史股價視覺化專案

## 專案目標 (Project Goal)
我們要建立一個使用 Streamlit 驅動的 Web 應用程式，用於視覺化台股歷史股價。

## 核心功能 (Core Features)

1. **資料獲取**：能夠使用 `yfinance` 套件下載指定的台股歷史資料。
2. **專案資料夾**: lesson16
3. **互動介面**：
    - 提供股票選單，讓使用者可以選擇想查詢的股票。
    - 提供日期區間選擇器，讓使用者能篩選特定時間範圍的資料。
    - 以表格形式顯示篩選後的股價資料。
    - 以折線圖形式視覺化所選股票在指定時間內的價格走勢。

## 開發流程與規則 (Development Workflow & Rules)

1. **迭代開發**：我們將採用迭代（step-by-step）的方式完成這個專案。
2. **任務清單 (Todolist)**：在每一次的互動中，我會提供一個任務清單。
3. **您的任務**：
    - 請先檢查清單中已完成的項目 (`[x]`)。
    - 接著，請完成清單中**尚未**完成的項目 (`[]`)。
    - 完成後，請在您的回覆中更新任務清單，將您剛完成的項目打勾 (`[x]`)。

---

## 本階段任務 (Current Task)

### Todolist

- [x] 專案功能已大致完成，請檢查目前的 UI/UX 設計，思考是否還有可以優化的地方，讓使用者操作時能有更好的體驗。請具體列出建議或可以改進的細節。

### UI/UX 優化建議

1. **資料載入提示**：下載或載入資料時，建議加上 Streamlit 的 `st.spinner` 或 `st.progress`，讓使用者知道正在處理，避免誤以為系統卡住。
2. **股票選單排序**：將股票選單依照名稱或代號排序，方便快速查找。
3. **預設日期區間**：目前預設為近 7 天，建議可提供「快速選擇」如「近一週」、「近一月」、「今年以來」等按鈕，提升便利性。
4. **表格顯示**：目前僅有圖表，建議在圖表下方加上 `st.dataframe` 顯示篩選後的原始數據，方便使用者查閱實際數值。
5. **錯誤處理與提示**：若資料下載失敗、無法連線或無資料時，應有明確的錯誤訊息與重試按鈕。
6. **圖表互動性**：可考慮加入滑鼠懸停顯示詳細數值、放大縮小等互動功能（Plotly 已支援，但可在說明中提示）。
7. **介面說明**：在頁面頂部加上簡短說明，讓新手用戶快速了解如何操作。
8. **多語系支援**：若有外籍使用者，可考慮加入英文介面切換。
9. **行動裝置相容性**：檢查在手機或平板上的顯示效果，必要時調整元件寬度或排版。
10. **主題色彩與字型**：可自訂 Streamlit 主題色彩、字型，讓整體視覺更符合台股或金融主題。
