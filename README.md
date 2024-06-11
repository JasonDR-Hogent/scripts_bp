# scripts_bp
Deze repository bevat de scripts die gebruikt zijn bij het ontwikkelen van een bachelorproef die onderzoek voert naar een manier om computervisie en AI te combineren op een microcontroller. Het doel hiervan was om het aantal etende biggen te kunnen tellen en de data weg te schrijven.

# Bestanden
- `script.py`: Dit is het script dat uitgevoerd wordt op de microcontroller. Het laadt het model in en past het toe op een afbeelding om vervolgens de data weg te schrijven. 
- `video_processor.py`: Dit bestand bevat de een video_processor object. Via verschillende stappen gaat het frame per frame door een video loopen en om de X aantal frames wordt de afbeelding bijgewerkt en opgeslagen. 
- `worker.py`: Dit is een kort script dat puur gebruikt wordt voor het initialiseren van een video_processor object en de workflow uitvoert.
- `trained.tflite`: Dit is het model dat gebruikt is geweest in het `script.py` bestand.

# Model
Het model is terug te vinden in een Edge Impulse repository: https://studio.edgeimpulse.com/studio/368922