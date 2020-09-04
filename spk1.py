paragraph=input("\n[IN]:Enter Your paragraph of spoken english:\n\t")

if not paragraph:
	raise ValueError("[Error]: You entered nothing.")

rules = {"Numbers":{
                        "zero": 0,
                        "one" : 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9,
                        "ten": 10,
                        "hundred":100
                        },
            "Tuples": {
                         "single":1,
                         "double":2,
                         "triple":3,
                         "quadruple":4,
                         "quintuple":5,
                         "sextuple":6,
                         "septuple":7,
                         "octuple":8,
                         "nonuple":9,
                         "decuple":10
                      },
            "General": {
                          "C M": "CM",
                          "P M": "PM",
                          "D M": "DM",
                          "A M": "AM"
                       },
            "Symbols": {
                          "dollars": "$",
                          "dollar": "$",
                          "hastag": "#",
                          
                       }

            }
result=""
numbers=rules['Numbers']
tuples=rules['Tuples']
general=rules['General']
symbols=rules['Symbols']
flag=0
flag1=0
flag2=0
pp1=paragraph.split()
for pp in pp1:
	if pp in tuples:
		b=pp
		flag=1
		continue
	if flag==1 :
		if len(pp)==1 or len(pp)==2:
			a=""
			if "," in pp:
				list3 = pp[:-1]
				
				for i in range(tuples[b]):
					a=a+list3
				a=a+","
			elif "." in pp:
				list3 = pp[:-1]
				
				for i in range(tuples[b]):
					a=a+list3
				a=a+"."	
			else:
				for i in range(tuples[b]):
					a=a+pp
			result=result+a
			result=result+" "
			flag=0
			continue
		else:
			result=result+b+" "
			flag=0
	if pp in numbers:
		temp=str(numbers[pp.lower()])
		flag1=1
		continue
	if flag1==1:
		if pp in symbols:
			a=temp+str(symbols[pp])
			result=result+a
		else:
			result=result+temp
		result=result+" "
		flag1=0
		continue
	if pp=="C" or pp=="A" or pp=="P" or pp=="D":
		temp1=pp
		flag2=1
		continue
	if flag2==1:
		
		temp1=temp1+" "+pp
		if "," in temp1:
			list3 = temp1[:-1]
			if list3 in general:
				result=result+general[temp1]
			else:
				result=result+temp1
			result=result+","
				
		elif "." in temp1:
			list3 = temp1[:-1]
			if list3 in general:
				result=result+general[temp1]
			else:
				result=result+temp1
			result=result+"."
		else:

			if temp1 in general:
				result=result+general[temp1]
			else:
				result=result+temp1
		flag2=0
		continue
	result=result+pp+" "


print(result)
