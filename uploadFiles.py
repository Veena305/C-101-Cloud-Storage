import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, local_path, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:

                local_path = os.path.join(root, filename)

                relative_path = os.path.relpth(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

        f = open(local_path, 'rb')
        dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BJRNy0IdBjhPGniRjrvP7GOV9fCxSrvlhpj85K5cnSoxoQLiLPmcjOPU3JxEU-4Iici7ApADcAgGFmbe7ECCU8vxIBwudSqpvHM4N8nRTq8xWUBDCNxqqIo7iUsY0UB584JUOY4'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer :")
    file_to = input("Enter the full path to upload to dropbox :")

    transferData.upload_file(file_from, file_to)
    print("File has been moved !!!")


main()