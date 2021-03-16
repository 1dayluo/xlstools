
import os
import xlrd
from fastapi import FastAPI,Query,File,UploadFile
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from io import BytesIO,StringIO
xls_path = '..\dga恶意检测\dga.xlsx'

# class Item(BaseModel):
#     data:list
def xls_read(xls_path,col_index, sheet=0):
    """
    parms:
        col_num:The index of the col to be obtained 
        sheet:The index of the sheet to be obtained

    """
    values = []

    # 读取xls文件
    workbook = xlrd.open_workbook(file_contents=xls_path)
    # 选择sheet
    worksheet = workbook.sheet_by_index(sheet)
    # 获取全部行
    for i in range(1, worksheet.nrows):
        # 获取特定单元值
        cell = worksheet.cell_value(i, col_index)
        values.append(cell)

    return values



app = FastAPI()

#
@app.post("/datas")
async def xlsdata(file:bytes=File(...),sheet: int = 0,colindex: int = 12):
    # stream = StringIO()
    print(file)
    values = []
    workbook = xlrd.open_workbook(file,encoding_override='utf-8')
    # 选择sheet
    worksheet = workbook.sheet_by_index(sheet)
    # 获取全部行
    for i in range(1, worksheet.nrows):
        # 获取特定单元值
        cell = worksheet.cell_value(i, colindex)
        values.append(cell)

    return {'value':values}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...),colindex:int=12):
    if(file.filename.split('.')[-1] == 'xlsx' or file.filename.split('.')[-1] == 'xlsx'):
        filecontent = await file.read()

        datas = xls_read(filecontent,colindex)

        return datas
    else:
        return '请检查文件格式是否为xls'
