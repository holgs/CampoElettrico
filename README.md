# Campo elettrico e potenziale di un sistema di cariche

Questo progetto utilizza Streamlit per generare un grafico del campo elettrico e del potenziale di un sistema di cariche.

## Requisiti

* Python 3.8 o superiore
* Streamlit
* NumPy
* Matplotlib

## Come usare

1. Clonare il repository da GitHub.
2. Aprire il terminale e spostarsi nella directory del progetto.
3. Eseguire il comando `streamlit run app.py`.

Il grafico del campo elettrico e del potenziale verrà visualizzato nel browser.

## Variabili di configurazione

Il numero di cariche, la densità della griglia e i limiti x e y del grafico possono essere configurati nel file `app.py`.

## Funzioni

Le seguenti funzioni vengono utilizzate per calcolare il campo elettrico e il potenziale di una singola carica e il campo elettrico e il potenziale totali di un sistema di cariche:

* `electric_field(charge, r, r_charge)`
* `potential(charge, r, r_charge)`
* `total_electric_field(charges, r)`
* `total_potential(charges, r)`

## Contributi

Sono benvenuti contributi al progetto. Se trovi un bug o desideri aggiungere una nuova funzionalità, invia un pull request.

## License

Questo progetto è rilasciato sotto la licenza MIT.
