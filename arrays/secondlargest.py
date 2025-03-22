# 🔹 Find Second Largest Number
def secondLarge(lt):
    larger = -1
    secondlarger = -1
    
    for num in lt:
        if num > larger:
            secondlarger = larger  # ✅ सबसे पहले वाले largest को secondlargest बनाओ
            larger = num  
        elif num > secondlarger and num != larger: 
            secondlarger = num

    return secondlarger  # ✅ सही वैल्यू रिटर्न करो

# 🔹 यूज़र से इनपुट लेना
n = int(input("Enter n: "))  # उपयोगकर्ता से संख्या लें
lt = []
for i in range(n):
    lt.append(int(input()))  # लिस्ट में नंबर जोड़ें

# 🔹 फ़ंक्शन कॉल करें और आउटपुट प्रिंट करें
result = secondLarge(lt)
print("Second Largest:", result)
