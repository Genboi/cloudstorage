import dropbox
class TransferData:
    def __init__ (self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token='sl.A_vAB4p58N7p13ahRzT20lF_3gdgqt3qni47JAhqu_K7cQnt0plxwRkxmWeRR9RBaprdlNo_E7CH3XfJ1pANBduUKqxISbvYipkZaIbg_mij4yKm4-ptsBb4psTnyVpvFQnGBSwMAPaH'
    transferData=TransferData(access_token)
    file_from=input("enter file path to transfer:- ")
    file_to=input("enter the file path to upload:- ")        
    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()