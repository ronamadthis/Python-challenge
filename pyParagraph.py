text="Two challenges to providing health services for adolescents are maintaining confidentiality of services (i.e., keeping private patients’ personal health information that is disclosed to their health care provider) and understanding minor consent laws (i.e., laws that enable minors to give consent for certain health care services). Providers have limits on how and when patient information can be shared with others. Traditionally, they are able to share health information only under limited circumstances, particularly if the young person poses a risk to himself or herself or others. Concern also exists in situations where an explanation of benefits might be sent from an insurer to the primary policyholder, revealing the sensitive nature of a medical care visit (25). Minor consent laws vary considerably among states with regard to whether adolescents are able to give consent for selected sensitive health care services, including screening and treatment for sexually transmitted infections, mental health counseling, substance use services, and reproductive health services. Addressing these challenges to confidentiality and clarifying and communicating information about minor consent laws to adolescents, parents, schools, and health care providers are required to ensure that these barriers to adolescent health care are eliminated. "

import re
lst = re.findall("[a-zA-Z_]+", text)
print(lst)


def averageLen(lst):
	lengths = [len(i) for i in lst]
	return (float(sum(lengths))/len(lengths))
aveLen = averageLen(lst)
total_words = len(lst)

print("Approximate word count: " + str(total_words))
print("The average Letter Count: " + str(aveLen))

wordcounts =[]
sentzCount = text.count(". ")
avgWordCount = total_words/sentzCount
print("Approximate Sentence Count: " + str(sentzCount))


print("Average Sentence Length: " + str(avgWordCount))