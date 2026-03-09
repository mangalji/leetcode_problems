# 58. Length of Last Word

# s = "Hello World"
# s = "   fly me   to   the moon  "
s = "luffy is still joyboy"

chars = s.strip()
# print(chars)
char_list = chars.split()
# print(char_list)
print(len(char_list[-1]))
