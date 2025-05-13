import os
files=os.listdir("Pictures")
for i in range(len(files)):
    file_path=os.path.join("Pictures",files[i])
    try:
        os.remove(file_path)
        print(f"Deleted: {files[i]}")
    except Exception as e:
        print(f"⚠️ Unknown error with {files[i]}: {e}")
    
