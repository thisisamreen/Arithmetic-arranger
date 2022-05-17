def arithmetic_arranger(problems,solve=False):
  #This ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
  """into this
      32      3801      45      123
  +  698    -    2    + 43    +  49
    -----    ------    ----    -----
"""
  first = ""
  second = ""
  lines = ""
  sumx = ""
  string =""
  arranged_problems=""
  for problem in problems:

    #error1
    if len(problems)>5: 
      return "Error: Too many problems."
      break
    #splitting
    fnum = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    snum = problem.split(" ")[2]
    
    if operator =="/" or operator =="*":
      return "Error : Operator must be \'+\' or \'-\'"
    #error 3
    try: 
      n1 = int(fnum)
      n2 = int(snum)
    except:
      return "Error : Numbers must only contain digits"

    #error 4
    if len(fnum)>4 or len(snum)>4:
      return "Error :  Numbers cannot be more than four digits"

    #saving the answers
    sum = ""
    if operator =="+": 
      sum = str(int(fnum) + int(snum))
    elif operator =="-":
      sum = str(int(fnum) - int(snum))

    length = max(len(fnum),len(snum)) +2
    top = str(fnum).rjust(length)
    bottom = operator + str(snum).rjust(length-1)
    line=""
    res = str(sum).rjust(length)
    for s in range(length):
      line+="-"

    if problem!=problems[-1]:
      first +=top + "    "
      second +=bottom + "    "
      lines += line + "    "
      sumx+= res + "    "
    else :
      first +=top
      second +=bottom
      lines+=line
      sumx+=res

  if solve:
    string = first + "\n" + second + "\n" + lines + "\n" + sumx
  else :
    string = first + "\n" + second + "\n" + lines
  arranged_problems = string
  return arranged_problems

problems = ['81 - 2', '123 + 49']
print(arithmetic_arranger(problems,True))