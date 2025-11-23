# Importa il modulo Pygame Zero per creare giochi 2D in modo semplificato
import pgzrun
# Importa il modulo random (non utilizzato in questo codice, ma lasciato per eventuali sviluppi futuri)
import random

# === FUNZIONE DI DISEGNO (chiamata automaticamente da Pygame Zero circa 60 volte al secondo) ===
def draw():
    global frame_count
    # Disegna l'immagine di sfondo nella posizione (0,0) - angolo superiore sinistro
    screen.blit("background", (0, 0))
    
    # Disegna tutti i 20 tronchi/zattere (5 righe x 4 colonne = 20)
    for index in range(0, 20):
        floats[index].draw()
    
    # Disegna la rana solo se:
    # - il gioco è attivo (game_state == 0), oppure
    # - la rana è morta (game_state == 1) E il frame è pari (frame_count%2 == 0)
    # Questo crea l'effetto lampeggio quando la rana muore
    if game_state == 0 or (game_state == 1 and frame_count % 2 == 0): 
        frog.draw()
    
    # Disegna tutte le 24 macchine (6 righe x 4 colonne = 24)
    for index in range(0, 24):
        cars[index].draw()
    
    # === INTERFACCIA UTENTE ===
    # Mostra il numero di vite rimanenti in alto a sinistra
    screen.draw.text("Vite: " + str(lives), (20, 20), color="white", fontsize=30)
    # Mostra il punteggio in alto a destra
    screen.draw.text("Punteggio: " + str(score), (600, 20), color="white", fontsize=30)
    
    # Se il gioco è finito (game_state == 2), mostra la schermata di Game Over
    if game_state == 2:
        screen.draw.text("GAME OVER", center=(400, 300), color="red", fontsize=60)
        screen.draw.text("Punteggio finale: " + str(score), center=(400, 350), color="white", fontsize=30)
        screen.draw.text("Premi SPAZIO per ricominciare", center=(400, 400), color="white", fontsize=30)
    
    # Incrementa il contatore globale ad ogni frame
    frame_count += 1
    
# === FUNZIONE DI AGGIORNAMENTO (chiamata automaticamente da Pygame Zero circa 60 volte al secondo) ===
def update():
    global game_state, lives, score
    
    # === STATO 0: GIOCO ATTIVO ===
    if game_state == 0:
        # All'inizio di ogni frame, assume che la rana non sia su nessun tronco
        frog.on_board = -1
        
        # === CONTROLLO VITTORIA ===
        # Se la rana ha raggiunto la zona verde in alto (y < 80)
        if frog.y < 80:
            score += 100  # Aggiungi 100 punti
            reset_frog()   # Riporta la rana alla posizione iniziale
            return        # Esci dalla funzione per evitare ulteriori controlli in questo frame
        
        # === GESTIONE MOVIMENTO OSTACOLI E PIATTAFORME ===
        # Cicla attraverso le 6 righe
        for row in range(0, 6):
            # Determina la direzione di movimento per questa riga
            speed = -1  # Direzione di default: verso sinistra
            if row % 2 == 0: 
                speed = 1  # Le righe pari (0,2,4) vanno verso destra
            
            # Cicla attraverso le 4 colonne
            for col in range(0, 4):
                # Calcola l'indice dell'elemento nell'array (da 0 a 23 per cars, 0 a 19 per floats)
                index = (row * 4) + col
                
                # === MOVIMENTO MACCHINE ===
                cars[index].x += speed  # Muovi la macchina nella direzione speed
                # Se la macchina esce dallo schermo a destra, riportala a sinistra
                if cars[index].x > 840: 
                    cars[index].x = -40
                # Se la macchina esce dallo schermo a sinistra, riportala a destra
                if cars[index].x < -40: 
                    cars[index].x = 840
                # Se la macchina collide con la rana, la rana muore
                if cars[index].colliderect(frog): 
                    game_state = 1
                
                # === MOVIMENTO TRONCHI (solo per le prime 5 righe) ===
                if row < 5:
                    # I tronchi si muovono nella direzione opposta rispetto alle macchine
                    floats[index].x -= speed
                    # Gestione wrap-around per i tronchi
                    if floats[index].x > 880: 
                        floats[index].x = -80
                    if floats[index].x < -80: 
                        floats[index].x = 880
                    
                    # Se il tronco collide con la rana
                    if floats[index].colliderect(frog):
                        frog.on_board = index  # Segna che la rana è su questo tronco
                        frog.x -= speed       # Muovi la rana insieme al tronco
        
        # === GESTIONE ANIMAZIONE SALTO ===
        # Se la rana ha appena saltato (delay > 0)
        if frog.delay > 0:
            frog.delay += 1  # Incrementa il delay
            # Dopo 10 frame, torna all'immagine normale della rana
            if frog.delay > 10:
                frog.image = "frog1"  # Immagine rana normale
                frog.angle = frog.direction  # Applica la rotazione in base alla direzione
        
        # === CONTROLLO MORTE IN ACQUA ===
        # Se la rana è nella zona del fiume (y tra 60 e 270) e non è su un tronco
        if frog.y > 60 and frog.y < 270 and frog.on_board == -1: 
            game_state = 1  # La rana muore
    
    # === STATO 1: RANA MORTA (LAMPEGGIO) ===
    elif game_state == 1:
        # Dopo 30 frame di lampeggio (circa mezzo secondo)
        if frame_count > 30:
            lives -= 1  # Togli una vita
            # Se ci sono ancora vite disponibili
            if lives > 0:
                reset_frog()    # Riporta la rana alla posizione iniziale
                game_state = 0  # Torna allo stato di gioco attivo
            else:
                game_state = 2  # Altrimenti vai allo stato di Game Over

