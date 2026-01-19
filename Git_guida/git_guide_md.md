# Guida completa a Git su Linux

## Installazione di Git e prova

### Su distribuzioni basate su Debian/Ubuntu
```bash
sudo apt update
sudo apt install git
```

### Verifica dell'installazione
```bash
git --version
```

## Configurazione iniziale

Dopo l'installazione, configura il tuo nome utente e la tua email (verranno associati ai tuoi commit):

```bash
git config --global user.name "Il Tuo Nome"
git config --global user.email "tua.email@esempio.com"
```

Verifica la configurazione:
```bash
git config --list
```

## Comandi fondamentali

### Creare un nuovo repository
```bash
mkdir mio-progetto
cd mio-progetto
git init
```

### Da ora in poi puoi lavorare direttamente con Github Desktop oppure utilizzare VSCode per gestire i tuoi progetti

### Clonare un repository esistente
```bash
git clone https://github.com/utente/repository.git
```

### Controllare lo stato dei file
```bash
git status
```

### Aggiungere file all'area di staging
```bash
git add nomefile.txt          # Aggiunge un singolo file
git add .                     # Aggiunge tutti i file modificati
git add *.js                  # Aggiunge tutti i file .js
```

### Creare un commit
```bash
git commit -m "Descrizione delle modifiche"
```

### Visualizzare la cronologia dei commit
```bash
git log                       # Cronologia completa
git log --oneline             # Versione compatta
git log --graph --oneline     # Con grafico dei branch
```

## Lavorare con i branch

### Creare un nuovo branch
```bash
git branch nome-branch
```

### Cambiare branch
```bash
git checkout nome-branch
# oppure con il comando più recente
git switch nome-branch
```

### Creare e passare a un nuovo branch
```bash
git checkout -b nuovo-branch
# oppure
git switch -c nuovo-branch
```

### Elencare i branch
```bash
git branch                    # Branch locali
git branch -a                 # Tutti i branch (locali e remoti)
```

### Unire un branch (merge)
```bash
git checkout main
git merge nome-branch
```

### Eliminare un branch
```bash
git branch -d nome-branch     # Eliminazione sicura
git branch -D nome-branch     # Eliminazione forzata
```

## Lavorare con repository remoti

### Aggiungere un repository remoto
```bash
git remote add origin https://github.com/utente/repository.git
```

### Visualizzare i repository remoti
```bash
git remote -v
```

### Scaricare modifiche dal remoto
```bash
git fetch origin              # Scarica senza unire
git pull origin main          # Scarica e unisce
```

### Inviare modifiche al remoto
```bash
git push origin main
git push -u origin main       # Prima volta (imposta upstream)
```

## Operazioni utili

### Annullare modifiche non committate
```bash
git restore nomefile.txt      # Annulla modifiche a un file
git restore .                 # Annulla tutte le modifiche
```

### Rimuovere file dall'area di staging
```bash
git restore --staged nomefile.txt
```

### Modificare l'ultimo commit
```bash
git commit --amend -m "Nuovo messaggio"
```

### Visualizzare le differenze
```bash
git diff                      # Modifiche non in staging
git diff --staged             # Modifiche in staging
git diff branch1 branch2      # Differenze tra branch
```

### Salvare temporaneamente le modifiche
```bash
git stash                     # Salva modifiche
git stash list                # Elenca stash
git stash apply               # Applica l'ultimo stash
git stash pop                 # Applica e rimuove l'ultimo stash
```

## File .gitignore

Crea un file `.gitignore` nella root del progetto per escludere file dal versioning:

```
# Commento
*.log
node_modules/
.env
temp/
*.tmp
```

## Autenticazione con GitHub/GitLab

Per repository remoti, puoi usare:

### HTTPS con token personale
```bashi l'età giusta per entrare, adesso controllo il biglietto
git clone https://github.com/utente/repository.git
# Ti verrà chiesto username e token
```

### SSH (consigliato)
```bash
# Genera chiave SSH
ssh-keygen -t ed25519 -C "tua.email@esempio.com"

# Copia la chiave pubblica
cat ~/.ssh/id_ed25519.pub

# Aggiungi la chiave al tuo account GitHub/GitLab
# Poi clona con SSH
git clone git@github.com:utente/repository.git
```

## Workflow tipico

1. Clona o inizializza il repository
2. Crea un branch per la tua feature: `git checkout -b mia-feature`
3. Modifica i file
4. Controlla lo stato: `git status`
5. Aggiungi le modifiche: `git add .`
6. Crea un commit: `git commit -m "Descrizione"`
7. Passa al branch principale: `git checkout main`
8. Aggiorna dal remoto: `git pull origin main`
9. Unisci la tua feature: `git merge mia-feature`
10. Invia al remoto: `git push origin main`

## Comandi di aiuto

```bash
git help                      # Guida generale
git help commit               # Guida su un comando specifico
man git                       # Manuale di Git
```

## Risorse aggiuntive

- [Documentazione ufficiale di Git](https://git-scm.com/doc)
