pathologies = {

    "Respiratory system": [

        {

            "id": 1,

            "name": "Cystic Fibrosis",

            "price": 300 	

        },

        {

            "id": 2,

            "name": "Emphysema",

            "price": 500

        },

        {

            "id": 3,

            "name": "Tuberculosis",

            "price": 450

        }

    ],

    "Nervous system": [

        {

            "id": 4,

            "name": "Parkinson",

            "price": 800 	

        },

        {

            "id": 5,

            "name": "Epilepsy",

            "price": 600

        }

    ],

    "Endocrine system": [

        {

            "id": 6,

            "name": "Diabetes",

            "price": 350 	

        },

        {

            "id": 7,

            "name": "Acromegaly",

            "price": 700

        },

        {

            "id": 8,

            "name": "Hashimoto’s thyroiditis",

            "price": 900

        }

    ],   

}


while True:
  print("Bienvenido a la clinica")
  var_1 = input("Por favor seleccione qué acción desea realizar: \n1.Registro y cobro de paciente\n2.Ver pacientes\n3.Menú principal\n => ")
  if not var_1.isnumeric():
    var_1 = input("Por favor ingrese una acción válida: ")

  if var_1 == "1":
    print("Ha seleccionado la opción de Registro y cobro de Clientes")
    
    nombre = input("Por favor ingrese su nombre: ").title()
    if not nombre.isalpha():
      nombre = input("Por favor ingrese un nombre válido: ").title()
    
    last_name = input("Por favor ingrese su apellido: ").title()
    if not last_name.isalpha():
      last_name = input("Por favor ingrese un apellido válido: ").title()
    
    cedula = input("Por favor ingrese su cédula: ")
    if not cedula.isnumeric():
      cedula = input("Por favor ingrese una cedula válida: ").title()
    
    patologias = ["1. Cystic Fibrosis , 2. Emphysema , 3. Tuberculosis , 4. Nervous systems , 5. Epilepsy , 6. Dibetes , 7. Acromegaly , 8. Hasimotos thyroiditis"]

    print(patologias)

    id_patologia = input(f'Por favor seleccione el id su patologia: \n')
    

    if id_patologia == "1":
      print(f"Factura: \n" , [nombre] , [last_name] , [cedula] ,[id_patologia] ,  "Monto total: 300")
    
    if id_patologia == "2":
      print(f"Factura: \n" , [nombre] , [last_name] , [cedula] ,[id_patologia] ,  "Monto total: 500")
    
    if id_patologia == "3":
       print("Factura: \n", [nombre] , [last_name] , [cedula] ,[id_patologia] ,  "Monto total: 450")
    
    if id_patologia == "4":
      print(f"Factura: \n", [nombre] , [last_name] , [cedula] ,[id_patologia] , "Monto total: 800")
    
    if id_patologia == "5":
      print(f"Factura: \n", [nombre] , [last_name] , [cedula] ,[id_patologia] ,  "Monto total: 600")
    
    if id_patologia == "6":
      print(f"Factura: \n", [nombre] , [last_name] , [cedula] ,[id_patologia] , "Monto total: 350")
    
    if id_patologia == "7":
      print(f"Factura: \n", [nombre] , [last_name] , [cedula] ,[id_patologia] , "Monto total: 700")
    
    if id_patologia == "8":
      print(f"Factura: \n", [nombre] , [last_name] , [cedula] ,[id_patologia] , "Monto total: 900")


  elif var_1 == "2":
    print("Ha escogido ver pacientes")
    print("pacientes")

  
  else:
    print("Menu Principal")
    var_3 = (input("Escoja que acción desea tomar: \n1.Registro y cobro de paciente\n2.Ver pacientes\n3.Salir\n =>"))

    if var_3 == "3":
      print("Su sesión ha cerrado")
      break 
    
  