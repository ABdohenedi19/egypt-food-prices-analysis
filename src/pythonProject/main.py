import pandas as pd

# 1. تحميل الداتا سيت الأولى (الأسعار)
# افترضنا أن اسمها prices.csv
df_prices = pd.read_csv('prices.csv')

# 2. تحميل الداتا سيت الثانية (بيانات الأسواق)
# افترضنا أن اسمها markets_lookup.csv
df_markets = pd.read_csv('markets_lookup.csv')

# 3. عملية الدمج (Integration) باستخدام الـ market_id
# هنستخدم Left Join عشان نحافظ على كل بيانات الأسعار ونضيف لها بيانات المكان
merged_df = pd.merge(
    df_prices,
    df_markets[['market_id', 'admin1', 'admin2']],
    on='market_id',
    how='left'
)

# 4. اختيار وترتيب الأعمدة المطلوبة للفورمات النهائي
# Feature Product, Category, Price, Date, Governorate, Market, Unit
final_df = merged_df[[
    'commodity',    # Product
    'category',     # Category
    'price',        # Price
    'date',         # Date
    'admin1',       # Governorate
    'market',       # Market
    'unit'          # Unit
]]

# 5. إعادة تسمية الأعمدة لتطابق طلبك بالظبط
final_df.columns = ['Product', 'Category', 'Price', 'Date', 'Governorate', 'Market', 'Unit']

# 6. حفظ النتيجة النهائية في ملف جديد
final_df.to_csv('final_integrated_dataset.csv', index=False)

print("تم دمج البيانات بنجاح وحفظها في final_integrated_dataset.csv")
print(final_df.head())

