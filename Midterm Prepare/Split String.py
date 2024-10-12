from collections import Counter
import matplotlib.pyplot as mp

text = """Lãnh thổ Việt Nam xuất hiện con người sinh sống từ thời đại đồ đá cũ, khởi đầu với các nhà nước Văn Lang, Âu Lạc. Âu Lạc bị nhà Triệu ở phương Bắc thôn tính vào đầu thế kỷ thứ 2 TCN sau đó là thời kỳ Bắc thuộc kéo dài hơn một thiên niên kỷ. Chế độ quân chủ độc lập được tái lập sau chiến thắng của Ngô Quyền trước nhà Nam Hán, mở đường cho các triều đại độc lập kế tục, nhiều lần chiến thắng trước các cuộc chiến tranh xâm lược từ phương Bắc đồng thời dần mở rộng về phía nam. Thời kỳ Bắc thuộc cuối cùng kết thúc sau chiến thắng trước nhà Minh của nghĩa quân Lam Sơn."""

# Tách câu
sentences = []
sentence = ""
for char in text:
    if char != '.':
        sentence += char
    else:
        if sentence.strip():
            sentences.append(sentence.strip())
        sentence = "" 
i = 1
for sen in sentences:
    print(f"Câu {i}: {sen}")
    i += 1

print()

# Tách từ
text = text.lower()
words = []
current_word = ''
for char in text:
    if char.isalnum(): 
        current_word += char
    else:
        if current_word:
            words.append(current_word)
            current_word = ''
if current_word:
    words.append(current_word)
for word in words:
    print(word,end ="\t")

print("\n")        
        
# Đếm tần số
word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word}: {count}")

# Tổng số từ
total_words = sum(word_count.values())
print(f"\nTổng số từ: {total_words}")

# Vẽ biểu đồ
labels = list(word_count.keys())
values = list(word_count.values())

sorted_word_count = word_count.most_common()
labels, values = zip(*sorted_word_count)

mp.figure(figsize=(12, 6))
mp.plot(labels, values, marker='o', linestyle='', color = 'red')
mp.xlabel('Từ')
mp.ylabel('Tần số ')
mp.title('Tần số của các từ trong văn bản (Biểu đồ đường)')
mp.xticks(rotation=90)
mp.tight_layout()
mp.grid()
mp.show()