from pdf_mail import sendpdf
###mail=sendpdf("ashokkumarakay96@gmail.com","abishakeashokkumar97@gmail.com","ygmlbrfiehsrdjyv","Demo_from_script","demo from script","test","D:/python/")
###mail.email_send()
def show_stars(rows):
    for i in range(0,rows+1):
        for j in range(0,i):
            print("*", end = "")
        print("\n")
print(show_stars(5))