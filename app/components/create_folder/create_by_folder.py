import os


def create_folder_age(create_age: set, path_route: str = "undefined") -> None:
    """_summary_

    Args:
        create_age (set): Conjunto de edades de los archivos.
        path_route (str, optional): Ruta principal para crear los archivos. Defaults to "undefined".
    """
    
    if not path_route == "undefined":
        os.mkdir(path_route + "/Organizer")
        os.chdir(path_route + "/Organizer")
        
        for age in create_age:
            os.mkdir(age)
            os.mkdir(age + "/documentos_{0}".format(age))