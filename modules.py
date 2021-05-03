import openpyxl
from openpyxl_image_loader import SheetImageLoader
from docx.enum.section import WD_SECTION
from docx.enum.section import WD_ORIENT
from docx.shared import Mm
from docx import Document
from docx.shared import Inches
import os
import win32com.client as win32
from pathlib import Path


def change_orientation(document):
    current_section = document.sections[0]
    new_width, new_height = current_section.page_height, current_section.page_width
    new_section = document.add_section(WD_SECTION.NEW_PAGE)
    new_section.orientation = WD_ORIENT.LANDSCAPE
    new_section.page_width = Mm(297)
    new_section.page_height = Mm(211)
    # current_section.orientation = WD_ORIENT.LANDSCAPE
    # current_section.page_width = Mm(297)
    # current_section.page_height = Mm(211)


def wrapping_pictures(document):
    word = win32.gencache.EnsureDispatch("Word.Application")
    doc = word.Documents.Open(document)
    for k,shape in enumerate(doc.InlineShapes):
        shape.ConvertToShape()
    for z,picture in enumerate(doc.Shapes):
        picture.WrapFormat.Type = 2
        picture.RelativeVerticalPosition = 1
        picture.RelativeHorizontalPosition = 1
        picture.Left = 0
        picture.Top = 0
    doc.Save()
    doc.Close()


def extract_img_to_word_doc(list,docu,savePath):
    count = 0
    for tups in list:
        if tups[0] == '':
            continue
        else:
            pxl_doc = openpyxl.load_workbook(tups[0])
            sheet = pxl_doc.worksheets[0]
            img_loader = SheetImageLoader(sheet)
            image_start = int(tups[1])
            image_end = int(tups[2])
            for i in range(image_start,image_end+1):
                image = img_loader.get("C{}".format(i))
                image_name = "image{}.png".format(count)
                image.save(image_name)
                count += 1
                docu.add_picture(image_name, width=Mm(297), height=Mm(210))
                os.remove(image_name)
            docu.save(savePath)

#wrapping_pictures(r"c:\Users\ehom\Documents\IdeaProjects\Python\Projects\merckScreenshotFormatter\sample files\MK1308A-004_eCOA Tablet_German (Switzerland)_v1.00_16NOV2020_2.docx")