# Frogger Zero

Una versione classica del gioco Frogger realizzata con Pygame Zero, a partire dalla porzione di codice offerta da WireFrame e presente ![qui](https://github.com/PythonBiellaGroup/LearningPythonWithGames/tree/main/extra/game-mechanics/frogger)

![Frogger Zero](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pygame Zero](https://img.shields.io/badge/Pygame%20Zero-1.2-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

## 📖 Descrizione

Aiuta la rana ad attraversare la strada trafficata e il fiume pericoloso per raggiungere la zona sicura! Evita le macchine, salta sui tronchi galleggianti e accumula più punti possibile.

## 🎮 Come si gioca

### Obiettivo
Porta la rana dalla parte inferiore dello schermo fino alla zona verde in alto, evitando ostacoli e pericoli.

### Comandi
- **↑ Freccia SU**: Muovi la rana in alto
- **↓ Freccia GIÙ**: Muovi la rana in basso
- **← Freccia SINISTRA**: Muovi la rana a sinistra
- **→ Freccia DESTRA**: Muovi la rana a destra
- **SPAZIO**: Riavvia il gioco (dopo Game Over)

### Regole
- 🚗 **Evita le macchine**: Se vieni investito, perdi una vita
- 🪵 **Salta sui tronchi**: Nel fiume devi stare sui tronchi galleggianti
- 💀 **Non cadere in acqua**: Se finisci nel fiume senza un tronco, muori
- ⭐ **Raggiungi la zona sicura**: Ogni volta che arrivi in alto guadagni 100 punti
- ❤️ **Vite limitate**: Hai 3 vite a disposizione

## 🚀 Installazione

### Requisiti
- Python 3.x
- Pygame Zero

### Installazione dipendenze

```bash
pip install pgzero
```

### Avvio del gioco

```bash
python frogger.py
```

oppure

```bash
pgzrun frogger.py
```

### Asset grafici necessari

Il gioco richiede le seguenti immagini nella cartella `images/`:
- `background.png` - Sfondo del gioco (800x600 pixel consigliati)
- `frog1.png` - Rana ferma
- `frog2.png` - Rana che salta
- `car1.png` a `car6.png` - 6 diversi tipi di veicoli
- `float1.png` a `float5.png` - 5 diversi tipi di tronchi/zattere

## 🎨 Caratteristiche

- **Gameplay classico**: Fedele al Frogger originale
- **Animazioni fluide**: 60 FPS per un'esperienza di gioco ottimale
- **Sistema di punteggio**: Guadagna punti raggiungendo la zona sicura
- **Vite multiple**: 3 vite per tentare di ottenere il punteggio più alto
- **Effetti visivi**: Animazione di salto e lampeggio alla morte
- **6 righe di traffico**: Macchine che si muovono in direzioni alternate
- **5 righe di fiume**: Tronchi galleggianti su cui saltare

## 🛠️ Dettagli tecnici

### Meccaniche di gioco

- **Movimento a griglia**: La rana si muove a scatti di 40 pixel
- **Collision detection**: Sistema preciso di rilevamento collisioni
- **Piattaforme mobili**: I tronchi trasportano la rana con loro
- **Stati di gioco**: Gioco attivo (0), Morte (1), Game Over (2)
- **Wrap-around**: Ostacoli e piattaforme riappaiono dal lato opposto

### Performance

- Ottimizzato per 60 FPS
- Basso utilizzo di risorse
- Compatibile con hardware retrogaming

## 🎲 Suggerimenti di gioco

1. **Tempismo è tutto**: Aspetta il momento giusto prima di attraversare
2. **Resta sui tronchi**: Nel fiume, cerca sempre un tronco su cui saltare
3. **Attenzione ai bordi**: Le macchine escono e rientrano dai lati
4. **Pianifica il percorso**: Guarda avanti e pianifica i tuoi movimenti
5. **Usa tutta la larghezza**: Non limitarti al centro dello schermo

## 📝 Licenza

Questo progetto è rilasciato sotto licenza MIT. Sentiti libero di modificarlo e distribuirlo.

## 🤝 Contributi

I contributi sono benvenuti! Sentiti libero di:
- Segnalare bug
- Proporre nuove funzionalità
- Migliorare il codice
- Aggiungere livelli o modalità di gioco

## 👨‍💻 Autore

Creato con ❤️ usando Pygame Zero

## 🔗 Link utili

- [Learning Python With Games]([https://pygame-zero.readthedocs.io/](https://github.com/PythonBiellaGroup/LearningPythonWithGames/)
- [Pygame Zero Documentation](https://pygame-zero.readthedocs.io/)
- [Python Official Site](https://www.python.org/)

---

**Buon divertimento! 🐸**
