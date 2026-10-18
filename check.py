# import pandas as pd
# import numpy as np
#
# # خواندن فایل (از نام جدید فایل استفاده می‌کنیم)
# df = pd.read_csv('StudentsPerformance-(2).csv')
#
# print("=" * 50)
# print("۱. بررسی سخت‌گیرانه مقادیر خالی (شامل NaN واقعی، فضاهای خالی و مقادیر متفرقه)")
# # جایگزینی مقادیر مشکوک با NaN واقعی
# missing_placeholders = ["?", "N/A", "null", "NULL", " ", "", "NA", "None"]
# df_cleaned = df.replace(missing_placeholders, np.nan)
#
# null_check = df_cleaned.isnull().sum()
# print(null_check)
#
# print("\n" + "=" * 50)
# print("۲. بررسی سطرهای تکراری (دقیق)")
# print(f"تعداد کل سطرهای تکراری کاملاً یکسان: {df.duplicated().sum()}")
#
# print("\n" + "=" * 50)
# print("۳. بررسی سخت‌گیرانه اوت‌لایرها در ستون‌های عددی (با فرمول IQR)")
# numeric_cols = ['math score', 'reading score', 'writing score']
#
# for col in numeric_cols:
#     Q1 = df[col].quantile(0.25)
#     Q3 = df[col].quantile(0.75)
#     IQR = Q3 - Q1
#     lower = Q1 - 1.5 * IQR
#     upper = Q3 + 1.5 * IQR
#
#     outliers = df[(df[col] < lower) | (df[col] > upper)]
#     print(f"ستون '{col}': تعداد اوت‌لایرها = {len(outliers)}")
#     if len(outliers) > 0:
#         print(outliers[col].values)
#
# print("\n" + "=" * 50)
# print("۴. بررسی کاراکترهای نامعتبر یا فضاهای خالی در ستون‌های متنی (Categorical)")
# cat_cols = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
#
# for col in cat_cols:
#     # بررسی مقادیر منحصربه‌فرد برای دیدن اینکه آیا مقدار عجیبی وجود دارد یا خیر
#     print(f"مقادیر منحصر‌به‌فرد در '{col}':")
#     print(df[col].unique())
