from defusedxml.ElementTree import parse
from typing import Union
import os
import sys
import uuid

from numpy.ma.core import outer

RACE_MAP: dict[str, str] = {
    "Humanoid": "899d275e-9893-490a-9cd5-be856794929f",
    "Human": "0eb594cb-8820-4be6-a58d-8be7a1a98fba",
    "Githyanki": "bdf9b779-002c-4077-b377-8ea7c1faa795",
    "Tiefling": "b6dccbed-30f3-424b-a181-c4540cf38197",
    "Elf": "6c038dcb-7eb5-431d-84f8-cecfaf1c0c5a",
    "Half-Elf/Half-Drow": "45f4ac10-3c89-4fb2-b37d-f973bb9110c0",
    "Dwarf": "0ab2874d-cfdc-405e-8a97-d37bfbb23c52",
    "Halfling": "78cd3bcc-1c43-4a2a-aa80-c34322c16a04",
    "Gnome": "f1b3f884-4029-4f0f-b158-1f9fe0ae5a0d",
    "Drow": "4f5d1434-5175-4fa9-b7dc-ab24fba37929",
    "Dragonborn": "9c61a74a-20df-4119-89c5-d996956b6c66",
    "Half-Orc": "5c39a726-71c8-4748-ba8d-f768b3c11a91"
}


def error_exit(msg: str):
    print(f"[ERROR] {msg}")
    sys.exit(1)


def main():
    # Accept root directory from system arguments or default to current directory
    cwd = os.getcwd()
    if len(sys.argv) >= 2:
        cwd = sys.argv[1]

    # A bit of sanity checking
    if not os.path.exists(os.path.join(cwd, "DIYRaceCCPatch")):
        error_exit("DIYRaceCCPatch does not exist!")

    if not os.path.exists(os.path.join(cwd, "UnpackedMods")):
        error_exit("UnpackedMods does not exist!")

    base_path = os.path.join(cwd, "UnpackedMods")
    mod_folders: list[str] = os.listdir(base_path)

    # Ask user for which race to copy from
    copy_from: str = "Not Real!"
    while copy_from not in RACE_MAP:
        for race in RACE_MAP:
            print(race)
        copy_from = input("Please enter a race above to copy from: ")
    copy_from = RACE_MAP[copy_from]

    # Ask user for race UUID
    folder_or_uuid: Union[str, None] = None
    is_uuid: bool = False
    while folder_or_uuid is None:
        for i in range(len(mod_folders)):
            print(f"{i + 1}: {mod_folders[i]}")
        folder_or_uuid = input("Enter the mod number above containing one race and only cosmetics for that race OR the UUID of your race: ")
        try:
            uuid.UUID(folder_or_uuid)
            is_uuid = True
            break
        except ValueError:  # Not a UUID, check if number in valid range
            try:
                index = int(folder_or_uuid) - 1
                if index >= len(mod_folders) or index < 0:
                    folder_or_uuid = None
                else:
                    break
            except ValueError:
                folder_or_uuid = None

    # Find race UUID if needed
    if is_uuid:
        race_id: str = folder_or_uuid
    else:
        found_id: Union[None, uuid.UUID] = None
        filpath = os.path.join(base_path, mod_folders[index], "Public", mod_folders[index], "CharacterCreation", "CharacterCreationAppearanceVisuals.lsx")
        xml = parse(filpath)
        for elem in xml.iterfind("region/node/children/node/attribute"):
            attribs = elem.attrib
            if "id" in attribs and attribs["id"] == "RaceUUID" and "value" in attribs:
                found_id = attribs["value"]
                break
        if found_id is not None:
            print(f"[INFO] Using Race UUID {found_id}.")
            race_id: str = found_id
        else:
            error_exit("Could not find UUID for race. Please input the UUID manually!")

    # Ask for all the mods to copy from
    indices = []
    while len(indices) == 0:
        for i in range(len(mod_folders)):
            print(f"{i + 1}: {mod_folders[i]}")
        answer = input("Enter the mod number above containing the cosmetics you want to copy. You can use commas in-between to copy multiple: ")
        try:
            indices: list[Union[str, int]] = answer.split(",")
            for i in range(len(indices)):
                indices[i] = int(indices[i]) - 1
                if indices[i] >= len(mod_folders) or indices[i] < 0:
                    indices = []
            else:
                break
        except ValueError:
            indices = []

    # Get all elements from mod to copy from
    new_elements = []
    for copy_from_index in indices:
        source_path = os.path.join(base_path, mod_folders[copy_from_index], "Public", mod_folders[copy_from_index], "CharacterCreation")
        source_path = os.path.join(source_path, os.listdir(source_path)[0])
        hairs_xml = parse(source_path)
        elements = hairs_xml.findall("region/node/children/node")
        for elem in elements:
            copy_in = False
            for attrib in elem.findall("attribute"):
                attrib_id = attrib.attrib["id"]
                if attrib_id == "RaceUUID":
                    if attrib.attrib["value"] == copy_from:  # Only copy over the race we're copying from
                        attrib.attrib["value"] = race_id
                        copy_in = True
                    else:
                        copy_in = False
                        break
                elif attrib_id == "UUID":  # Give it a new UUID so it doesn't conflict with the pre-existing one
                    attrib.attrib["value"] = str(uuid.uuid4())
            if copy_in:
                new_elements.append(elem)

    # Add entries to destination
    dest_path = os.path.join(cwd, "DIYRaceCCPatch", "Public", "DIYRaceCCPatch", "CharacterCreation", "CharacterCreationAppearanceVisuals.lsx")
    dest_xml = parse(dest_path)
    place_to_add = dest_xml.find("region/node/children")
    for elem in new_elements:
        place_to_add.append(elem)
    dest_xml.write(dest_path)


if __name__ == "__main__":
    main()