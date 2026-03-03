import pandas as pd

# 1. 加载数据 (模拟从日报基础数据读取)
# 假设你有很多个 CSV，Python 可以一秒钟全部读取
df = pd.read_csv('production_data.csv')

# 2. 数据处理：计算总产出和平均废品率
# 这里的逻辑对应你以前在 Excel 里的公式
summary = df.groupby('Line').agg({
    'Output': 'sum',
    'Waste_Rate': 'mean',
    'Labor_Hours': 'sum'
}).reset_index()

# 3. 业务逻辑：计算每小时产量 (Efficiency)
summary['Units_Per_Hour'] = summary['Output'] / summary['Labor_Hours']

# 4. 自动筛选：找出废品率过高的生产线 (比如大于 4%)
high_waste = summary[summary['Waste_Rate'] > 0.04]

# 5. 输出结果
print("--- 生产数据汇总 ---")
print(summary)
print("\n--- 预警：废品率过高的生产线 ---")
print(high_waste)

# 6. 导出到 Excel (这就是你以前手动做的日报底稿)
# summary.to_excel('Monthly_Summary_Report.xlsx', index=False)