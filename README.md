# BG3-Hair-Copier

A small Python script to copy hairs (and probably other cosmetic mods, but I haven't tested that) to allow you to use hairs from hair mods on custom races with little effort!

## WARNINGS

These warnings are copied directly from [this how-to](https://www.nexusmods.com/baldursgate3/articles/346) which were immensely helpful in writing this script.

I very humbly ask you to reserve these for personal use. The UUIDs in pretty much every file must be refreshed if you want to publish, otherwise, it will cause a mod conflict. 

And because of how these patches are prone to conflict, I ask that you also send a notice to the creator of the mods in question if you do end up patching something for publishing, so that if a conflict does happen, even if it's by reason of honest mistakes, affected modders will know how to troubleshoot.

## How to Use

1. Install Python. Tested under Python 3.12. Make sure to "Add Python to PATH" in the installer.
2. Download and extract [BG3 Modder's Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool) to a folder.
3. Download [DIYRaceCCPatch](https://www.nexusmods.com/baldursgate3/mods/3861?tab=files&file_id=29009) and extract the "DIYRaceCCPatch" folder inside to the folder you made in step 2.
4. Open BG3 Modder's Multitool.
5. Click on "Configuration" near the top left, and set the "bg3.exe Location" to your Baldur's Gate 3 executable. This is in the "bin" folder of your Baldur's Gate 3 install.
6. In the main window, make sure "Pack .paks to Mods folder instead of zipping" is NOT checked if you plan to give these mods to friends.
7. Drag all the hair mods you want into the "Drop mod workspace folder or a mod .pak here" area. If your mod is in a .zip, you should extract the .zip file, then drag the extracted .pak inside. Do not drag directly from the .zip, you need to extract it first!
8. Download `main.py` from this repository. You can do this by clicking `main.py` above, right-clicking "Raw" near the top-right, then clicking "Save link as...". You should put this file in the same folder as the one you made in step 2.
9. Open a command prompt window by pressing START, typing "cmd", then pressing ENTER.
10. Copy the file path to the folder from step 2, then in the window that opened from step 9, type `cd "THE_FILE_PATH_YOU_COPIED"` replacing `THE_FILE_PATH_YOU_COPIED` with the file path to the folder from step 2 that you copied. Make sure to leave the quotes!
11. Type `pip install -r requirements.txt`, press ENTER, then wait until installing is done. Then type `python main.py`.
12. Enter the race you want to copy hairs from exactly as listed above, then press ENTER.
13. Enter the number corresponding to the mod containing your race above, then press ENTER.
14. Enter the number corresponding to the mod containing the hairs above. If there are multiple, you can enter them separated with commas, such as `4,5,8,11`. Then, press ENTER.
15. Drag the `DIYRaceCCPatch` folder (this should have been made in step 3) into the "Drop mod workspace folder or a mod .pak here" area in the BG3 Modder's Multitool.
16. You should see a new `.zip` file named `DIYRaceCCPatch.zip`. If you don't have file extensions on, you should look for the version of `DIYRaceCCPatch` with a zipper on it. Install this in BG3 Mod Manager as usual, and distribute to others if wanted!
17. You're done! Make sure both the patch mod and all the hair mods you want are enabled, and you're good to go!

## Potential Problems

### BG3 Mod Manager Reports Duplicate Mods with My Mod!

Perform the following steps:

1. Go to `DIYRaceCCPatch` (without the zipper), then `Mods`, then `DIYRaceCCPatch`, 
2. Open `meta.lsx` with notepad. 
3. Open BG3 Modder's Multitool, click the "Generate" button, then click the string of letters and numbers that just generated to copy it.
4. In notepad, find the line that starts with `<attribute id="UUID"` and replace the letters and numbers in the quotes after `value=` with the one you just copied. Make sure to keep the quotes!
5. Save and close the notepad window.
6. Perform the steps in "How to Use" starting from step 15.

## Thanks

Thanks to [this how-to](https://www.nexusmods.com/baldursgate3/articles/346) for how-to perform this process manually. As mentioned, the warning above is copy-pasted from there.