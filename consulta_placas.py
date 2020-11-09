from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import csv


def consultaPlaca(placa):
    data_vehicle = []
    data_vehicle.append(placa)

    try:
        quote_page = 'http://consultas.atm.gob.ec/PortalWEB/paginas/clientes/clp_grid_citaciones.jsp?ps_tipo_identificacion=PLA&ps_identificacion=' + placa + '&ps_placa='
        page = requests.get(quote_page)
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table', {'cellpadding': "2"})
        rows = table.find_all('tr')
        for tr in rows:
            # print(tr)
            for wrapper in tr.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['detalle_formulario'] and tag.get('class') == ['detalle_formulario']):
                data_vehicle.append(wrapper.text)
                # print(wrapper.text)
                # write_csv(wrapper.text)
        # print(data_vehicle)
        return data_vehicle
    except Exception as e:
        print('Datos no disponibles')
        print(e)
        return data_vehicle


def write_csv(datos):
   # field names
    fields = ['Placa', 'Marca', 'Color', 'Anio de Matricula', 'Modelo',
              'Clase', 'Fecha de Matricula', 'Anio', 'Servicio', 'Fecha de Caducidad']

    # data rows of csv file
    # name of csv file
    filename = "dataset_placas.csv"

    # writing to csv file
    with open(filename, 'a') as csvfile:
        # creating a csv writer object
        # csvwriter = csv.writer(csvfile)
        # print(datos)
        csvfile.writelines("%s," % place for place in datos)
        csvfile.writelines("\n")
        # for listitem in datos:

        # writing the fields
        # csvwriter.writerow(fields)

        # writing the data rows
        #csvwriter.writerows("%s" % place for place in datos)
        #csvwriter.writerows("%s" % datos)
        # csvwriter.writerow("\n")


def consulta_Puntos(cedula):
    data_puntos = []
    data_puntos.append(cedula)

    try:
        quote_page = 'https://sistematransito.ant.gob.ec:5038/PortalWEB/paginas/clientes/clp_grid_citaciones.jsp?ps_tipo_identificacion=CED&ps_identificacion='+cedula+'&ps_placa='
        page = requests.get(quote_page)
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table', {'cellpadding': "2"})
        rows = table.find_all('tr')
        for tr in rows:
            for wrapper in tr.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['detalle_formulario'] and tag.get('class') == ['detalle_formulario']):
                data_puntos.append(wrapper.text)
                # print(wrapper.text)

        print(data_puntos)
        return data_puntos
    except Exception as e:
        print('Datos no disponibles')
        print(e)
        return data_puntos


if __name__ == "__main__":
    #data_vehicle = []
    file_object = open("FORMATO.txt", "r")
    data = file_object.readlines()
    # print(data)
    #consultaPlaca("AA099C", data_vehicle)
    j = 0
    for i in data:
        j = j+1
        # print(j)
        if j <= 2500:
            print(i.split()[0])
            result = consultaPlaca(i.split()[0])
            print(result)
            write_csv(result)
    # break

    #print(consultaPlaca("AA099C", data_vehicle))
    # for i in data_vehicle:
    #     write_csv(i)
    print("resultado")
    # print(data_vehicle)
