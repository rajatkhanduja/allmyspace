from dropbox.client import DropboxClient

class DropboxSyncClient:
    
    def __init__(self, oauth2_access_token):
        self._client = DropboxClient(oauth2_access_token) 

    def upload_file(self, dropbox_file_path, local_file_path, replace = False):
        f = open(local_file_path, 'rb')
        response = self._client.put_file(dropbox_file_path, f, replace)
        return response

    def generate_public_url(self, dropbox_file_path):
        return self._client.share(path)['url']

    def delete_file(self, dropbox_file_path):
        self._client.file_delete(dropbox_file_path)

    def update_local_to_cloud(self, dropbox_file_path, local_file_path):
        return self.upload_file(dropbox_file_path, local_file_path, True)        

    def update_cloud_to_local(self, dropbox_file_path, local_file_path):
        open(local_file_path, 'wb').write(self._client.get_file(dropbox_file_path).read())

    def get_file_list(self, dropbox_folder_path):
        folder_metadata = self._client.metadata(dropbox_folder_path)
        return [content['path'] for content in folder_metadata['contents']]
