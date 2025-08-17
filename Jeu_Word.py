# قائمة الحروف الممنوعة
forbidden_letters = set('sfektmwr')

# تحميل قائمة كلمات إنجليزية من ملف أو من قاموس افتراضي
# هنا نستخدم كلمات مدمجة مع Python للتجريب
import nltk
nltk.download('words')
from nltk.corpus import words

# فلترة الكلمات بناءً على الشروط
valid_words = []
for word in words.words():
    word = word.lower()
    if len(word) == 4:
        if word[1] == 'a' and word[3] == 'p' and word[0] != 'p':
            if not any(char in forbidden_letters for char in word):
                valid_words.append(word)

# عرض النتائج
print("الكلمات المطابقة:")
print(valid_words)
 