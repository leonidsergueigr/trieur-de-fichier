# Trieur de fichiers

Ce script Python vous permet de trier facilement vos fichiers en les déplaçant dans des dossiers spécifiques en fonction de leur extension.

## Fonctionnement

1. Le programme vous demande d'entrer le chemin du dossier que vous souhaitez trier.

2. Il récupère la liste de tous les fichiers présents dans le dossier.

3. Chaque fichier est déplacé dans un sous-dossier approprié en fonction de son extension, selon la correspondance définie dans le dictionnaire 'chemin'.

4. Les dossiers de destination sont créés automatiquement s'ils n'existent pas encore.

5. Le programme affiche le nombre total de fichiers triés avec succès.

## Exemple de dictionnaire 'chemin'


chemin = {
    '.png': 'Images',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.gif': 'Images',
    '.ico': 'Images',
    '.svg': 'Images',
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.3gp': 'Videos',
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.docx': 'Documents',
    '.pdf': 'Documents',
    '.txt': 'Documents',
    '.json': 'Documents',
    '.mp3': 'Musiques',
    '.wav': 'Musiques'
}

N'hésitez pas à personnaliser ce dictionnaire en fonction de vos besoins de tri.

## Utilisation

1. Assurez-vous d'avoir Python installé sur votre système.

2. Clonez ce dépôt sur votre machine locale.

3. Exécutez le script en utilisant la commande `python trieur.py`.

4. Suivez les instructions pour trier vos fichiers.

## Avertissement

Assurez-vous de sauvegarder vos fichiers importants avant d'utiliser ce script, car il déplacera automatiquement les fichiers dans de nouveaux dossiers.


