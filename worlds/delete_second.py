from xml.dom import minidom

def remove_duplicate_poses(file_path):
    # Wczytanie pliku XML
    doc = minidom.parse(file_path)
    
    # Znalezienie wszystkich elementów <pose>
    poses = doc.getElementsByTagName('pose')
    
    # Tworzenie słownika, w którym kluczem jest wartość <pose>, a wartością jest lista indeksów powtarzających się elementów
    pose_dict = {}
    for index, pose in enumerate(poses):
        pose_value = pose.firstChild.nodeValue.strip()
        if pose_value in pose_dict:
            pose_dict[pose_value].append(index)
        else:
            pose_dict[pose_value] = [index]
    
    # Usunięcie powtarzających się elementów
    for pose_indexes in pose_dict.values():
        if len(pose_indexes) > 1:
            for index in pose_indexes[1:]:
                pose = poses[index]
                include = pose.parentNode
                include.parentNode.removeChild(include)
    
    # Zapisanie zmodyfikowanego pliku
    with open(file_path, 'w') as f:
        f.write(doc.toxml())

# Wywołanie funkcji z podaniem ścieżki do pliku XML
remove_duplicate_poses('baylands_droniada.world')