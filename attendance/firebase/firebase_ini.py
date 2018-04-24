import firebase_admin;
from firebase_admin import credentials;
from firebase_admin import storage;


def upload_file(filename):
    cred=credentials.Certificate('firebase/shubam-firebase-adminsdk-j4p7g-2cab53e953.json');
    default_app=firebase_admin.initialize_app(cred,{
        'storageBucket': 'shubam.appspot.com'
    });
    bucket=storage.bucket();

    uploadBlob = bucket.blob('attendance/'+filename);
    #uploadBlob = bucket.get_blob('attendance2018-09-10.xls');
    print(uploadBlob);
    uploadBlob.upload_from_filename(filename='firebase/attendance_files/'+filename);
    print('file uploaded! ');
