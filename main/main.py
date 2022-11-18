from fastapi import FastAPI ,Request ,  UploadFile
from uttils import remove_microsecond , final_list_creator , listing
from fastapi.openapi.utils import get_openapi
import shutil
import srt

app = FastAPI()

@app.post('/api')
def uploadfile(file1 : UploadFile , file2 : UploadFile):
	if file1 and file2:

		namesub1 = file1.filename
		pathsub1 = f'files/{namesub1}'
		namesub2 = file2.filename
		pathsub2 = f'files/{namesub2}'


		with open(pathsub1 , 'w+b') as OPEN:
		  shutil.copyfileobj(file1.file , OPEN)
		  print("sutil done")
		with open(pathsub2 , 'w+b') as OPEN:
		  shutil.copyfileobj(file2.file , OPEN)
		  print("sutil done")

		en_address = open(f'files/{namesub1}')
		de_address = open(f'files/{namesub2}')

		en_list = list(srt.parse(en_address))
		de_list = list(srt.parse(de_address))

#Making Microseconds Zero For English Subtitle
	for i in en_list:
		i.start = remove_microsecond(i.start)
		i.end = remove_microsecond(i.end)

#Making Microseconds Zero For Deutsch Subtitle
	for i in de_list:
		i.start = remove_microsecond(i.start)
		i.end = remove_microsecond(i.end)

	return {
		f"{file1.filename}":listing(en_list),
		f"{file2.filename}":listing(de_list),
	}

@app.get("/get_root_path")
def read_main(request: Request):
    return {"message": "This Message Show Your root_path and be used In Proxy Servers", "root_path": request.scope.get("root_path")}