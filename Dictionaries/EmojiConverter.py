message = input("> ")
words = message.split(' ')

emojis = {
    ":)": "😊",
    ":(": "😔",
    ":}": "😎",
    "rich": "💰",
    "cold": "🥶",
    "sick": "🤒",
    "king" or "queen": "👑",
    "happy": "😁"

}
output = ""
for word in words:
    output += emojis.get(word, word) + ' '
print(output)