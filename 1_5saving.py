# 1_5 Saving output in python

output_data = "This is some output that I want to save."
with open('doc2.txt', 'w') as file:
    file.write(output_data)
print("Successfully replaced the text with given text")
