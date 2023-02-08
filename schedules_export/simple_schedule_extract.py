import clr 
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import ViewSchedule
from Autodesk.Revit.DB import FilteredElementCollector
from Autodesk.Revit.DB import ViewScheduleExportOptions
import tempfile, os, urllib

walls = FilteredElementCollector(doc).OfClass(Wall)

collector = FilteredElementCollector(doc).OfClass(ViewSchedule)
schedules = {vs.Name: vs for vs in list(collector)}

schedule_name_list = ['ModDoorSchedule','ModPartMaterialTakeoff', 'ModWindowSchedule']

opt = ViewScheduleExportOptions()

fd, fpath = tempfile.mkstemp(suffix='.csv')
os.close(fd)
# dname, fname = os.path.split(fpath)
opt = ViewScheduleExportOptions()
opt.FieldDelimiter = ', '

schedule = schedules[schedule_name_list[0]]

dname ="C:\\Users\\Shaun Gan\\Desktop\\bruns-ai\\example_exports"
fname = doc.Title +"_"+ schedule_name_list[0] + ".csv"
schedule.Export(dname, fname, opt)

with open(fpath, 'r') as csv:
    result = csv.read()
os.unlink(fpath)