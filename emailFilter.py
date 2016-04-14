from validate_email import validate_email
import threading

class EmailFilter():
    inputFileName = "emails.txt"
    outputFileName = "filteredEmails.txt"
    inputFile = file
    outputFile = file
    expiredMails = 0

    def __init__(self, inputFileName, outputFileName):
        self.inputFile = file(inputFileName, "r")
        self.outputFile = file(outputFileName, "a+")
        pass

    def __init__(self):
        self.inputFile = file(self.inputFileName, "r")
        self.outputFile = file(self.outputFileName, "a+")
        pass

    def mailExist(self, mail):
        try:
            return validate_email(mail, verify=True)
        except:
            return False

    def updateMail(self, mail):
        if self.mailExist(mail):
            self.outputFile.write(mail + ",")
        else:
            self.expiredMails += 1

    def processMails(self):
        fileContent = self.inputFile.read()
        processedMails = set(fileContent.split(","))
        print(processedMails)
        for mail in processedMails:
            self.updateMail(mail.strip())
        print("Total Expired Mails: ", self.expiredMails)
        return processedMails


def main():
    emailFilter = EmailFilter()
    emailFilter.processMails()
    #or give your parameters
    #customEmailFilter = EmailFilter("inputfile.txt", "outputfile.txt")
    #customEmailFilter.processMails()


main()
