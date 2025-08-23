from nltk.corpus import words
import nltk

# تحميل قاموس الكلمات (مرة واحدة فقط)
nltk.download('words')

# الحصول على كلمات إنجليزية مكونة من 6 حروف
word_list = [word.lower() for word in words.words() if len(word) == 5]

# الشروط
required_letters = {'t', 'e'}
excluded_letters = {'o', 'k', 'n'}

def is_valid(word):
    return (
        required_letters.issubset(set(word)) and
        word[3] == 'e' and            # الحرف الثالث = c
        word[0] != 't' and 
        #word[3] != 's' and 
        #word[0] != 'a' and            # الحرف الثاني ≠ e
       #word[3] == 'p' and
       #word[2] == 'a' and 
       #word[2] == 'c' and 
       #word[4] == 's' and  
        #word.count('t') == 1 and      # e لا يتكرر مرتين
        #word.count('o') == 1 and 
        # word[4] != 'r' and            # الحرف الخامس ≠ r
        
        
        not any(letter in excluded_letters for letter in word)
    )

# تطبيق الشروط
valid_words = [word for word in word_list if is_valid(word)]

# عرض النتائج
print(valid_words[:20])  # عرض أول 20 كلمة مطابقة إن وُجدت
