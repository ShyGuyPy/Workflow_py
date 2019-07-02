import win32com.client
import win32gui as wg
import win32con
import time

prog_ID = "Extend.application"
win_ID = "ExtendSim"

es_handle = win32com.client.Dispatch(prog_ID)
print(es_handle)

app_ID = wg.FindWindow(None, win_ID)
print(app_ID)

#time.sleep(10)

wg.ShowWindow(app_ID, win32con.SW_MAXIMIZE)
#time.sleep(5)
wg.ShowWindow(app_ID, win32con.SW_MAXIMIZE)
#es_handle.Execute("""ActivateApplication()""")

#brings specified worksheet to forefront
es_handle.Execute("""ActivateWorksheet("test_model.mox")""")

#set the run parameters SetEndTime, SetStartTime, SetNumSim, SetNumStep
#es_handle.Execute(""" SetRunParameters(10000, 0 , 1, 1) """)
