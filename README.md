# Stem Extractor

Extension Spicetify qui ajoute un bouton pour **extraire les stems** (voix /
batterie / basse / autres) du morceau écouté, directement depuis Spotify.

Au clic, un menu propose **Extraction Rapide** (htdemucs) ou **Extraction
Qualité** (htdemucs_ft). Les morceaux s'enchaînent dans une **file d'attente**
avec barre de progression, temps restant estimé, et possibilité d'annuler.

## ⚠️ Nécessite SpiceUtils

La séparation des stems tourne sur un **serveur local** fourni par l'application
**SpiceUtils** (Python + Demucs). L'extension seule ne suffit pas.

➡️ **Téléchargez SpiceUtils :** https://github.com/noahhrcy/SpiceUtils/releases

Une fois SpiceUtils installé et son serveur démarré (onglet *Serveur*), le bouton
fonctionne. Si le serveur n'est pas détecté, l'extension propose le lien de
téléchargement.

## Utilisation

- Bouton dans la barre de lecture, ou clic droit sur un titre.
- Les stems sont enregistrés dans le dossier configuré dans SpiceUtils
  (par défaut `Téléchargements/Stems`).

## Licence

MIT.