# === GESTIONE INPUT DA TASTIERA ===
def on_key_down(key):
    global game_state, lives, score
    
    # Se il gioco è attivo, gestisci i movimenti della rana
    if game_state == 0:
        # Freccia SU: muovi in alto, rotazione 0 gradi
        if key.name == "UP": 
            move_frog(0, -40, 0)
        # Freccia GIÙ: muovi in basso, rotazione 180 gradi
        if key.name == "DOWN": 
            move_frog(0, 40, 180)
        # Freccia SINISTRA: muovi a sinistra, rotazione 90 gradi
        if key.name == "LEFT": 
            move_frog(-40, 0, 90)
        # Freccia DESTRA: muovi a destra, rotazione 270 gradi
        if key.name == "RIGHT": 
            move_frog(40, 0, 270)
    
    # Se è Game Over e si preme SPAZIO, riavvia il gioco
    elif game_state == 2 and key.name == "SPACE":
        lives = 3      # Ripristina le vite
        score = 0      # Azzera il punteggio
        reset_frog()    # Riporta la rana alla posizione iniziale
        game_state = 0  # Torna allo stato di gioco attivo

# === FUNZIONE MOVIMENTO RANA ===
# Parametri: delta_x e delta_y sono gli spostamenti, direction è la direzione (angolo di rotazione)
def move_frog(delta_x, delta_y, direction):
    # Muovi la rana sull'asse X solo se rimane dentro i limiti dello schermo (0-800)
    if 800 > frog.x + delta_x > 0: 
        frog.x += delta_x
    # Muovi la rana sull'asse Y solo se rimane dentro i limiti dello schermo (0-600)
    if 600 > frog.y + delta_y > 0: 
        frog.y += delta_y
    # Cambia l'immagine alla rana che salta (frog2)
    frog.image = "frog2"
    # Attiva l'animazione del salto impostando delay a 1
    frog.delay = 1
    # Memorizza la direzione per applicarla dopo l'animazione
    frog.angle = frog.direction = direction

# === FUNZIONE RESET RANA ===
# Riporta la rana alle condizioni iniziali
def reset_frog():
    global frame_count
    frog.center = (400, 580)  # Posizione iniziale in basso al centro
    frog.direction = frog.delay = 0  # Resetta direzione e delay dell'animazione
    frog.on_board = -1  # La rana non è su nessun tronco
    frog.image = "frog1"  # Immagine normale della rana
    frog.angle = 0  # Nessuna rotazione
    frame_count = 0  # Resetta il contatore (importante per il lampeggio)

TITLE = "Frogger Zero"
# === INIZIALIZZAZIONE DELLA RANA (PERSONAGGIO GIOCABILE) ===
# Crea l'attore principale: la rana, posizionata in basso al centro dello schermo
frog = Actor('frog1', center=(400, 580))
# Inizializza la direzione della rana (angolo di rotazione) e il delay (usato per l'animazione del salto)
frog.direction = frog.delay = 0
# on_board indica su quale tronco/zattera si trova la rana (-1 = non è su nessun tronco)
frog.on_board = -1

# === INIZIALIZZAZIONE LISTE OSTACOLI E PIATTAFORME ===
# Lista vuota che conterrà tutti gli attori "macchina" (ostacoli sulla strada)
cars = []
# Lista vuota che conterrà tutti gli attori "tronco/zattera" (piattaforme galleggianti sul fiume)
floats = []

# === VARIABILI DI GIOCO ===
# game_state gestisce lo stato del gioco: 0=gioco attivo, 1=rana morta (lampeggio), 2=game over
# frame_count è un contatore globale usato per animazioni e timing
game_state = frame_count = 0
# Numero di vite disponibili per il giocatore
lives = 3
# Punteggio del giocatore
score = 0

# === CREAZIONE OSTACOLI E PIATTAFORME ===
# Ciclo esterno: crea 6 righe (row va da 0 a 5)
for row in range(0, 6):
    # Ciclo interno: crea 4 elementi per ogni riga (colonne)
    for col in range(0, 4):
        # Crea una macchina per ogni posizione
        # car1, car2, ... car6 sono le diverse immagini delle macchine
        # La formula matematica distribuisce le macchine in modo sfalsato su ogni riga
        # (row*20) crea uno sfalsamento iniziale per riga
        # (col*(240-(row*10))) distribuisce le macchine nella riga con spaziatura variabile
        # 540-(row*40) posiziona verticalmente le righe di macchine (ogni riga è 40 pixel più in alto)
        cars.append(Actor('car'+str(row+1), center=((row*20)+(col*(240-(row*10))), 540-(row*40))))
        
        # Crea i tronchi/zattere solo per le prime 5 righe (il fiume ha 5 righe)
        if row < 5: 
            # float1, float2, ... float5 sono le diverse immagini dei tronchi
            # 260-(row*40) posiziona verticalmente le righe di tronchi (zona del fiume)
            floats.append(Actor('float'+str(row+1), center=((row*20)+(col*(240-(row*10))), 260-(row*40))))

# Avvia il gioco con Pygame Zero
pgzrun.go()
