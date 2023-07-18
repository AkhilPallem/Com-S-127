#Akhil Pallem Lab week 11 
dict = {"AAA": {}, "AAS": {}, "ASA": {}, "SAA": {},
"SSS": {}, "SSA": {}, "SAS": {}, "ASS": {},
"AMA": {}, "AAM": {}, "MMM": {},
"MMM": {}, "MMA": {}, "MAM": {}, "AMM": {},
"MMS": {}, "MSM": {}, "SMM": {},"SSM": {}, 
"SMS": {}, "MSS": {}, "ASM": {}, "MAS": {}, 
"SMA": {}, "MSA": {}, "AMS": {}, "SAM": {}}
list = {}

def AAA(a, b ,c, d):
    final = a + b + c + d
    return final 

def AAS(a, b ,c, d):
    final = a + b + c - d
    #dict["AAS"].append(str(final))
    return final 

def ASA(a, b ,c, d):
    final = a + b - c + d
    #dict["ASA"].append(str(final))
    return final 

def SAA(a, b ,c, d):
    final = a - b + c + d
    #dict["SAA"].append(str(final))
    return final 

def SSS(a, b ,c, d):
    final = a - b - c - d
    #dict["SSS"].append(str(final))
    return final 

def SSA(a, b ,c, d):
    final = a - b - c + d
    #dict["SSA"].append(str(final))
    return final 

def SAS(a, b ,c, d):
    final = a - b + c - d
    #dict["SAS"].append(str(final))
    return final 

def ASS(a, b ,c, d):
    final = a + b - c - d
    #dict["ASS"].append(str(final))
    return final 

def AMA(a, b ,c, d):
    final = a + b * c + d
    #dict["AMA"].append(str(final))
    return final 

def MAA(a, b ,c, d):
    final = a * b + c + d
    #dict["MAA"].append(str(final))
    return final 

def AAM(a, b ,c, d):
    final = a + b + c * d
    #dict["AAM"].append(str(final))
    return final 

def MMM(a, b ,c, d):
    final = a * b * c * d
    #dict["MMM"].append(str(final))
    return final 

def MMA(a, b ,c, d):
    final = a * b * c + d
    #dict["MMA"].append(str(final))
    return final 

def MAM(a, b ,c, d):
    final = a * b + c * d
    #dict["MAM"].append(str(final))
    return final 

def AMM(a, b ,c, d):
    final = a + b * c * d
   #dict["AMM"].append(str(final))
    return final 

def MMS(a, b ,c, d):
    final = a * b * c - d
    #dict["MMS"].append(str(final))
    return final

def MSM(a, b ,c, d):
    final = a * b - c * d
    #dict["MSM"].append(str(final))
    return final

def SMM(a, b ,c, d):
    final = a - b * c * d
    #dict["SMM"].append(str(final))
    return final

def SSM(a, b ,c, d):
    final = a - b - c * d
    #dict["SSM"].append(str(final))
    return final 

def SMS(a, b ,c, d):
    final = a - b * c - d
    #dict["SMS"].append(str(final))
    return final 

def MSS(a, b ,c, d):
    final = a * b - c - d
    #dict["MSS"].append(str(final))
    return final 

def ASM(a, b ,c, d):
    final = a + b - c * d
    #dict["ASM"].append(str(final))
    return final 

def MAS(a, b ,c, d):
    final = a * b + c - d
    #dict["MAS"].append(str(final))
    return final  

def SMA(a, b ,c, d):
    final = a - b * c + d
    #dict["SMA"].append(str(final))
    return final 

def MSA(a, b ,c, d):
    final = a * b - c + d
   # dict["MSA"].append(str(final))
    return final 

def AMS(a, b ,c, d):
    final = a + b * c - d
    #dict["AMS"].append(str(final))
    return final  

def SAM(a, b ,c, d):
    final = a - b + c * d
    #dict["SAM"].append(str(final))
    return final  

def main():
    a = int(input("Number a: "))
    b = int(input("Number b: "))
    c = int(input("Number c: "))
    d = int(input("Number d: "))
    dict["AAA"]=(str(AAA(a, b , c , d)))
    dict["AAS"]=(str(AAS(a, b , c , d)))
    dict["ASA"]=(str(ASA(a, b , c , d)))
    dict["SAA"]=(str(SAA(a, b , c , d)))
    dict["SSS"]=(str(SSS(a, b , c , d)))
    dict["SSA"]=(str(SSA(a, b , c , d)))
    dict["SAS"]=(str(SAS(a, b , c , d)))
    dict["ASS"]=(str(ASS(a, b , c , d)))
    dict["AMA"]=(str(AMA(a, b , c , d)))
    dict["MAA"]=(str(MAA(a, b , c , d)))
    dict["AAM"]=(str(AAM(a, b , c , d)))
    dict["MMM"]=(str(MMM(a, b , c , d)))
    dict["MMA"]=(str(MMA(a, b , c , d)))
    dict["MAM"]=(str(MAM(a, b , c , d)))
    dict["AMM"]=(str(AMM(a, b , c , d)))
    dict["MMS"]=(str(MMS(a, b , c , d)))
    dict["MSM"]=(str(MSM(a, b , c , d)))
    dict["SMM"]=(str(SMM(a, b , c , d)))
    dict["SSM"]=(str(SSM(a, b , c , d)))
    dict["SMS"]=(str(SMS(a, b , c , d)))
    dict["MSS"]=(str(MSS(a, b , c , d)))
    dict["ASM"]=(str(ASM(a, b , c , d)))
    dict["MAS"]=(str(MAS(a, b , c , d)))
    dict["SMA"]=(str(SMA(a, b , c , d)))
    dict["MSA"]=(str(MSA(a, b , c , d)))
    dict["AMS"]=(str(AMS(a, b , c , d)))
    dict["SAM"]=(str(SAM(a, b , c , d)))
    for key, value in dict.items():
        print(key, ":", value)





main()