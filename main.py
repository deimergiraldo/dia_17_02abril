#Vamos a importar la librería de excel
import openpyxl

#Crea un archivo de excel
deimer= openpyxl.Workbook()


#Vamos a cambiar el nombre de la hoja
#bailes.titles('NuevosBailes')

deimer.save('excel_deimer.xlsx')

from openpyxl import load_workbook

dei= load_workbook('excel_deimer.xlsx')

#Crea varias hojas de calculo en el mismo archivo de excel
canciones=dei.create_sheet('Hoja1')
bailes=dei.create_sheet('Hoja2',0)
discotecas=dei.create_sheet('Hoja3',-1)

dei.save('excel.deimer.xlsx')