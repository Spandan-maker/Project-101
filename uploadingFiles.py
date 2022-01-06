import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = str(input("Enter your Dropbox App Token: "))
    transferData = TransferData(access_token)

    file_from = str(input("Enter the file/folder you want to upload: "))

    print("Path format example: /text_folder/text.txt \nEnter your folder name that you want the file to be in and the orginal file name.")
    file_to = str(input("Enter the path with the file/folder name: "))

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()