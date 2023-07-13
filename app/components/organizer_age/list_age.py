import os 
import datetime

from ..create_folder.create_by_folder import create_folder


def obtener_ano_creacion(path_route: str) -> int:
    """_summary_

    Args:
        path_route (str): Ruta principal para crear los archivos.

    Returns:
        int: Año de creación del archivo.
    """
    time_create = os.path.getctime(path_route)
    date_create = datetime.datetime.fromtimestamp(time_create)
    age_create = date_create.year
    return age_create


def list_all_files(path_route: str = "undefined") -> None:
    """_summary_

    Args:
        path_route (str, optional): Ruta principal para crear los archivos. Defaults to "undefined".
    """
    files_path: list[str] = []
    folder_age: set = set()
    
    if not path_route == "undefined":
        for route, _, files in os.walk(path_route):
            for file in files:
                files_path.append(os.path.join(route, file))
                folder_age.add(obtener_ano_creacion(os.path.join(route, file)))
                
    create_folder(folder_age, path_route)