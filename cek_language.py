from textblob import TextBlob

input_bahasa = "నేను నిన్ను ప్రేమిస్తున్నాను"
input_bahasa = TextBlob(input_bahasa)
print(input_bahasa.detect_language())