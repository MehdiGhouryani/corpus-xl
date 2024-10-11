import pandas as pd
import re

def normalize_farsi(text):
    #اعداد , علامت های نگارشی , و .. حذف میشوند تا جزء آمار حساب نشوند
    if not isinstance(text, str):
        return ''

    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[،.()\"«»:؛]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()    
    text = text.replace('ك', 'ک').replace('ي', 'ی')     
    return text



#در اینجا ادرس فایل اکسل و بدید 
file_path = 'dependency.xlsx'  

#علاوه بر کتابخانه pandas باید openpyxl و هم نصب کنید تا فرمت xlsx و بشناسه
df = pd.read_excel(file_path, engine='openpyxl')
df['normalized_word'] = df['word'].apply(normalize_farsi)
all_tokens = df['normalized_word'].str.cat(sep=' ').split()



token_count = len(all_tokens)  # تعداد Tokens
type_count = len(set(all_tokens))  # تعداد Types (کلمات منحصر به فرد)

ttr = type_count / token_count 



print(f'Total Tokens: {token_count}')
print(f'Total Types: {type_count}')
print(f'TTR: {ttr:.4f}')




normalized_words = df['normalized_word'].unique() 
first_hundred_words = normalized_words[:100]  



with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f'Total Tokens : {token_count}\n')
    f.write(f'Total Types : {type_count}\n')
    f.write(f'TTR : {ttr:.5f}\n\n\n\n')
    f.write('مجموعه صدتایی از کلمات نرمالایز شده :\n\n')
    for i in range(0, len(first_hundred_words), 10):
        line_words = first_hundred_words[i:i + 10]  
        f.write('  ,  '.join(line_words) +'\n')



