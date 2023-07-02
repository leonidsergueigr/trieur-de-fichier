from pathlib import Path

chemin = {
    '.png':'Images',
    ".jpg":"Images",
    ".jpeg":"Images",
    ".gif":"Images",
    ".ico":"Images",
    ".svg":"Images",
    ".mp4":"Videos",
    ".mov":"Videos",
    ".3gp":"Videos",
    ".zip":"Archives",
    ".rar":"Archives",
    ".docx":"Documents",
    ".pdf":"Documents",
    ".txt":"Documents",
    ".json":"Documents",
    ".mp3":"Musiques",
    ".wav":"Musiques"
}
while True:
    chemin_tri = Path(input("Entrez le chemin où vous voulez faire du tri: "))
    if chemin_tri.is_dir():
        break
    else:
        print("Veuillez entrez un chemin de dossier s'il vous plait!")

fichiers = [f for f in chemin_tri.iterdir() if f.is_file()]
for f in fichiers:
    chemin_sortie = chemin_tri / chemin.get(f.suffix,"Autres")
    chemin_sortie.mkdir(exist_ok=True)
    f.rename(chemin_sortie / f.name)
print(f"{len(fichiers)} fichiers triés avec succès!")