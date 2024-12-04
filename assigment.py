print("ram is a good boy")
print("ram is a bad boy",end="\n")
print("she is a good girl")



#and gate

a = True
b = True
c = a and b
print(c)

# or gate
a = True
b = False
c = a or b
print(c)

#not gate
a = True
c = not a   
print(c)        

#Bitwise अपरेटरहरू प्रोग्रामिङमा
# Bitwise अपरेटरहरू प्रोग्रामिङमा आधारभूत उपकरणहरू हुन् जुन बिट स्तरमा संख्याहरूको बाइनरी प्रतिनिधित्वहरूमा काम गर्दछ। तिनीहरू कार्यहरूका लागि आवश्यक छन् जसलाई बिटहरूको प्रत्यक्ष हेरफेर आवश्यक पर्दछ, जस्तै निम्न-स्तर प्रोग्रामिङ, उपकरण ड्राइभरहरू, र क्रिप्टोग्राफी।

# बिटवाइज अपरेटरहरूको प्रकार

# and र (&) 
# # bitwise AND अपरेटरले दुई नम्बरहरूको प्रत्येक बिट तुलना गर्छ र नयाँ नम्बर फर्काउँछ जसको बिटहरू 1 मा सेट गरिएको छ भने मात्र अपरेन्डहरूको सम्बन्धित बिटहरू 1 छन्। उदाहरणका लागि:
 
#Python मा उदाहरण
# a = 6 # 0110 बाइनरीमा
# b = 15 # 1111 बाइनरीमा
# परिणाम = a & b # 0110 बाइनरीमा, जुन दशमलवमा 6 छ
# प्रिन्ट (नतिजा) # आउटपुट: 6
# यो अपरेटर प्रायः बिट मास्किङको लागि प्रयोग गरिन्छ, जहाँ संख्याको विशिष्ट बिटहरू जाँच गरिन्छ वा हेरफेर गरिन्छ|

# or वा (|) 
# # bitwise OR अपरेटरले दुई नम्बरहरूको प्रत्येक बिटलाई तुलना गर्छ र नयाँ नम्बर फर्काउँछ जसको बिटहरू 1 मा सेट गरिएको छ यदि कम्तिमा एक अपरेन्डको सम्बन्धित बिटहरू 1 छ भने। उदाहरणका लागि:

#Python मा उदाहरण
# a = 6 # 0110 बाइनरीमा
# b = 15 # 1111 बाइनरीमा
# परिणाम = a | b # 1111 बाइनरीमा, जुन दशमलवमा 15 हो
# छाप (नतिजा) # आउटपुट: 15
# यो अपरेटर नम्बर मा विशिष्ट बिट सेट गर्न को लागी उपयोगी छ
# २
# ।
# 
# XOR (^)
# 
# # बिटवाइज XOR (अनन्य OR) अपरेटरले दुई नम्बरहरूको प्रत्येक बिटलाई तुलना गर्छ र ओपेरेन्डहरूको सम्बन्धित बिटहरू मध्ये एउटा मात्र 1 हो भने नयाँ नम्बर फर्काउँछ जसको बिटहरू 1 मा सेट गरिएको छ। उदाहरणका लागि:
 
#Python मा उदाहरण
# a = 6 # 0110 बाइनरीमा
# b = 15 # 1111 बाइनरीमा
# परिणाम = a ^ b # 1001 बाइनरीमा, जुन दशमलवमा 9 हो
# प्रिन्ट(नतिजा) # आउटपुट: ९
# यो अपरेटर प्राय: टगलिङ बिटहरू वा साधारण इन्क्रिप्शन प्रविधिहरूको लागि प्रयोग गरिन्छ| 
# होइन (~)
# 
#  bitwise NOT अपरेटर एक unary अपरेटर हो जसले यसको अपरेन्डका सबै बिटहरूलाई उल्टो गर्छ, 1s लाई 0s र 0s लाई 1s मा परिणत गर्दछ। उदाहरणका लागि:
# 
#Python पाइथन मा उदाहरण
# a = 6 # 0110 बाइनरीमा
# परिणाम = ~a # 1001 बाइनरीमा (दुईको पूरक प्रतिनिधित्व), जुन दशमलवमा -7 छ
# प्रिन्ट(नतिजा) # आउटपुट: -7
# यो अपरेटर बिटवाइज नकारात्मक को लागी उपयोगी छ

# बायाँ शिफ्ट (<<) 
# # बायाँ शिफ्ट अपरेटरले ० सेकेन्डमा खाली गरिएका बिट्सहरू भरेर निर्दिष्ट स्थानहरूद्वारा यसको अपरेन्डका बिटहरूलाई बायाँतिर सार्छ। उदाहरणका लागि:
# 
#Python मा उदाहरण
# a = 6 # 0110 बाइनरीमा
# परिणाम = a << 2 # 11000 बाइनरीमा, जुन दशमलवमा 24 हो
# छाप (नतिजा) # आउटपुट: 24
# यो अपरेटर सिफ्ट गणनाको पावरमा उठाइएको संख्यालाई 2 ले गुणन गर्न बराबर छ
 
# दायाँ शिफ्ट (>>)
# 
# दायाँ शिफ्ट अपरेटरले निर्दिष्ट स्थानहरूको संख्याद्वारा यसको अपरेन्डको बिटहरूलाई दायाँतिर सिफ्ट गर्दछ। उदाहरणका लागि:
# 
#Python मा उदाहरण
# a = 6 # 0110 बाइनरीमा
# परिणाम = a >> 1 # 0011 बाइनरीमा, जुन दशमलवमा 3 हो
# प्रिन्ट(नतिजा) # आउटपुट: ३
# यो अपरेटर सिफ्ट गणनाको पावरमा उठाइएको संख्यालाई 2 ले भाग गर्न बराबर छ|
# 
# प्रयोगहरू
# 
# Bitwise अपरेटरहरू विभिन्न अनुप्रयोगहरूमा व्यापक रूपमा प्रयोग गरिन्छ, जसमा:
# 
# यन्त्र ड्राइभरहरू: बिट स्तरमा हार्डवेयर नियन्त्रणको लागि।
# 
# क्रिप्टोग्राफी: एन्क्रिप्शन र डिक्रिप्शन एल्गोरिदमहरूको लागि।
# 
# ग्राफिक्स प्रोग्रामिङ: पिक्सेल मानहरू हेरफेरको लागि।
# 
# नेटवर्क प्रोग्रामिङ: प्रोटोकल हेडर र झण्डाहरू ह्यान्डल गर्नका लागि |
# 
# बिटवाइज अपरेटरहरू बुझ्न र निपुणताले प्रभावकारी र निम्न-स्तर कोड लेख्ने तपाईंको क्षमतालाई उल्लेखनीय रूपमा वृद्धि गर्न सक्छ।
# 

a = 4 
b = 5
c = a&b   
print(c)

a = 4
b = 5
c = a|b
print(c)

a = 4
b = 5
c = a^b
print(c)

a = 4
b = 5
c = ~a
print(c)

a = 4
b = 5
c = a<<b
print(c)

a = 4
b = 5
c = a>>b
print(c)

        