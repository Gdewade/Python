# qoute1="Hello wolrd"
# quote2="welcome to python"

# fobj=open("file1.txt",'w')  # filename

# fobj.write(qoute1)
# fobj.write(quote2)

# fobj.close

pets=["cats\n","dog\n","bird\n"]
fobj3=open("text3.txt","w")
fobj3.writelines(pets)
fobj3.close()
